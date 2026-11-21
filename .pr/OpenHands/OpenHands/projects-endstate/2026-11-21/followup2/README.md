# Follow-up 2: #19810's PR-status refresher, and Canvas on a released 1.63.1 Agent Server (2026-11-21)

Two checks on the end state from [../README.md](../README.md):

1. OpenHands/OpenHands#19810's new commit `758f4d9954` ("Share one PR status refresher and pause it while the user is away"), live, against the build before it.
2. The same Canvas build against the **released** Agent Server 1.63.1, which has neither Projects (#6602) nor PR recording (#6922): what a user sees if Canvas ships before the SDK release.

## What ran

| Part | Commit |
| --- | --- |
| Canvas end-state merge (fork branch `enyst/OpenHands:verify/projects-endstate-20261121b`) | `9dbf930b15d7b77a9e9bbf1649caef097bd347a7` |
| ↳ OpenHands/OpenHands#19495 | `e537d4937a` |
| ↳ OpenHands/OpenHands#19496 | `6e0554b213` |
| ↳ OpenHands/OpenHands#19810 | `758f4d9954` |
| Control: the previous end-state merge (`verify/projects-endstate-20261121`), #19810 at `c49724334b` | `eed5f10704b0c53ca7453f5d6658497c02a344a1` |
| Agent Server for check 1 | software-agent-sdk main `885242b56`, from source |
| Agent Server for check 2 | released `1.63.1` (`--sdk-version 1.63.1`) |

The 9dbf930 merge differs from eed5f107 only in #19810's three files: `src/hooks/query/use-pull-request-status.ts`, its test, and `src/utils/user-activity.ts`.

Chromium via `verify-openhands`, Paper theme, real model (DeepSeek V4.1 Flash through the LiteLLM eval proxy). PR states were read live from GitHub with a temporary token, deleted afterwards. No credentials appear in these files.

## 1. One PR-status refresher, paused while the user is away

`logs/758f4d9-vitest-typecheck.log`: the hook's 3 tests pass and `tsc --noEmit` is clean.

The live page is worker alpha's conversation in project QA Endstate: its sidebar chip and the Project tab's PRs list both show OpenHands/OpenHands#19810 (`screenshots/F32.prs-refresh/new-prs-tab.png`). Every `GET …/pull-requests/19810` the page sent was counted.

**Before (`eed5f107`, `logs/pr-refresh-old-eed5f107.log`).** Each surface ran its own 60 s `refetchInterval`: 2 requests on load, 4 after 150 s, and 2 more in 75 s with the page untouched. (That idle reading was taken with the page clock moved forward, which does not affect the old build: its `refetchInterval` runs on timers alone.)

**After (`9dbf930`, `logs/pr-refresh-new-9dbf930-realtime.log`), in real time with no clock changes.** The page loaded at 17:35:43Z. The user pressed Shift every 30 s until 17:43:48Z, then left the page untouched until 18:07:54Z, then pressed Shift again (the return). The scripts are in `logs/pr-refresh-real*.sh`. The untouched window was extended once from 18:00:46Z to 18:07Z by restarting the logger, which sends no input.

| When | Expected from the code | Seen |
| --- | --- | --- |
| Load, chip and panel row both mounted | one request, shared | 1 request (17:35:43) |
| 0–5 min, fresh | no requests | none |
| 5–6 min, stale, user active | read once at the next 60 s check | 1 request at 17:41:43, 6:00 after load |
| Untouched, but within 10 min of the last keypress | still present, so stale states are read | 17:47:43 and 17:53:43 (9 min 55 s after the last keypress) |
| Untouched for more than 10 min; stale since 17:58:43 | no requests at the eight checks from 17:59:43 to 18:06:43 | **none** from 17:53:43 to 18:07:54 (14 min) |
| User returns (Shift at 18:07:54) | read at once | 1 request at 18:07:54, the same second |

So the old build reads each PR about once a minute per surface, whether anyone is there or not. The new build reads it once for all surfaces, at most once every 5–6 minutes while someone is there, never while they are away, and at once when they come back. `screenshots/F32.prs-refresh/new-after-return.png` shows the same chip and PRs list after the return.

Browser errors: `logs/errors-note.txt`. The run's log holds only errors from 17:27:46–17:27:59Z, while `restart --rebuild` had the server down; none after 17:35Z, and 0 page and 0 app errors after a clear and reload at the end.

A first attempt that jumped the page clock with Playwright's `setSystemTime` is kept in `logs/pr-refresh-new-clock-skew-attempt.log` only for honesty: it moved `Date.now()` but not timers, so TanStack's own stale timer had not fired and the "stale" phase measured nothing. The real-time run above replaces it.

## 2. Canvas `9dbf930` on the released Agent Server 1.63.1

`control-openhands doctor` on that run: agent-server reachable at version 1.63.1, which meets the UI minimum (1.63.1); served build matches `9dbf930`; UI loads without page errors.

| Check | Result | Files |
| --- | --- | --- |
| Experimental features the server lists | `conversation_reactions`, `ask_user`, `conversation_mentions`, `message_edits`, `factories`: no `projects` | `logs/sdk1631-experimental-features.json`, `screenshots/SDK1631/settings-experimental.png` |
| `GET /api/projects` | 404 | `logs/sdk1631-api-projects.json` |
| Home | No Projects entry, no error or compatibility banner | `screenshots/SDK1631/home.png` |
| `/projects` typed directly | The "Projects is turned off on this Agent Server. Turn it on in Settings › Experimental." notice | `screenshots/SDK1631/projects-route.png` |
| Browser traffic over home, `/projects`, settings and a chat | 0 requests to `/api/projects`; 0 page errors, 0 app errors | — |
| Plain chat | Asked for `PLAIN-1631-OK`, got exactly `PLAIN-1631-OK`; conversation `finished` on `litellm_proxy/deepseek-v4.1-flash` | `screenshots/SDK1631/plain-chat.png`, `plain-chat.mp4` |

**One wording finding.** On a server without Projects, the `/projects` notice says to turn it on in Settings › Experimental, which has no Projects switch on that server. It is reachable only by typing or following an old `/projects` URL, and it goes away if Canvas raises `compatibility.minimumAgentServer` to the SDK release that ships Projects. Not fixed here.

## Not proven here

- Published packages: Canvas still pins `@openhands/typescript-client` 1.63.1, which has no Projects client; check 1 ran on SDK main from source.
- The hidden-tab path of `isUserIdle` (`visibilityState === "hidden"`): the verify browser keeps its single tab visible. The unit tests cover it.
