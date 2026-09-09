# Findings

The `SR-*` schema for a published vulnerability. Candidate validation lives in [methodology](methodology.md); this file is what to write once a candidate survives.

Identifiers are local to this review, starting at `SR-001`. Allocate the next unused number for each published finding.

## Publish rule

Publish an `SR-*` only when attacker, attack path, evidence, affected asset, and impact are all established. If any of those cannot be established, leave the candidate unpublished.

The Attack Path names the failed **control** and the **exploit**. Impact names the **asset**. Evidence carries code citations from the range.

## Schema

Every published finding includes:

- **ID** — `SR-001`, `SR-002`, …
- **Severity** — Critical, High, Medium, or Low (see [severity](severity.md))
- **Title** — one line that names the exploit and the asset
- **ASVS Reference** — a versioned id `v5.0.0-X.X.X` when a specific requirement is named; otherwise the applicable area name
- **Affected Security Requirement** — the `SEC-*` this finding falsifies, or `none located`
- **Evidence** — citations in the range; label each bullet `Verified:`, `Inference:`, or `Uncertain:`
- **Attacker** — actor and privilege at the trust boundary they occupy
- **Preconditions** — what must already be true
- **Attack Path** — ordered steps, including the control that fails
- **Impact** — what becomes possible against the named asset
- **Why Exploitable** — why the path works in this code, not why the category is famous
- **Recommended Remediation** — the property to restore so the path no longer works
- **Regression Test** — a concrete check a later review can re-run on the same path

## Evidence labels

A finding whose evidence is only `Uncertain:` stays unpublished. `Inference:` may support a finding when it rests on `Verified:` facts from the range. Keep the three labels visible in the conversation report so speculation is not read as a vulnerability.
