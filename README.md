# sdd-security-skills

Two Agent Skills that add application-security reasoning to Spec-Driven Development: a preventive design review before the spec, and an adversarial implementation review after implement.

An SDD loop can specify and implement a change without asking how the design can be abused or whether the implementation is exploitable. This collection is exactly two skills. It is not an orchestrator, scanner, or custom SDD framework.

## The two skills

| Skill | Role | Human guide |
| --- | --- | --- |
| `security-design-review` | **Preventive.** Always **before the spec** is finalized. Records `THREAT-*` and invariant-style `SEC-*` in the *consumer* repository. | [docs/engineering/security-design-review.md](docs/engineering/security-design-review.md) |
| `security-review` | **Verification.** Always **after implement**, against a completed change. Publishes evidenced `SR-*` findings. When `SEC-*` exist, records PASS or FAIL on the same design artifact. | [docs/engineering/security-review.md](docs/engineering/security-review.md) |

They are a pair, not substitutes. Design review produces requirements; implementation review checks the diff and those requirements. Agent process lives in `skills/<name>/SKILL.md`. This README does not repeat it.

## Placement in Spec-Driven Development

- `security-design-review` always runs **before the spec**.
- `security-review` always runs **after implement** (after that work has been reviewed and committed on its own terms). It is not a hook inside another workflow's code-review step.

That timing is the integration. Other SDD toolchains are fine; none is a dependency. The skills are also usable in Spec-Driven Development workflows you already run.

## Traceability

1. `THREAT-*`: credible abuse paths from design review.
2. `SEC-*`: security invariants traced from those threats, written to `docs/security/<feature-slug>.md` in the **consumer** repository (not in this collection).
3. `SR-*`: evidenced findings from implementation review (conversation report).
4. Each located `SEC-*` is marked PASS or FAIL with evidence on that same consumer file.

Identifiers are local to the artifact file, starting at `001`.

## ASVS

OWASP Application Security Verification Standard (ASVS) 5.0.0 is the verification framework, applied **by relevance**: understand the change, then load only applicable areas. Named requirements use the form `v5.0.0-X.X.X`. This collection does not copy ASVS requirement bodies.

## Install

Canonical install is the whole collection:

```bash
npx skills add daviduartedev/sdd-security-skills --all
```

`npx skills add daviduartedev/sdd-security-skills` also works; `--all` installs both skills without selecting them one by one.

The published layout is the portable Agent Skills shape: `skills/<name>/SKILL.md`. Any Agent Skills-compatible harness that reads that layout can load the skills.

- **Claude Code:** `.claude-plugin/plugin.json` (the plugin discovers the skills directory).
- **Cursor:** `.cursor-plugin/plugin.json` with `"skills": "./skills/"`.

## Status

V0.1: initial public collection. Evaluation fixtures and a reasoning-quality harness are future work. See [CHANGELOG](CHANGELOG.md) and [CONTRIBUTING](CONTRIBUTING.md).

## License

Original collection text is MIT. See [`LICENSE`](LICENSE).

OWASP ASVS 5.0.0 is licensed under CC BY-SA 4.0. Attribution, and the statement that this project is not affiliated with or endorsed by OWASP or any other author, are in [`NOTICE`](NOTICE).
