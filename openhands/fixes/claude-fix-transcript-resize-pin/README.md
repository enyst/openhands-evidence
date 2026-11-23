# Transcript stays at the bottom when it resizes (OpenHands#20004)

AI-generated on behalf of Engel Nyst (Claude Code).

- Issue: https://github.com/OpenHands/OpenHands/issues/20004
- Branch: `claude/fix-transcript-resize-pin`
- Source commit: OpenHands/OpenHands `da3523d6b65fde3d7e90f94383e40a6eb549a815` (base `c5e47c4`)
- Date: 2026-11-23
- Stack: `verify-openhands` `control-openhands launch --new` from the fix worktree; local backend, Agent Server 1.63.1; LLM `litellm_proxy/deepseek-v4-flash`.
- "Before" screenshots are in the issue (`openhands/bugs/2026-11-23/transcript-resize-bottom/`).

## Steps

1. `conversation start --prompt "Write a numbered list of 60 short lines, one word each. Do not run any tools." --wait`
2. `browser viewport desktop`, `browser goto /conversations/<id>`, measure `scrollHeight - scrollTop - clientHeight` of `[data-testid=chat-scroll-container]`.
3. `browser viewport phone`, measure again. Then the reverse, a scrolled-up reader, the right-panel toggle, and a streamed follow-up reply.

## Results (after the fix)

| Check | Before resize | After resize |
|---|---|---|
| desktop 1440x1000 -> phone 390x844 | sh 1632 st 818 ch 814, gap 0 | sh 1656 st 1006 ch 650, gap 0 (was 188 on main) |
| fresh phone -> desktop | gap 0 | gap 0 |
| scrolled up (scrollTop 300), desktop -> phone | st 300 | st 300 (kept) |
| right panel opens at desktop (chat 768 -> 538 px wide) | sh 1632 st 818, gap 0 | sh 1656 st 842, gap 0 |
| right panel closes | gap 0 | gap 0 |
| streamed follow-up reply, sampled every 250 ms | | max 28 px mid-stream (one line between frames), 0 at the end |

The model's reply text differs from the issue's run (it counted down), so the
absolute heights differ; the desktop -> phone growth is the same 188 px.

## Files

- `desktop-to-phone-after.png`: after desktop -> phone, the reply ends at its last line above the composer.
- `phone-to-desktop-after.png`: fresh phone load resized to desktop, at the bottom.
- `scrolled-up-keeps-position.png`: a reader scrolled up at desktop keeps scrollTop 300 after the resize to phone (scroll-to-bottom button shown).
- `side-panel-toggle-1.png`: right panel opened at desktop, transcript still at the bottom.
- `streaming-follows-after.png`: a streamed follow-up reply ends at the bottom.
