# sdd-security-skills / daviduartedev skills

Composable Agent Skills for spec-driven work: an AppSec pair, a plain-language companion for that pair, plus a human smoke gate after implement. The published GitHub repository is `daviduartedev/skills`.

## Language

**security-design-review**:
Preventive AppSec review of a change whose implementation spec is not yet finalized.
_Avoid_: design understood

**security-review**:
Adversarial AppSec review of a completed implementation against a fixed point.
_Avoid_: generic code review, standards-or-spec quality pass

**teach-me-sec**:
Working-literacy companion of a `security-design-review` or `security-review`.
_Avoid_: fourth AppSec review, course, rewrite of the AppSec file

**explained companion**:
The derived file `docs/security/<feature-slug>-explained.md`.
_Avoid_: source of truth, `SEC-*` register, AppSec review

**smoke-test-list**:
Human-observable smoke checklist of a completed implementation, after a local run on a free port.
_Avoid_: automated test suite, AppSec findings, commit on the agent's initiative

**description**:
The YAML `Use when` pointer that fires a published skill.
_Avoid_: a second `Use when`; synonym trigger lists

**completion criteria**:
Observable facts that mark a skill run done.
_Avoid_: examined, understood, evaluated, considered

**ASVS mapping**:
The collection's single ASVS 5.0.0 applicability roster.
_Avoid_: the same roster in `SKILL.md`

**consumer repository**:
The repository that installs this collection and holds the design-review artifact and any explained companion.

**fixed point**:
The commit range or stated implementation scope that bounds a `security-review`.

**`THREAT-*`**:
A credible abuse path on a design-review artifact, local to that file.

**`SEC-*`**:
An implementation-independent security invariant traced from a `THREAT-*`, local to that file.

**`SR-*`**:
An evidenced finding from `security-review`, published in the conversation report.
