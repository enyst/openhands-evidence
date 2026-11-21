#!/bin/bash
# Count PR-status requests for OpenHands/OpenHands#19810 from the running Canvas.
# usage: pr-refresh.sh <label> <phase>
#   phase steady : open worker alpha with chip + Project tab PRs, count for 150 s
#   phase stale  : jump the page clock +6 min (user active), count for 75 s
#   phase idle   : jump the page clock +11 min more (no activity), count for 75 s
#   phase back   : scroll (user returns), count for 15 s
set -u
cd "$(dirname "$0")/../../.."
export PATH="$PWD/.agents/skills/verify-openhands/scripts:$PATH"
export OH_VERIFY_RUN=$(cat .amp/in/r21/canvas-run)
B="control-openhands browser"
LABEL=$1; PHASE=$2
OUT=.amp/in/r22/pr-refresh-$LABEL.log
count() { $B network --filter 'pull-requests/19810' --last 200 | python3 -I -c "
import json,sys; d=json.load(sys.stdin); rows=d.get('recent') or d.get('rows') or []
print(len(rows), [r.get('status') for r in rows])"; }
say() { echo "$(date +%H:%M:%S) $*" | tee -a "$OUT"; }
case $PHASE in
  steady)
    $B clock --offset-ms 0 >/dev/null
    $B network --clear >/dev/null
    $B goto /conversations/6ced6fd9dcf342b4ae2353de682da153 >/dev/null
    $B wait testid=project-conversation-pr >/dev/null
    [ "$($B visible testid=conversation-right-panel | python3 -I -c 'import json,sys;print(json.load(sys.stdin)["visible"])')" = True ] \
      || $B click testid=right-panel-toggle >/dev/null
    $B click testid=conversation-tab-project >/dev/null
    $B click testid=project-panel-tab-prs >/dev/null
    $B wait testid=project-panel-pr >/dev/null
    say "surfaces: chip=$($B count testid=project-conversation-pr | python3 -I -c 'import json,sys;print(json.load(sys.stdin)["count"])') panel-rows=$($B count testid=project-panel-pr | python3 -I -c 'import json,sys;print(json.load(sys.stdin)["count"])')"
    say "after load: $(count)"
    sleep 150
    say "after 150 s: $(count)"
    ;;
  stale)
    $B network --clear >/dev/null
    $B clock --system +360000 >/dev/null
    $B scroll testid=conversation-chat-panel --by 10 >/dev/null
    sleep 75
    say "stale (+6 min, active), after 75 s: $(count)"
    ;;
  idle)
    $B network --clear >/dev/null
    $B clock --system +1080000 >/dev/null
    sleep 75
    say "idle (+18 min, untouched), after 75 s: $(count)"
    ;;
  back)
    $B network --clear >/dev/null
    $B scroll testid=conversation-chat-panel --by 10 >/dev/null
    sleep 15
    say "back (scroll), after 15 s: $(count)"
    ;;
esac
