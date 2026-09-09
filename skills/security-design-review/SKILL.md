---
name: security-design-review
description: "Use when the implementation spec is not yet finalized."
---

# security-design-review

Preventive application-security review of a change whose implementation spec is not yet finalized. Produce credible abuse paths and persist invariant-style `SEC-*` requirements in the consumer repository.

## Process

1. Ground the review in available evidence: conversation, requirements, the consumer repo, architecture, ADRs, `CONTEXT.md`, authentication, authorization, data model, actors, and integrations. Record only what those sources show. Mark uncertainty.

2. Establish actors, attacker capabilities, assets, entry points, data flows, trust boundaries, privilege boundaries, external systems, sensitive operations, and attack surface. Load [methodology](references/methodology.md) for how to derive each from evidence.

3. Identify credible abuse paths. For each candidate threat, record attacker, prerequisite, attacker-controlled input or capability, attack path, affected asset, and impact. Keep a threat only when that path is credible in this design.

4. Convert each material risk into an implementation-independent `SEC-*` invariant. Load [security requirements](references/security-requirements.md) for wording, local `THREAT-*`/`SEC-*` identifiers, and traceability.

5. Resolve the feature slug: the value the user supplied; otherwise the branch, feature, or spec title; otherwise ask before writing the file.

6. Apply only relevant OWASP ASVS 5.0.0 areas from the [ASVS applicability mapping](../_shared/asvs-mapping.md). If that file is missing, skip structured ASVS coverage and say the mapping was absent.

7. Write or update `docs/security/<feature-slug>.md` in the consumer repository. Print the same review in the conversation.

## Output

Path in the consumer repo: `docs/security/<feature-slug>.md`.

Include a section only when it adds value: Scope, Actors, Assets, Trust Boundaries, Attack Surface, Threats/Abuse Cases, Security Requirements, ASVS Coverage, Assumptions, Out of Scope.

## Completion criteria

The review is done when all of the following hold:

- Attack surface listed in `docs/security/<feature-slug>.md`
- Trust boundaries named there with both sides
- Each surviving `THREAT-*` recorded there with attacker, path, asset, and impact
- Each material `THREAT-*` has a `SEC-*` on that file
- Each applicable ASVS area recorded there as applied or skipped with reason, or the file states the mapping was absent
- Assumptions listed there, or the file states none
- The same review printed in the conversation
