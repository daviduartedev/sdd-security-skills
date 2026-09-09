# Security requirements

How to write `SEC-*` invariants. Load this when converting a material `THREAT-*` into a requirement. The conversion step lives in `SKILL.md`; this file is wording and traceability.

## Invariant wording

State a property that must remain true of the running system. Subject, obligation, and object: who or what is constrained, what must hold, over which resources or operations.

Write in the present tense as a rule the implementation must preserve, not as a task for the current ticket.

## Implementation independence

Name the security property, not the mechanism. The spec and the code remain free to choose any correct enforcement (query filter, policy engine, storage isolation) as long as the invariant holds.

A requirement that names a library, ORM helper, file, or framework call is an implementation instruction. Rewrite it as the property that helper was meant to guarantee.

## Traceability

Identifiers are local to this artifact. They are not a repo-wide counter.

- Threats: `THREAT-001`, `THREAT-002`, …
- Requirements: `SEC-001`, `SEC-002`, …

Every `SEC-*` names the `THREAT-*` it exists to stop. One threat may justify several requirements; one requirement may trace from several threats when they share a property. Do not emit a `SEC-*` with no threat, or a surviving material threat with no requirement.

Reuse an existing `SEC-*` when updating the artifact for the same feature and the property is unchanged. Allocate the next unused number only for a new property.

## Granularity

One requirement, one testable property. Split when two threats need independent controls (authentication vs object authorization). Merge when several threats are stopped by the same property.

Scope the invariant to the assets and operations this design actually exposes.

## Testability

A later implementation review must be able to pass or fail the requirement with evidence from a diff. If you cannot say what observation would falsify it, the wording is still a wish: tighten the subject, the operation, or the asset until a counterexample is imaginable.

## Examples

Good: Every operation on tenant-owned resources must enforce access against the authenticated tenant.

Bad: Use Prisma `organizationId` in every query.

The good example states the property (tenant-scoped access on tenant-owned resources). The bad example freezes one persistence pattern and cannot survive a store change that still preserves tenancy.
