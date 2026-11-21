#!/bin/bash
# Continuation of pr-refresh-real.sh new: stay untouched until 18:07Z, then return.
set -u
cd "$(dirname "$0")/../../.."
export PATH="$PWD/.agents/skills/verify-openhands/scripts:$PATH"
export OH_VERIFY_RUN=$(cat .amp/in/r21/canvas-run)
B="control-openhands browser"
OUT=.amp/in/r22/pr-real-new.log
T0=$(date -j -u -f '%Y-%m-%dT%H:%M:%SZ' 2026-11-21T17:36:46Z +%s)
END=$(date -j -u -f '%Y-%m-%dT%H:%M:%SZ' 2026-11-21T18:07:00Z +%s)
el() { echo $(( $(date +%s) - T0 )); }
say() { echo "$(date -u +%H:%M:%SZ) $*" | tee -a "$OUT"; }
reqs() { $B network --filter 'pull-requests/19810' --last 200 | python3 -I -c "
import json,sys; d=json.load(sys.stdin); rows=d.get('recent') or []
print(len(rows), [(r['ts'][11:19], r.get('status')) for r in rows])"; }
say "(script restarted to extend the untouched window to 18:07Z; no input sent)"
while [ "$(date +%s)" -lt "$END" ]; do sleep 60; say "untouched t=$(el)s: $(reqs)"; done
$B press Shift >/dev/null
say "returned (Shift) at t=$(el)s"
sleep 20
say "after return t=$(el)s: $(reqs)"
$B screenshot --feature F32.prs-refresh --name new-after-return >/dev/null
say "errors: $($B errors --app-only --no-warnings | python3 -I -c 'import json,sys;d=json.load(sys.stdin);print("page",d["pageErrors"],"app",d["appErrors"])')"
say done
