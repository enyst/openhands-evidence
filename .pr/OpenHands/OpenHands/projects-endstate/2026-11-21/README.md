# Projects end state: Canvas #19495 + #19496 + #19810 with SDK #6922 (2026-11-21)

This is a live end-to-end run of the Projects stack as it will look after the three Canvas PRs land on the SDK's current main.

## What ran

| Part | Commit |
| --- | --- |
| Canvas end-state merge (fork branch `enyst/OpenHands:verify/projects-endstate-20261121`) | `eed5f10704b0c53ca7453f5d6658497c02a344a1` |
| ↳ OpenHands/OpenHands#19495 `astra/insider-ui-voice` | `e537d4937a` |
| ↳ OpenHands/OpenHands#19496 `astra/verify-insider-cat-20261106` | `6e0554b213` |
| ↳ OpenHands/OpenHands#19810 `claude/project-thread-mcp0in` | `c49724334b` |
| Canvas base, OpenHands main | `bb526a3bd` |
| SDK / Agent Server, software-agent-sdk main (includes #6602 `fde86c378` and #6922) | `885242b56` |
| TypeScript client | `1.63.1`, packed locally from SDK `885242b56` |

**Source-tested, not package-tested.** The published `@openhands/typescript-client@1.63.1` has no Projects client, so Canvas was built against a client packed from SDK main. Nothing here exercises published npm, PyPI or Docker artifacts.

Every run used the Paper theme, Chromium driven by `verify-openhands`, and a real model: DeepSeek V4.1 Flash through the LiteLLM proxy. No credentials appear in these files.

## Checks without a model (`logs/`)

- `typecheck.log`: `npm run typecheck` clean.
- `eslint.log`: 0 errors, 8 warnings.
- `vitest-full.log`: 11,113 passed and 13 failed. All 13 failures are in `__tests__/scripts/docker-automation-kv-secret.test.ts`, and they are environmental. That test runs bash with only `PATH`, so bash reads the runner's `~/.bashrc`, and the only stderr the test sees is that file's `line 7: /.local/bin/env: No such file`. The merge changes nothing under `scripts/` or `__tests__/scripts/` compared with main.
- `verify-tooling-tests.log`: verify-openhands tooling, 130/130 passed.
- `py-projects.log`: SDK Projects-related pytest, 282 passed.
- `ts-client.log`: TypeScript client tests, 451/451 passed.
- `f36-full.json`: the SDK verify map F36 (Projects), run against a live Agent Server with the real model: 33/33 pass.

## Live Canvas run (`screenshots/`)

| Area | What was shown | Files |
| --- | --- | --- |
| Flag off | No Projects link; `/projects` and existing project URLs show the off notice; members have no badge, no project sidebar, no Project tab and no project-file item; zero `/api/projects` requests | `F32.off/*` |
| Flag toggle | One PATCH; Projects appears | `F30.toggle/projects-on.png` |
| Create | Empty name keeps Create disabled. **Finding:** the first Create failed with 422 because the auto-created `project-coordinator` profile still referenced the seed LLM `default`, which the editor hid behind the fallback name. Editing and saving the profile fixed it | `F32.create/*` |
| Coordinator and board | Coordinator started via Talk, workers alpha and beta. Beta's question sits in Needs you | `F32.coordinator/`, `F32.board/` |
| Update headers | Compact `update_from` headers with working mentions | `F32.headers/` |
| Resolve, reopen, remove, rename | All work; other tags are kept; removing a worker keeps the conversation | `F32.resolve/` |
| PR recording (#6922) | Alpha ran a `./gh` stand-in that prints the PR URL. The server recorded `prs=OpenHands/OpenHands#19810` | `F32.sidebar/`, `F32.panel/` |
| Sidebar (#19810) | Project rows grouped, coordinator first. Without a token the chip shows `[unknown]` (409 from git route). With a token it shows `#19810 Ready`, and idle alpha moves to Needs you | `F32.sidebar/*` |
| Project tab (#19810) | Files: From agents / From you, Attach. PRs: Open · 1 (#19810) and Merged · 1 (software-agent-sdk#6922) | `F32.panel/project-tab-files.png`, `F32.panel/prs-tab-open-and-merged-live-2.png` |
| Files | Upload md/png/pdf/bin; previews; byte-identical download; delete with confirmation; attaching a file in a worker's composer → model read it via `read_artifact` | `F32.files/*`, `F32.attach/` |
| `ask_user` | Gamma's decision card resolved it. In a second project, delta's question was relayed to the coordinator; choosing French gave delta "Option 2: French" and `greet.py` returned "Bonjour" | `F32.relay/*` |
| Memory | MARKER-MEM-58 saved and shown; the mention opens the worker | `F32.memory/` |
| Persistence | Same projects, members, files and memory before and after a restart | `logs/persist-before.txt`, `logs/persist-after.txt` |
| Phone (390 px) | Project page with no overflow; worker badge; drawer with project sidebar | `F32.phone/*` |

## Findings

The fixes and re-checks are in [followup/README.md](followup/README.md): finding 1 is fixed in the SDK, findings 2 and 3 turned out not to be Projects bugs, and finding 4 is fixed in the map.

#19810's later commit `758f4d9` (one shared PR-status refresher, paused while the user is away) and this Canvas build against the released Agent Server 1.63.1 are checked in [followup2/README.md](followup2/README.md).

1. **Stale coordinator profile LLM (confirmed).** Auto-creating `project-coordinator` copied a reference to an LLM profile that no longer existed. Create then failed with 422 and the first click showed no toast. It is not known whether a normally onboarded user can reach this state.
2. **PRs tab sometimes unclickable (seen once).** After the right panel was toggled, another element covered the tab and the click timed out. Toggling again cleared it (`F32.panel/prs-tab-unclickable.png`).
3. **PDF preview blank in headless Chromium.** The iframe renders nothing there. This is a known headless gap; it was not checked in a headed browser.
4. **SDK verify map gap.** F36 does not cover #6922's `prs` tag.

## Not proven

- Published packages, Docker images and Cloud.
- A real `gh pr create`. The PR URL came from a stand-in; the chip states were read from the real GitHub API with a token.
- Failing, draft and checking chip states against a live PR. Only Ready, Merged and unknown were seen.
- Browsers other than Chromium.
