# Follow-up on the end-state findings (2026-11-21)

These are the fixes and re-checks for the four findings in [../README.md](../README.md). Each one was handled on the fork first; nothing here is upstream yet.

## 1. Coordinator profile pointed at a missing LLM: fixed in the SDK

Fork branch `enyst/agent-sdk:fix/project-profile-llm-fallback`, on upstream main `3a893a1b2`:

- `7c614b0e0` fix(projects): build project profiles on the active LLM when the user's names none
- `08af087df` docs(verify): cover the prs tag in F36

**Cause.** A fresh server seeds the `default` agent profile with `llm_profile_ref: "default"`. While there is no real LLM config, no LLM profile of that name is saved, so the reference points at nothing. Canvas launches chats from `default` with the active LLM profile, and falls back to it when a reference is missing, so chats work. The server built `project-coordinator` and `project-worker` by copying that missing reference, and project launches have no client to substitute the active LLM. Creating a project with a coordinator therefore failed with 422.

**Fix.** When the server first builds a project profile, it uses the active LLM profile if the user's profile names an LLM profile that is not saved. A reference to a saved profile is kept as it is. The server still never overwrites an existing project profile, so one already built with the missing reference needs a single edit and Save in Settings › Agents.

**Before and after.** The scenario below ran on fresh Agent Servers: seeded `default`, then `llm preset deepseek` (active LLM `deepseek-flash`), Projects on, then `POST /api/projects` with a coordinator.

| Checkout | `default` agent profile's LLM | `POST /api/projects` | `project-coordinator` LLM |
| --- | --- | --- | --- |
| upstream main `3a893a1b2` | `default` (not saved) | **422** "LLM profile 'default' not found" | `default` |
| fix `7c614b0e0` | `default` (not saved) | **201**, coordinator started | `deepseek-flash` |

The full output is in `logs/profile-main.log`, `logs/profile-fix.log`, `logs/create-main.json` and `logs/create-fix.json`.

- The regression test `test_the_profiles_run_the_active_llm_when_the_users_names_none` fails without the fix. It covers both a missing reference and a saved one as a control.
- Agent-server project and profile tests: 622 passed.

## 2. "No toast on the first click": not a bug

The coordinator profile was pointed at a missing LLM `qa-ghost` again. The first Create click showed the error toast within 309 ms (`screenshots/first-click-toast.png`). The earlier capture came after the toast's 4–6 s lifetime.

## 3. PRs tab unclickable: not a Projects bug

When the right panel closes, it stays on the page, slid off-screen at zero opacity (`w-0 translate-x-full opacity-0`), and the chat panel covers it. The earlier click ran while the panel was closed (`screenshots/panel-closed-no-tab.png`), so Playwright timed out on a tab users cannot see. With the panel open, switching between Files and PRs worked after each of 5 close/open cycles (`screenshots/prs-tab-after-5-toggles.png`).

That closed-panel behaviour belongs to `conversation-main.tsx` on main, which these PRs do not change.

## 4. F36 did not cover `prs`: added

The new `F36.prs` recipe uses a `gh` stand-in that prints a PR URL:

1. A member runs `echo <PR URL>` and then `./gh pr create`. Only the `gh pr create` URL is recorded (`qa-f36/app#412`).
2. The board lists it under `pull_requests`.
3. A client `PATCH` cannot change it, and the next turn keeps it.

The full F36 run on a fresh server from the fix branch, with the real model (DeepSeek V4.1 Flash via proxy), passed **34/34** (`logs/f36-fresh.json`, `logs/F36.prs-*.json`).
