# Verification ledger — run 2026-11-19T0927-95abdc

Revision `e1b8b60f25084a64412c3a2789a921034fc895c7`, local mode, Agent Server 1.62.0, base http://127.0.0.1:18800.

Checks: 5 — pass 4, fail 0, blocked 1, not-run 0, xfail 0, xpass 0. Families: 3.

## Families

| Family | pass | fail | blocked | not-run | xfail | xpass |
|---|---|---|---|---|---|---|
| F06 | 1 | 0 | 0 | 0 | 0 | 0 |
| F18 | 2 | 0 | 0 | 0 | 0 | 0 |
| F26 | 1 | 0 | 1 | 0 | 0 | 0 |

## Checks

| Feature/check | Entry point | Expected → actual | Result | Note | Evidence |
|---|---|---|---|---|---|
| F26.lan-http-origin | LAN origin, conversation start --stay pong | status finished, agent-message pong → status error (dummy key); secure:false/randomUUID undefined/clipboard undefined confirmed; appErrors 0; no error toast | blocked | prerequisite: a working LLM key (DEEPSEEK_API_KEY empty in this session) | `evidence/F26.lan-http-origin/conversation-noreply.png` |
| F06.branch-from-here | Leaving mid-fork: eval chain on 2-user-message conversation (dummy key), loopback desktop | URL stays /conversations, toast 'Branched this conversation' with Open, Open lands on branch with message text in chat-input → URL http://127.0.0.1:18800/conversations while toast visible; toast history 'Branched this conversation Open'; Open -> /conversations/7526c88b...; chat-input 'Reply with only the word PONG.'; 1 user-message; title '... (branch)'. Reproduced twice (2nd strictly literal chain -> 1d2e115d..., same prefill) | pass |  | `evidence/F06.branch-from-here/leave-mid-fork-toast.png` |
| F18.add-skill-modal | LAN origin /skills > Add skill > example Copy | Copied to clipboard; clipboard = example command → aria-label 'Copied to clipboard', enabled false, pageErrors 0, no toast; loopback-tab clipboard '/add-skill https://github.com/OpenHands/extensions/tree/main/skills/code-review' | pass |  | `evidence/F18.add-skill-modal/lan-copy.png` |
| F18.copy-source | LAN origin /skills, qa-hello card + modal copy (fixture written directly to private HOME, not via agent) | Copied to clipboard; clipboard = SKILL.md path → card aria-label 'Copied to clipboard', modal count 0, pageErrors 0; modal aria-label 'Copied to clipboard', modal stays open (count 1); loopback-tab clipboard = full .../private/home/.agents/skills/qa-hello/SKILL.md path both times | pass |  | `evidence/F18.copy-source/lan-card-copy.png` |
| F26.lan-http-origin | LAN origin, user-bubble copy (tab 0 re-pointed to LAN conversation) | aria-label Copied to clipboard, pageErrors 0, no error toast, loopback tab clipboard = prompt → aria-label 'Copied to clipboard'; pageErrors 0; toast history empty; tab 1 clipboard 'Reply with the single word: pong' | pass | Literal order fails: after 'Return with browser goto /' tab 0 is on http://127.0.0.1 Home and hover user-message times out | `evidence/F26.lan-http-origin/copy.png` |
