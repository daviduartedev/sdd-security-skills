---
name: security-design-review
description: "Use when a feature's design is understood and the implementation spec is not yet finalized. Use when establishing attack surface, trust boundaries, credible abuse paths, or SEC-* security invariants before implementation."
---

# security-design-review

Preventive application-security review of a change whose design is understood and whose implementation spec is not yet finalized. Produce credible abuse paths and persist invariant-style `SEC-*` requirements in the consumer repository.

## Process

1. Ground the review in available evidence: conversation, requirements, the consumer repo, architecture, ADRs, `CONTEXT.md`, authentication, authorization, data model, actors, and integrations. Record only what those sources show. Mark uncertainty.

2. Establish actors, attacker capabilities, assets, entry points, data flows, trust boundaries, privilege boundaries, external systems, sensitive operations, and attack surface. Load [methodology](references/methodology.md) for how to derive each from evidence.

3. Identify credible abuse paths. For each candidate threat, record attacker, prerequisite, attacker-controlled input or capability, attack path, affected asset, and impact. Keep a threat only when that path is credible in this design.

4. Convert each material risk into an implementation-independent `SEC-*` invariant. Load [security requirements](references/security-requirements.md) for wording, local `THREAT-*`/`SEC-*` identifiers, and traceability.

5. Resolve the feature slug: the value the user supplied; otherwise the branch, feature, or spec title; otherwise ask before writing the file.

6. Apply only relevant OWASP ASVS 5.0.0 areas. Load [ASVS applicability mapping](../_shared/asvs-mapping.md) when choosing areas. If that file is missing, continue with the area names under Rules. Cite a specific requirement as `v5.0.0-X.X.X` (identifier only).

7. Write or update `docs/security/<feature-slug>.md` in the consumer repository. Print the same review in the conversation.

## Rules

ASVS area names (fallback when the mapping file is absent): V1 Encoding and Sanitization; V2 Validation and Business Logic; V3 Web Frontend Security; V4 API and Web Service; V5 File Handling; V6 Authentication; V7 Session Management; V8 Authorization; V9 Self-contained Tokens; V10 OAuth and OIDC; V11 Cryptography; V12 Secure Communication; V13 Configuration; V14 Data Protection; V15 Secure Coding and Architecture; V16 Security Logging and Error Handling; V17 WebRTC.

## Output

Path in the consumer repo: `docs/security/<feature-slug>.md`.

Include a section only when it adds value: Scope, Actors, Assets, Trust Boundaries, Attack Surface, Threats/Abuse Cases, Security Requirements, ASVS Coverage, Assumptions, Out of Scope.

## Completion criteria

The review is done when all of the following hold:

- Attack surface examined
- Trust boundaries understood
- Credible abuse paths evaluated
- Material risks have `SEC-*`
- Relevant ASVS areas considered
- Assumptions explicit
- Unsupported claims not presented as facts
