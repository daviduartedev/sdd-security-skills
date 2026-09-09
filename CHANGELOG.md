# Changelog

All notable changes to this collection are documented here.

## [0.1.0] — 2026-09-08

Initial public collection (V0.1).

- **security-design-review**: preventive AppSec skill that records `THREAT-*` and invariant-style `SEC-*` in the consumer repo before the spec is finalized.
- **security-review**: verification AppSec skill that publishes evidenced `SR-*` findings after implement, and records `SEC-*` PASS/FAIL when originating requirements are found.
- Package layout for install: `skills/<name>/SKILL.md`, Claude Code (`.claude-plugin`), Cursor (`.cursor-plugin` with a skills pointer). Canonical install is `npx skills add daviduartedev/sdd-security-skills`.
- Lightweight package validation (`scripts/validate-package.py` and GitHub Actions) for published collection invariants.
- Human docs: product README, this changelog, CONTRIBUTING, and per-skill engineering pages under `docs/engineering/`.
