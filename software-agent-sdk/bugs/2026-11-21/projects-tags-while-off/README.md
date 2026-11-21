# Projects off: a client can put a conversation into a project and set its server-owned tags

AI-generated on behalf of Engel Nyst (@enyst) by the daily map-maintenance automation.

The server is OpenHands/software-agent-sdk at main@3a893a1b26de7ec02cc0dd2427906eea6aea3fc7, launched with `control-agent-server launch --new`. The bug was reproduced on two fresh runs; these files are from round 1. Scratch paths are shown as `<scratch>`.

- `round.sh` is the script both rounds ran.
- `round1.log` is its full output, including the 422 the control step got while Projects was on.
- `round1/05-on-patch-tags.json`: with Projects on, the PATCH that adds `project`, `prs` and `resolved` gets 422.
- `round1/08-off-start-tagged.json`: with Projects off, starting a conversation tagged `project=<existing project>` is accepted.
- `round1/11-off-patch-tags.json` and `round1/12-off-get-B.json`: with Projects off, the PATCH that sets `project`, `prs=evil/repo#1` and `resolved=user` is accepted and stored.
- `round1/14-on-project-conversations.json`: after Projects is switched back on, both conversations are listed as members. The patched one shows `attention: resolved`, `resolved: user` and `pull_requests: [evil/repo#1]`.
- `round1/18-on-patch-clear-B.json` and `round1/19-on-get-B-after-clear.json`: a client PATCH can no longer remove the faked tags.
