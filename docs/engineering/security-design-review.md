# security-design-review

Human guide to the preventive skill in this collection. Agent instructions live in `skills/security-design-review/`. This page is for the engineer who decides when to run it and what to do with the result.

## What it does

The skill walks an agent through a design-time application-security review of one change. It builds a picture of actors, assets, trust boundaries, and attack surface, keeps only abuse paths that are credible in *this* design, and turns material risks into `SEC-*` requirements. Each `SEC-*` is an invariant (a property the system must preserve), traced from a `THREAT-*` identifier. IDs are local to the review file, not a global register.

The review is written into the **consumer** repository and printed in the conversation so later spec, implement, and verification sessions can still see it.

## When to run it

In a Spec-Driven Development workflow, run it **after the design is understood and always before the spec is finalized**. That is the slot: security properties exist in time to shape the spec, rather than arriving as after-the-fact comments on an already-written plan.

The skill is model-invoked (the agent can notice the slot from its description). You can also invoke it by name.

Skip it when there is no design yet to review, or when you are already reviewing a finished implementation.

## Input

Whatever already exists for the change:

- Conversation, requirements, and any draft design notes
- The consumer repo: architecture, ADRs, `CONTEXT.md`, authn/authz, data model, actors, integrations

The agent must not invent repository or architecture facts. Gaps show up as assumptions or as explicit uncertainty.

You may supply a **feature slug**. If you do not, the agent uses the branch, feature, or spec title, and asks if none of those exist.

## Output

Two copies of the same review:

1. A markdown file in the consumer repo at `docs/security/<feature-slug>.md` (created or updated)
2. The same content printed in the conversation

Sections appear only when they add value: Scope, Actors, Assets, Trust Boundaries, Attack Surface, Threats/Abuse Cases, Security Requirements, ASVS Coverage, Assumptions, Out of Scope.

ASVS 5.0.0 is applied by relevance (only areas that match the change). Requirement IDs, when named, use the form `v5.0.0-X.X.X`. The skill does not paste ASVS requirement text.

## Example

A tenant-scoped “list invoices” API is about to be specified. After design review, `docs/security/list-invoices.md` might contain:

```markdown
## Threats/Abuse Cases

### THREAT-001
Authenticated member of tenant A supplies tenant B's id and reads B's invoices.

## Security Requirements

### SEC-001
Every operation on tenant-owned resources must enforce access against the authenticated tenant.

Traces from: THREAT-001
```

`SEC-001` does not say which query filter or ORM helper to use. The spec can choose a correct mechanism; a later implementation review can pass or fail the invariant with evidence.

## Non-goals

- Implementation or pull-request review (findings against a diff)
- Running scanners, linters, or a custom SDD orchestrator
- Evaluating every ASVS area on every change
- Inventing a global `SEC-*` numbering scheme across the consumer repo
- Depending on any other author’s skill repository or issue tracker
- Reproducing OWASP ASVS requirement bodies
