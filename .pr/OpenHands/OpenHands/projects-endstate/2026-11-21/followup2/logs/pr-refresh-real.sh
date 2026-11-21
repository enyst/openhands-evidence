#!/bin/bash
# Real-time PR-status refresh timeline for OpenHands/OpenHands#19810 (no clock skew).
# usage: pr-refresh-real.sh <label>
#   0-7 min  : user active (Shift keydown every 30 s)
#   7-24 min : untouched (idle after 17 min)
#   24 min   : Shift keydown (user returns), then 20 s
set -u
cd "$(dirname "$0")/../../.."
export PATH="$PWD/.agents/skills/verify-openhands/scripts:$PATH"
export OH_VERIFY_RUN=$(cat .amp/in/r21/canvas-run)
B="control-openhands browser"
LABEL=$1
OUT=.amp/in/r22/pr-real-$LABEL.log
: > "$OUT"
say() { echo "$(date -u +%H:%M:%SZ) $*" | tee -a "$OUT"; }
reqs() { $B network --filter 'pull-requests/19810' --last 200 | python3 -I -c "
import json,sys; d=json.load(sys.stdin); rows=d.get('recent') or []
print(len(rows), [(r['ts'][11:19], r.get('status')) for r in rows])"; }
$B stop >/dev/null 2>&1
$B start >/dev/null
$B network --clear >/dev/null
$B goto /conversations/6ced6fd9dcf342b4ae2353de682da153 >/dev/null
$B wait testid=project-conversation-pr >/dev/null
[ "$($B visible testid=conversation-right-panel | python3 -I -c 'import json,sys;print(json.load(sys.stdin)["visible"])')" = True ] \
  || $B click testid=right-panel-toggle >/dev/null
$B click testid=conversation-tab-project >/dev/null
$B click testid=project-panel-tab-prs >/dev/null
$B wait testid=project-panel-pr >/dev/null
T0=$(date +%s)
el() { echo $(( $(date +%s) - T0 )); }
say "loaded; clock=$($B eval 'new Date().toISOString()' | python3 -I -c 'import json,sys;print(json.load(sys.stdin)["value"])')"
$B screenshot --feature F32.prs-refresh --name "$LABEL-loaded" >/dev/null
while [ "$(el)" -lt 420 ]; do
  sleep 30
  $B press Shift >/dev/null
  [ $(( $(el) % 60 )) -lt 30 ] && say "active t=$(el)s: $(reqs)"
done
say "last activity at t=$(el)s"
while [ "$(el)" -lt 1440 ]; do
  sleep 60
  say "untouched t=$(el)s: $(reqs)"
done
$B press Shift >/dev/null
say "returned (Shift) at t=$(el)s"
sleep 20
say "after return t=$(el)s: $(reqs)"
$B screenshot --feature F32.prs-refresh --name "$LABEL-after-return" >/dev/null
say "errors: $($B errors --app-only --no-warnings | python3 -I -c 'import json,sys;d=json.load(sys.stdin);print(len(d.get("errors") or d.get("items") or []))')"
say done
