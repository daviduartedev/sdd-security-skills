# Dispatch

How to obtain a source when this run has none. The ordered process lives in `SKILL.md`; load this only on that branch.

`teach-me-sec` still produces no findings of its own. The dispatched skill is the AppSec review; this skill teaches from its output in the same session.

## Infer the slot

Pick one skill:

- Implementation spec still open, or no completed implementation in view: `security-design-review`.
- Completed implementation, or the human named a **fixed point**: `security-review`.
- Slot unclear: ask which of those two.

Run one skill. Leave the other unrun unless the human names it.

## Confirm, then run

Name the skill you will run and wait for a yes. The dispatched skill writes consumer AppSec artifacts (`docs/security/<feature-slug>.md`, `SR-*`, PASS/FAIL).

On yes: load that skill's `SKILL.md`, finish that skill's run, then return here with its output as the source and continue `teach-me-sec` in this session.

On no: stop. Write no explained companion.
