# sdd-security-skills

Two Agent Skills that add application-security reasoning to Spec-Driven Development.

## Language

**security-design-review**:
Preventive AppSec review of a change whose implementation spec is not yet finalized.
_Avoid_: design understood

**security-review**:
Adversarial AppSec review of a completed implementation against a fixed point.
_Avoid_: generic code review, standards-or-spec quality pass

**description**:
The YAML `Use when` pointer that fires a published skill.
_Avoid_: a second `Use when`; synonym trigger lists

**completion criteria**:
Observable facts that mark a review done.
_Avoid_: examined, understood, evaluated, considered

**ASVS mapping**:
The collection's single ASVS 5.0.0 applicability roster.
_Avoid_: the same roster in `SKILL.md`

**consumer repository**:
The repository that installs this collection and holds the design-review artifact.

**fixed point**:
The commit range or stated implementation scope that bounds a `security-review`.

**`THREAT-*`**:
A credible abuse path on a design-review artifact, local to that file.

**`SEC-*`**:
An implementation-independent security invariant traced from a `THREAT-*`, local to that file.

**`SR-*`**:
An evidenced finding from `security-review`, published in the conversation report.
