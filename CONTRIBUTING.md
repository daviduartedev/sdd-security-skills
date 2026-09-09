# Contributing

This repository is a **four-skill** Agent Skills collection: `security-design-review`, `security-review`, `teach-me-sec`, and `smoke-test-list`. Propose changes against that product, not a larger platform.

## Propose a change

1. Open a GitHub issue describing the gap (behaviour, docs, or package invariants).
2. Wait for the issue to be specified before sending a pull request, unless the change is a small doc or validation fix.
3. Keep original collection text in English (en-UK). Do not paste OWASP ASVS requirement bodies; cite versioned IDs (`v5.0.0-X.X.X`) only.

Further skills, orchestrators, scanners, or an evaluation harness need a new spec, not a drive-by PR.

## Scope of this collection

In scope: the published skills, shared ASVS *applicability* mapping, plugin manifests, package validation, and human docs (README, this file, CHANGELOG, `docs/engineering/`).

Out of scope without a new spec:

- Additional skills beyond the four published here
- An SDD orchestrator or wrapper around specify / ticket / implement
- Scanners, CLIs, or SaaS
- Evaluation fixtures, true/false-positive suites, or a test harness for agent reasoning

The `examples/nextjs-saas/` folder is a README stub reserved for later eval work. Do not land an application there in V0.1.

## Install (contributors)

Canonical consumer install (the whole collection):

```bash
npx skills add daviduartedev/skills --all
```

To work on this repo, clone it. Skill sources live at `skills/<name>/SKILL.md`. Any Agent Skills-compatible harness that reads that layout can load them. Claude Code uses `.claude-plugin/plugin.json`; Cursor uses `.cursor-plugin/plugin.json` (skills pointer `./skills/`).

Do not commit `.agents/` or `skills-lock.json`. They are local engineering-skill installs, not part of the published collection.

## Validate

From the repo root:

```bash
python3 scripts/validate-package.py
```

CI runs the same command. The check asserts package invariants (skill files, frontmatter, linked references, manifests, license, and that README / CHANGELOG / CONTRIBUTING exist and are not empty). It does not score review quality.

## Human docs vs agent instructions

- Agent process lives in `skills/*/SKILL.md` and disclosed references. Do not copy that process into README or these contributor notes.
- Engineer-facing skill pages live in `docs/engineering/`. README points at them.
- `AGENTS.md` is for developing *this* repository, not for consumers of the collection.
