# The issue's "Steps to Reproduce", verbatim, printing each check's verdict.
export PATH=/home/user/software-agent-sdk/.agents/skills/verify-agent-server/scripts:$PATH
export AGENT_SERVER_VERIFY_HOME=$S/defects/ask-agent-stats/agent-server
cd /home/user/software-agent-sdk
export AGENT_SERVER_VERIFY_RUN=$(control-agent-server launch --new "$@" --print-run)
control-agent-server doctor >/dev/null && echo "doctor ok; build $(control-agent-server api GET /server_info --field build_git_sha)"
STUB=$(control-agent-server fixture llm-stub --name qa-ask \
  --step 'tool:finish:{"message":"DONE1"}' --step 'reply:SIDE1@usage=1111,11' --print-path)
AGENT="{\"llm\": {\"model\": \"openai/qa-stub\", \"api_key\": \"qa-stub-key\", \"base_url\": \"$STUB/v1\", \"num_retries\": 0}, \"tools\": []}"
A=$(control-agent-server conversation start --body-json "{\"agent\": $AGENT}" --no-autotitle --prompt QA_TURN1 --wait --print-id)
v() { "$@" >/dev/null 2>&1 && echo PASS || echo FAIL; }
control-agent-server ws start /sockets/events/$A --name live --duration 120 >/dev/null
control-agent-server api POST "/api/conversations/$A/ask_agent" --json '{"question": "QA_SIDE_Q1"}' --expect 200 >/dev/null
echo "socket stats event has ask-agent-llm:        $(v control-agent-server ws stop live --contains ask-agent-llm --expect-min 1 --wait 5)"
echo "REST has ask-agent-llm prompt_tokens 1111:   $(v control-agent-server api GET "/api/conversations/$A" --check stats.usage_to_metrics.ask-agent-llm.accumulated_token_usage.prompt_tokens eq 1111)"
echo "base_state.json contains ask-agent-llm:      $(v control-agent-server state cat base_state.json --conversation "$A" --contains ask-agent-llm)"
control-agent-server restart >/dev/null
echo "REST after restart has prompt_tokens 1111:   $(v control-agent-server api GET "/api/conversations/$A" --check stats.usage_to_metrics.ask-agent-llm.accumulated_token_usage.prompt_tokens eq 1111)"
control-agent-server stop >/dev/null
