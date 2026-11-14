#!/usr/bin/env bash
# Gateway continuation of a conversation in each resting status.
# usage: repro.sh LABEL [CHECKOUT]   (run from the TARGET checkout; needs control-agent-server on PATH)
set -u
LABEL=$1; CHECKOUT=${2:-}
export AGENT_SERVER_VERIFY_RUN=$(control-agent-server launch --new --name "gwp-$LABEL" ${CHECKOUT:+--checkout "$CHECKOUT"} --print-run)
trap 'control-agent-server stop >/dev/null' EXIT
control-agent-server doctor | jq -c '{doctor_ok: .ok}'
control-agent-server api GET /server_info --raw-out "$AGENT_SERVER_VERIFY_RUN/si.json" --quiet >/dev/null
jq -c '{build_git_sha, version}' "$AGENT_SERVER_VERIFY_RUN/si.json"
T="$AGENT_SERVER_VERIFY_RUN/fixtures/tmp"; mkdir -p "$T"
# The gateway needs a saved LLM profile to name as the model; a continued
# conversation keeps its own LLM, so this stub is never called.
MODEL=$(control-agent-server fixture llm-stub --name gw-model --step reply:UNUSED --print-path)
control-agent-server llm set --profile gw-model --model openai/qa-stub --base-url "$MODEL/v1" \
  --no-api-key --no-validate --no-activate --num-retries 0 >/dev/null

start() {  # start NAME [extra conversation-start args]; the stub NAME must exist
  local stub=$1; shift
  control-agent-server conversation start --tools none --no-autotitle --print-id "$@" \
    --llm-json "{\"model\": \"openai/qa-stub\", \"base_url\": \"$stub/v1\", \"api_key\": \"qa-stub\", \"num_retries\": 0}"
}
status() { control-agent-server api GET "/api/conversations/$1" --field execution_status; }
report() {  # report CASE ID MARKER STUBNAME
  local case=$1 id=$2 marker=$3 stub=$4
  echo "[$case] status right after response: $(status "$id")"
  sleep 5
  echo "[$case] status 5 s later: $(status "$id")"
  control-agent-server api GET "/api/conversations/$id/events/search" --query source=user --query "body=$marker" \
    --raw-out "$T/u.json" --quiet >/dev/null
  echo "[$case] user messages containing $marker: $(jq '.items|length' "$T/u.json")"
  control-agent-server api GET "/api/conversations/$id/events/search" --query limit=100 --raw-out "$T/e.json" --quiet >/dev/null
  echo "[$case] events (state updates omitted): $(jq -c '[.items[] | (.kind|split(".")|last) + (if .llm_message then ":" + .source + ":" + (.llm_message.content[0].text // "") else "" end)] | map(select(. != "ConversationStateUpdateEvent"))' "$T/e.json")"
  echo "[$case] model calls received by the conversation's stub: $(control-agent-server sink read --name "$stub" | jq '.count // (.requests|length)')"
}
gateway() {  # gateway CASE ID MARKER
  control-agent-server api POST /v1/chat/completions --auth bearer --timeout 180 \
    --header "X-OpenHands-ServerConversation-ID: $2" \
    --json "{\"model\": \"openhands_gw-model\", \"messages\": [{\"role\": \"user\", \"content\": \"$3\"}]}" > "$T/g.json"
  echo "[$1] GATEWAY RESPONSE: $(jq -c '{status, elapsed_ms, body: .response.body, conversation_header: .response.headers["x-openhands-serverconversation-id"]}' "$T/g.json")"
}

echo "=== case A: paused after /interrupt ==="
A=$(control-agent-server fixture llm-stub --name stub-a --step hang:300 --step reply:GW_ANSWER_A --print-path)
ID=$(start "$A" --prompt DIRECT_A)
control-agent-server conversation wait "$ID" --until running --timeout 30 >/dev/null
control-agent-server sink read --name stub-a --expect-min 1 --wait 30 >/dev/null
control-agent-server api POST "/api/conversations/$ID/interrupt" --expect 200 --quiet >/dev/null
control-agent-server conversation wait "$ID" --until paused --timeout 30 >/dev/null
sleep 2
echo "[A] status before gateway call: $(status "$ID")"
gateway A "$ID" GW_TURN_A
report A "$ID" GW_TURN_A stub-a

echo "=== case B: paused after /pause (the run stops after its current step) ==="
B=$(control-agent-server fixture llm-stub --name stub-b --step reply:x --print-path)
# First model call: 4 s, then a `think` tool call, so the run has a next step to stop before.
cat > "$AGENT_SERVER_VERIFY_RUN/fixtures/llm-stub/stub-b.json" <<'JSON'
[{"hang": 4, "tool": "think", "args": {"thought": "x"}}, {"reply": "GW_ANSWER_B"}]
JSON
ID=$(start "$B" --prompt DIRECT_B)
control-agent-server conversation wait "$ID" --until running --timeout 30 >/dev/null
control-agent-server sink read --name stub-b --expect-min 1 --wait 30 >/dev/null
control-agent-server api POST "/api/conversations/$ID/pause" --expect 200 --quiet >/dev/null
sleep 8
echo "[B] status before gateway call: $(status "$ID")"
gateway B "$ID" GW_TURN_B
report B "$ID" GW_TURN_B stub-b

echo "=== case C: finished ==="
C=$(control-agent-server fixture llm-stub --name stub-c --step reply:DIRECT_ANSWER_C --step reply:GW_ANSWER_C --print-path)
ID=$(start "$C" --prompt DIRECT_C --wait)
echo "[C] status before gateway call: $(status "$ID")"
gateway C "$ID" GW_TURN_C
report C "$ID" GW_TURN_C stub-c

echo "=== case D: idle (never run) ==="
Dd=$(control-agent-server fixture llm-stub --name stub-d --step reply:GW_ANSWER_D --print-path)
ID=$(start "$Dd")
echo "[D] status before gateway call: $(status "$ID")"
gateway D "$ID" GW_TURN_D
report D "$ID" GW_TURN_D stub-d

echo "=== case E: error ==="
E=$(control-agent-server fixture llm-stub --name stub-e --step status:401 --step reply:GW_ANSWER_E --print-path)
ID=$(start "$E" --prompt DIRECT_E)
control-agent-server conversation wait "$ID" --until error --timeout 30 >/dev/null
sleep 2
echo "[E] status before gateway call: $(status "$ID")"
gateway E "$ID" GW_TURN_E
report E "$ID" GW_TURN_E stub-e

echo "=== case F: paused after /interrupt, inner route /events/_gateway/run ==="
F=$(control-agent-server fixture llm-stub --name stub-f --step hang:300 --step reply:GW_ANSWER_F --print-path)
ID=$(start "$F" --prompt DIRECT_F)
control-agent-server conversation wait "$ID" --until running --timeout 30 >/dev/null
control-agent-server sink read --name stub-f --expect-min 1 --wait 30 >/dev/null
control-agent-server api POST "/api/conversations/$ID/interrupt" --expect 200 --quiet >/dev/null
control-agent-server conversation wait "$ID" --until paused --timeout 30 >/dev/null
sleep 2
echo "[F] status before gateway call: $(status "$ID")"
control-agent-server api POST "/api/conversations/$ID/events/_gateway/run" --timeout 180 \
  --json '{"role":"user","content":[{"type":"text","text":"GW_TURN_F"}],"run":true}' > "$T/g.json"
echo "[F] INNER ROUTE RESPONSE: $(jq -c '{status, elapsed_ms, body: .response.body}' "$T/g.json")"
report F "$ID" GW_TURN_F stub-f
