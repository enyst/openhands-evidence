#!/bin/bash
source $SCRATCH/env.sh
export AGENT_SERVER_VERIFY_HOME=$AGENT_SERVER_VERIFY_HOME/coord
cd /home/user/software-agent-sdk
export AGENT_SERVER_VERIFY_RUN=$(control-agent-server launch --new --name coord-count-idle --print-run)
W=$AGENT_SERVER_VERIFY_RUN/fixtures/w; mkdir -p $W
AG='{"llm": {"model": "openai/qa-offline", "api_key": "k", "base_url": "http://127.0.0.1:9/v1", "num_retries": 0}, "tools": []}'
A=$(control-agent-server api POST /api/conversations --json "{\"workspace\": {\"working_dir\": \"$W\"}, \"agent\": $AG}" --expect 201 --field id)
B=$(control-agent-server api POST /api/conversations --json "{\"workspace\": {\"working_dir\": \"$W\"}, \"agent\": $AG}" --expect 201 --field id)
C=$(control-agent-server api POST /api/conversations --json "{\"workspace\": {\"working_dir\": \"$W\"}, \"agent\": $AG}" --expect 201 --field id)
echo "A=$A B=$B C=$C"
control-agent-server api GET /api/conversations/search | jq -c '{n:(.response.body.items|length), b:.response.body.broken_items}'
control-agent-server stop >/dev/null
D=$AGENT_SERVER_VERIFY_RUN/server/workspace/conversations
ls $D
rm $D/${B//-/}/base_state.json
echo '{not json' > $D/${C//-/}/meta.json
control-agent-server restart >/dev/null 2>&1 || control-agent-server launch --help >/dev/null
control-agent-server doctor | jq -c .ok
control-agent-server api GET /api/conversations/search | jq -c '{status, n:(.response.body.items|length), b:[.response.body.broken_items[]|{id,reason}]}'
control-agent-server api GET /api/conversations/count | jq -c '.response.body'
control-agent-server api GET /api/conversations/count --query status=idle | jq -c '.response.body'
control-agent-server api GET /api/conversations/search --query status=idle | jq -c '{n:(.response.body.items|length), b:(.response.body.broken_items|length)}'
control-agent-server api GET /api/conversations/search --query limit=1 | jq -c '{n:(.response.body.items|length), b:(.response.body.broken_items|length), next:.response.body.next_page_id}'
control-agent-server api DELETE /api/conversations/$B | jq -c '.status'
control-agent-server api DELETE /api/conversations/$C | jq -c '.status'
control-agent-server api GET /api/conversations/count | jq -c '.response.body'
control-agent-server stop | jq -c .ok
