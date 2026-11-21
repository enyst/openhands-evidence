#!/bin/bash
# usage: round.sh   (uses AGENT_SERVER_VERIFY_RUN)
set -u
C=control-agent-server
S=F36.flag-spoof
run(){ echo; echo "### \$ $*"; "$@"; echo "### exit=$?"; }
run $C api PATCH /api/settings/experimental/projects --json '{"enabled": true}' --save $S/01-flag-on
PID=$($C api POST /api/projects --json '{"name":"qa-spoof"}' --save $S/02-create-project --field id); echo "PID=$PID"
# control (a) while ON
run $C conversation start --no-run --placeholder-agent --tools none --no-autotitle --tag project=$PID --save $S/03-on-start-tagged
# ordinary conversation for (b) while ON
CON=$($C conversation start --no-run --placeholder-agent --tools none --no-autotitle --tag qa=on --print-id --save $S/04-on-start-plain | tail -1); echo "CON=$CON"
run $C api PATCH /api/conversations/$CON --json "{\"tags\":{\"qa\":\"on\",\"project\":\"$PID\",\"prs\":\"evil/repo#1\",\"resolved\":\"user\"}}" --save $S/05-on-patch-tags
run $C api GET /api/conversations/$CON --save $S/06-on-get-patched --field tags
# flag OFF
run $C api PATCH /api/settings/experimental/projects --json '{"enabled": false}' --save $S/07-flag-off
run $C api GET /api/projects/$PID --save $S/07b-off-get-project
A=$($C conversation start --no-run --placeholder-agent --tools none --no-autotitle --tag project=$PID --print-id --save $S/08-off-start-tagged | tail -1); echo "A=$A"
run $C api GET /api/conversations/$A --save $S/09-off-get-A --field tags
B=$($C conversation start --no-run --placeholder-agent --tools none --no-autotitle --tag qa=off --print-id --save $S/10-off-start-plain | tail -1); echo "B=$B"
run $C api PATCH /api/conversations/$B --json "{\"tags\":{\"qa\":\"off\",\"project\":\"$PID\",\"prs\":\"evil/repo#1\",\"resolved\":\"user\"}}" --save $S/11-off-patch-tags
run $C api GET /api/conversations/$B --save $S/12-off-get-B --field tags
# flag ON again
run $C api PATCH /api/settings/experimental/projects --json '{"enabled": true}' --save $S/13-flag-on-again
run $C api GET /api/projects/$PID/conversations --save $S/14-on-project-conversations
run $C api GET /api/conversations/$A --save $S/15-on-get-A --field tags
run $C api GET /api/conversations/$B --save $S/16-on-get-B --field tags
run $C api GET /api/conversations/$CON --save $S/17-on-get-CON --field tags
# after membership: client PATCH tries to clear the spoofed tags on B
run $C api PATCH /api/conversations/$B --json '{"tags":{"qa":"cleared"}}' --save $S/18-on-patch-clear-B
run $C api GET /api/conversations/$B --save $S/19-on-get-B-after-clear --field tags
