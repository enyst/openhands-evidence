#!/usr/bin/env bash
# Repro: a coordinator update saved just before a restart; does the coordinator run on it afterwards?
# Usage: restart-wake.sh NAME   (run under the subreaper)
set -eo pipefail
NAME=$1
cd /home/user/software-agent-sdk
export PATH=$PWD/.agents/skills/verify-agent-server/scripts:$PATH
export AGENT_SERVER_VERIFY_HOME=<scratch>/agent-server
export AGENT_SERVER_VERIFY_RUN=$(control-agent-server launch --new --print-run --name "rw-$NAME")
echo "RUN=$AGENT_SERVER_VERIFY_RUN"
trap 'control-agent-server stop >/dev/null || true' EXIT
control-agent-server doctor | jq -c '{ok}'
control-agent-server llm preset deepseek | jq -c '{ok}'
control-agent-server api POST /api/agent-profiles/qa-rw-agent \
  --json '{"llm_profile_ref": "deepseek-flash", "tools": [{"name": "terminal"}, {"name": "file_editor"}]}' --expect 201 | jq -c '{ok}'
control-agent-server api POST "/api/agent-profiles/$(control-agent-server api GET /api/agent-profiles/qa-rw-agent --field profile.id)/activate" --expect 200 | jq -c '{ok}'
control-agent-server api PATCH /api/settings/experimental/projects --json '{"enabled": true}' --expect 200 | jq -c '{ok}'
mkdir -p "$AGENT_SERVER_VERIFY_RUN/fixtures/qa-rw-cat"
P=$(control-agent-server api POST /api/projects \
  --json "{\"name\": \"qa-rw\", \"coordinator\": {\"working_dir\": \"$AGENT_SERVER_VERIFY_RUN/fixtures/qa-rw-cat\", \"title\": \"qa-rw-cat\"}}" \
  --expect 201 --save "F36.restart-wake/$NAME-project" --field id)
CAT=$(python3 -c 'import sys, uuid; print(uuid.UUID(sys.argv[1]))' \
  "$(control-agent-server api GET "/api/projects/$P" --field coordinator_conversation_id)")
echo "P=$P CAT=$CAT"
M=$(control-agent-server api POST "/api/conversations/$CAT/children" \
  --json '{"title": "qa-rw-member", "task": "Reply with the single word ok and finish. Do not use tools.", "isolation": "shared"}' \
  --expect 201 --save "F36.restart-wake/$NAME-child" --field conversation_id)
echo "M=$M"
date -u +%FT%T.%3NZ
# As soon as the update is saved in the coordinator, restart.
control-agent-server api GET "/api/conversations/$CAT/events/search" --query kind=MessageEvent --query 'body=Update from' \
  --check items len-ge 1 --until-ok 300 >/dev/null
echo "update seen at $(date -u +%FT%T.%3NZ)"
control-agent-server restart | jq -c '{ok}'
echo "restarted at $(date -u +%FT%T.%3NZ)"
control-agent-server api GET "/api/conversations/$CAT" --save "F36.restart-wake/$NAME-cat-after-restart" | jq -c '{status: (.body // .response.body).execution_status, tags: (.body // .response.body).tags}' || true
control-agent-server api GET "/api/conversations/$M" | jq -c '{status: (.body // .response.body).execution_status, tags: (.body // .response.body).tags}' || true
control-agent-server conversation events "$CAT" --show 12 --full --save "F36.restart-wake/$NAME-cat-events-after-restart" >/dev/null
sleep 120
echo "after 2 min at $(date -u +%FT%T.%3NZ)"
control-agent-server api GET "/api/conversations/$CAT" --save "F36.restart-wake/$NAME-cat-after-2min" | jq -c '{status: (.body // .response.body).execution_status, tags: (.body // .response.body).tags}'
control-agent-server conversation events "$CAT" --show 20 --full --save "F36.restart-wake/$NAME-cat-events-after-2min" \
  | jq -c '.events[] | {kind, source, timestamp, sender, text: ((.llm_message.content // []) | map(.text // "") | join(" ") | .[0:160]), action: (.action.kind // null), err: (.error // .reason // null)}'
control-agent-server logs --grep 'missed|Delivering|stale running|reconcil|Catching up|coordinator' | jq -r '.lines[]?' | tail -20 || true
