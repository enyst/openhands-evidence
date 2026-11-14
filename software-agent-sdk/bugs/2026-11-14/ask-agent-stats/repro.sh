#!/usr/bin/env bash
# usage: S=<scratchpad> repro.sh [--checkout PATH]
# Side-question (ask_agent) usage: socket vs REST vs base_state.json vs restart.
set -u
D=$S/defects/ask-agent-stats
export PATH=/home/user/software-agent-sdk/.agents/skills/verify-agent-server/scripts:$PATH
export AGENT_SERVER_VERIFY_HOME=$D/agent-server
cd /home/user/software-agent-sdk
export AGENT_SERVER_VERIFY_RUN=$(control-agent-server launch --new "$@" --print-run)
RUN=$AGENT_SERVER_VERIFY_RUN
control-agent-server doctor >/dev/null && echo "doctor ok" || echo "doctor FAILED"
echo "server build: $(control-agent-server api GET /server_info --field build_git_sha)"

rest() { control-agent-server api GET "/api/conversations/$2" --field . | python3 $D/summ.py "$1" --rest; }
disk() { python3 $D/summ.py "$1" --disk $RUN/server/workspace/conversations/${2//-/}/base_state.json; }
sock() { python3 $D/summ.py "$1" --ws $RUN/captures/$2.jsonl; }
ask()  { control-agent-server api POST "/api/conversations/$1/ask_agent" --json "{\"question\": \"$2\"}" --expect 200 --field response; }
agent() { echo "{\"llm\": {\"model\": \"openai/qa-stub\", \"api_key\": \"qa-stub-key\", \"base_url\": \"$1/v1\", \"num_retries\": 0}, \"tools\": []}"; }

echo; echo "== A. side question on a finished conversation =="
STUB=$(control-agent-server fixture llm-stub --name qa-ask \
  --step 'tool:finish:{"message":"DONE1"}' --step 'reply:SIDE1@usage=1111,11' \
  --step 'reply:SIDE2@usage=2222,22' --step 'tool:finish:{"message":"DONE2"}' \
  --step 'reply:SIDE3@usage=3333,33' --print-path)
A=$(control-agent-server conversation start --body-json "{\"agent\": $(agent $STUB)}" --no-autotitle --prompt QA_TURN1 --wait --print-id)
rest "A1 after turn 1 (finished)" $A
control-agent-server ws start /sockets/events/$A --name a-ask1 --duration 120 >/dev/null
echo "ask 1 -> $(ask $A QA_SIDE_Q1)   (stub usage 1111/11)"
sleep 1; control-agent-server ws stop a-ask1 >/dev/null
sock "A2 after ask 1" a-ask1; rest "A2 after ask 1" $A; disk "A2 after ask 1" $A
control-agent-server restart >/dev/null && echo "-- server restarted (graceful) --"
rest "A3 after restart" $A; disk "A3 after restart" $A
control-agent-server ws start /sockets/events/$A --name a-ask2 --duration 120 >/dev/null
echo "ask 2 -> $(ask $A QA_SIDE_Q2)   (stub usage 2222/22)"
sleep 1; control-agent-server ws stop a-ask2 >/dev/null
sock "A4 after restart + ask 2" a-ask2; rest "A4 after restart + ask 2" $A; disk "A4 after restart + ask 2" $A
control-agent-server conversation send $A --text QA_TURN2 --wait >/dev/null
rest "A5 after turn 2 (finished)" $A; disk "A5 after turn 2 (finished)" $A
control-agent-server ws start /sockets/events/$A --name a-ask3 --duration 120 >/dev/null
echo "ask 3 -> $(ask $A QA_SIDE_Q3)   (stub usage 3333/33)"
sleep 1; control-agent-server ws stop a-ask3 >/dev/null
sock "A6 after ask 3" a-ask3; rest "A6 after ask 3" $A; disk "A6 after ask 3" $A
control-agent-server restart >/dev/null && echo "-- server restarted (graceful) --"
rest "A7 after restart" $A; disk "A7 after restart" $A

echo; echo "== B. side question while a run is blocked on its model =="
HANG=$(control-agent-server fixture llm-stub --name qa-hang --step hang:300 --step 'reply:SIDEB@usage=4444,44' --print-path)
B=$(control-agent-server conversation start --body-json "{\"agent\": $(agent $HANG)}" --no-autotitle --prompt QA_BUSY --print-id)
control-agent-server conversation wait $B --until running --timeout 30 >/dev/null
control-agent-server sink read --name qa-hang --expect-min 1 --expect-max 1 --wait 30 >/dev/null
control-agent-server ws start /sockets/events/$B --name b-ask --duration 120 >/dev/null
T0=$(date +%s%N); R=$(ask $B QA_SIDE_QB); T1=$(date +%s%N)
echo "ask B -> $R in $(( (T1-T0)/1000000 )) ms   (stub usage 4444/44); status: $(control-agent-server api GET /api/conversations/$B --field execution_status)"
sleep 1; control-agent-server ws stop b-ask >/dev/null
sock "B1 after ask, still running" b-ask; rest "B1 after ask, still running" $B; disk "B1 after ask, still running" $B
control-agent-server api POST "/api/conversations/$B/interrupt" --expect 200 >/dev/null
control-agent-server conversation wait $B --until paused --timeout 30 >/dev/null
rest "B2 after interrupt (paused)" $B; disk "B2 after interrupt (paused)" $B

echo; echo "== C. condense on a finished conversation (another socket-pushed stats source) =="
CST=$(control-agent-server fixture llm-stub --name qa-cond --step 'tool:finish:{"message":"DONEC"}' --step 'reply:QA summary@usage=5555,55' --print-path)
CL="{\"model\": \"openai/qa-stub\", \"api_key\": \"qa-stub-key\", \"base_url\": \"$CST/v1\", \"num_retries\": 0"
C=$(control-agent-server conversation start --body-json "{\"agent\": {\"llm\": $CL}, \"tools\": [], \"condenser\": {\"kind\": \"LLMSummarizingCondenser\", \"llm\": $CL, \"usage_id\": \"condenser\"}, \"max_size\": 80, \"keep_first\": 1}}}" --no-autotitle --prompt QA_TURNC --wait --print-id)
rest "C1 after turn 1 (finished)" $C
control-agent-server ws start /sockets/events/$C --name c-cond --duration 120 >/dev/null
control-agent-server api POST /api/conversations/$C/condense --expect 200 >/dev/null && echo "condense -> 200   (stub usage 5555/55)"
sleep 2; control-agent-server ws stop c-cond >/dev/null
sock "C2 after condense" c-cond; rest "C2 after condense" $C; disk "C2 after condense" $C

control-agent-server stop >/dev/null && echo && echo "run stopped: $RUN"
