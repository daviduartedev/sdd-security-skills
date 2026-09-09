---
name: security-review
description: "Use when a completed implementation needs adversarial AppSec review."
---

# security-review

Adversarial application-security review of a completed implementation against a **fixed point**. Publish only evidenced `SR-*` findings with a credible attack path. When originating `SEC-*` exist, record PASS or FAIL with evidence on that design-review artifact.

## Process

1. Establish the **fixed point**: the user-stated range, or infer the current diff, branch comparison, pull request, or stated implementation scope. When comparing branches, use three-dot `git diff <fixed-point>...HEAD`. Stop if the range is empty or the scope cannot be established. Load [methodology](references/methodology.md) for pinning the range, scoped reading, candidate validation, evidence grades, false-positive rejection, and checking `SEC-*`.

2. Read surrounding code only when a security boundary is otherwise unclear.

3. Identify candidate issues. Validate each attack path. Keep a candidate only when attacker, control, preconditions, vulnerable path, asset, exploit, impact, and code evidence can all be established. Load [findings](references/findings.md) for the `SR-*` schema. Load [severity](references/severity.md) when assigning Critical, High, Medium, or Low.

4. Apply only relevant OWASP ASVS 5.0.0 areas from the [ASVS applicability mapping](../_shared/asvs-mapping.md). If that file is missing, skip structured ASVS coverage and say the mapping was absent.

5. Locate originating `SEC-*` in this order: (1) an explicit path the user supplied, (2) the originating spec, issue, or conversation, (3) consumer `docs/security/*.md` tied to this change. When found, mark each `SEC-*` PASS or FAIL with evidence on that file and append a Verification section with `SR-*` summaries. When none are found, still review the range and state that no `SEC-*` were found. PASS and FAIL are recorded only for requirements that search actually located.

6. Print the full report in the conversation (`SR-*`).

## Output

Primary: the conversation report of `SR-*` findings.

When `SEC-*` are found on the design-review artifact (`docs/security/<feature-slug>.md` in the consumer repo): write PASS/FAIL and the Verification section only on that file.

Non-specialist explanation: load [teach-me-sec](../teach-me-sec/SKILL.md).

## Completion criteria

The review is done when all of the following hold:

- Fixed point established, or the run stopped because the range was empty
- Surrounding code read only to understand a security boundary
- Every published `SR-*` has a validated attack path
- Each applicable ASVS area recorded in the conversation report as applied or skipped with reason, or the report states the mapping was absent
- `SEC-*` search order followed; PASS/FAIL written only when `SEC-*` were found
- Full conversation report printed
