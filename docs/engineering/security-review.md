# security-review

Human guide to the verification skill in this collection. Agent instructions live in `skills/security-review/`. This page is for the engineer who decides when to run it and what to do with the result.

## What it does

The skill walks an agent through an adversarial application-security review of a *completed* implementation. It pins a **fixed point** (current diff, branch comparison, pull request, or stated implementation scope), keeps only issues with a credible attack path and code evidence, and publishes those as `SR-*` findings in the conversation.

When originating `SEC-*` requirements exist on the design-review artifact, each one is marked PASS or FAIL with evidence on that same file, and a Verification section is appended. The skill does not create a second findings file.

Severity is Critical, High, Medium, or Low from demonstrated exploitability and impact.

## When to run it

In a Spec-Driven Development workflow, run it **always after implement**: after that work has been reviewed and committed on its own terms. It is a later verification step: adversarial AppSec against the finished change, not a standards-or-spec code-quality pass, and not a hook inside another workflow's review.

The skill is model-invoked (the agent can notice a completed implementation from its description). You can also invoke it by name.

Skip it when there is no completed implementation to review, or when you still need a design-time review (that is `security-design-review`).

## Input

- A **fixed point**: you may name a commit, branch, pull request, or implementation scope. If you do not, the agent infers the current diff, branch comparison, or pull request. An empty or unresolvable range stops the review; it does not widen into the rest of the repository.
- Optionally, a path to the design-review artifact that holds `SEC-*`.
- The consumer repo at that range, including surrounding files only where a security boundary needs them.

## Output

1. A conversation report of `SR-*` findings (or an explicit statement that none met the evidence bar).
2. When `SEC-*` were found: updates on that same consumer file (`docs/security/<feature-slug>.md`): PASS or FAIL with evidence per requirement, plus a Verification section summarizing `SR-*`.
3. When no `SEC-*` were found: the conversation still contains the diff review and states that no security requirements were located. PASS/FAIL is not invented.

ASVS 5.0.0 is applied by relevance. Requirement IDs, when named, use the form `v5.0.0-X.X.X`. The skill does not paste ASVS requirement text.

## Example

After implement, a tenant-scoped “list invoices” API is reviewed against `main...HEAD`. The design-review file `docs/security/list-invoices.md` still holds `SEC-001` (every operation on tenant-owned resources must enforce access against the authenticated tenant).

The handler reads `id` from the query and loads the invoice without comparing the record's tenant to the session. Conversation output includes:

```markdown
### SR-001

- **Severity:** High
- **Title:** Cross-tenant invoice read by substituting id
- **ASVS Reference:** v5.0.0-8.2.1
- **Affected Security Requirement:** SEC-001
- **Attacker:** Authenticated member of tenant A
- **Impact:** Read another tenant's invoices
```

On the same design-review file, `SEC-001` is marked FAIL with a citation, and a Verification section is appended:

```markdown
## Verification

Fixed point: `main...HEAD`

- SEC-001: FAIL: invoice load by `id` does not bind to the session tenant (`invoices.ts`)
- SR-001 (High): cross-tenant invoice read; falsifies SEC-001
```

If that file (and every other search step) had contained no `SEC-*`, the same `SR-001` would still be reported, with **Affected Security Requirement** `none located`, and no PASS/FAIL written.

## Non-goals

- Generic code-quality, style, or standards/spec review
- Running inside another workflow's code-review step, or replacing that step
- Running scanners, linters, or a custom SDD orchestrator
- Evaluating every ASVS area on every change
- Inventing PASS/FAIL or a Verification section when no `SEC-*` exist
- A second findings file beside the design-review artifact
- Reproducing OWASP ASVS requirement bodies
- Depending on any other author’s skill repository or issue tracker
