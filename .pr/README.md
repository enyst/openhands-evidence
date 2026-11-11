# Temporary PR artifacts

Agents helping **Engel Nyst** may use this directory for temporary pull-request
review artifacts. Keep review-only material here and link it from the relevant
PR, rather than merging it into upstream repositories' main branches.

This follows the [OpenHands SDK's PR-specific evidence convention](https://github.com/OpenHands/software-agent-sdk/blob/main/AGENTS.md#pr-specific-evidence-documents):
`.pr/` holds temporary reviewer context, not permanent project documentation.

## What belongs here

- Design rationale, investigation notes, and debugging analysis.
- Development-only scripts that demonstrate a change.
- Sanitized logs, live-test evidence, screenshots, and test summaries.
- Other PR-specific material that helps reviewers understand or verify the work.

Production code, permanent documentation, and regression tests belong in their
own repositories. Do not put anything here that needs to be preserved.

## Layout and review links

Use one directory per upstream repository and PR to avoid collisions:

```text
.pr/
├── README.md
└── OpenHands/
    └── software-agent-sdk/
        └── pr-1234/
            ├── README.md
            ├── design.md
            ├── verification.md
            └── scripts/
```

In each PR directory, record the upstream PR URL, the exact source commit tested,
the date, and how to reproduce the checks. Distinguish observed results from
plans or untested claims. When evidence changes, make clear which source commit
it covers. Link reviewers to the relevant files, preferably at an artifact
commit SHA so later edits do not change the cited evidence.

Coordinate with other agents before replacing their files. Upload only the
artifacts needed for that PR, not whole workspaces or raw conversation exports.
Never commit credentials, tokens, secret-bearing files, or private personal data;
check and redact logs and screenshots before uploading.

## Temporary means removable

Artifacts may be removed after review, when the PR closes or merges, or when they
become obsolete. This is not an archive. Keep this convention README; clean up
completed PR directories when their evidence is no longer needed.

The SDK's own `PR Artifacts` workflow notifies reviewers, removes `.pr/` after
approval for same-repository PRs, and opens or updates a cleanup PR if artifacts
reach `main`. **That workflow is not installed in this repository.** Cleanup here
is manual unless automation is added explicitly. Artifacts can live on this
repository's main branch without entering an upstream product branch.

Repository visibility still applies: a link to a private artifact does not grant
reviewers access. Confirm reviewer access before relying on a link, and ask Engel
before changing visibility or sharing restricted material elsewhere.

---

Created by SmolPaws, an AI agent, on behalf of Engel Nyst.
