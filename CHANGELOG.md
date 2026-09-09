# Changelog

All notable changes to this collection are documented here.

## [0.3.0] - 2026-09-09

- **teach-me-sec**: working-literacy companion of `security-design-review` and `security-review`. Writes `docs/security/<feature-slug>-explained.md` (en-UK) and a conversation copy in the teaching language. No new findings. The AppSec pair points here when the human asks for a non-specialist explanation; those reviews stay done without it.

## [0.2.0] - 2026-09-09

- Published GitHub identity is `daviduartedev/skills`. Canonical install is `npx skills add daviduartedev/skills`.
- Plugin id `daviduartedev-skills`. Cursor display name: World's Okayest Software Developer.
- README follows a personal-collection layout (install, why, categorised reference) in en-UK.
- **smoke-test-list**: after implement, local run on a free port and an unchecked human-observable checklist. No demo passwords, no product-specific defaults.

## [0.1.1] - 2026-09-09

- One `Use when` per skill description, naming the SDD slot only.
- `security-design-review` completion criteria bound to facts in `docs/security/<feature-slug>.md`.
- `security-review` ASVS completion uses the same applied-or-skipped bound.
- ASVS V1-V17 area roster lives only in `skills/_shared/asvs-mapping.md`.

## [0.1.0] - 2026-09-08

Initial public collection (V0.1).

- **security-design-review**: preventive AppSec skill that records `THREAT-*` and invariant-style `SEC-*` in the consumer repo before the spec is finalized.
- **security-review**: verification AppSec skill that publishes evidenced `SR-*` findings after implement, and records `SEC-*` PASS/FAIL when originating requirements are found.
- Package layout for install: `skills/<name>/SKILL.md`, Claude Code (`.claude-plugin`), Cursor (`.cursor-plugin` with a skills pointer). Canonical install is `npx skills add daviduartedev/sdd-security-skills`.
- Lightweight package validation (`scripts/validate-package.py` and GitHub Actions) for published collection invariants.
- Human docs: product README, this changelog, CONTRIBUTING, and per-skill engineering pages under `docs/engineering/`.
