# World's Okayest Software Developer

[![skills.sh](https://skills.sh/b/daviduartedev/skills)](https://skills.sh/daviduartedev/skills)

Agent skills I actually run. Small, composable, and meant to sit in a spec-driven loop rather than replace it. They work with any model. Fork them. Make them yours.

This collection is not an orchestrator, scanner, or custom SDD framework. It is also not affiliated with OWASP or with Matt Pocock.

## Installation

Two ways in. **The plugin manifests in this repo** install the set as a bundle. **[skills.sh](https://skills.sh/daviduartedev/skills)** copies editable skill files into your project, so you can hack on them. Pick one: installing both leaves you with every skill twice.

### 1. Get the skills

**Claude Code**

The plugin lives in [`.claude-plugin/plugin.json`](.claude-plugin/plugin.json). From a clone, add this repository as a plugin; the plugin discovers `skills/`.

**Codex, Cursor, and other agents**

```bash
npx skills add daviduartedev/skills --all
```

`npx skills add daviduartedev/skills` also works; `--all` installs every skill without picking them one by one.

**For tinkerers**

Use the same installer. It writes the skills into your repo as ordinary files you own. Pull later changes with `npx skills update`.

The published layout is the portable Agent Skills shape: `skills/<name>/SKILL.md`.

- **Claude Code:** `.claude-plugin/plugin.json`
- **Cursor:** `.cursor-plugin/plugin.json` with `"skills": "./skills/"`

### 2. Bam — you're ready to go.

No per-repo setup skill. Install, then invoke by name or let the agent reach for a matching `Use when`.

## Why these skills exist

I built them for failure modes I keep seeing when an agent drives spec-driven work.

### #1: The spec never asked how the design can be abused

An SDD loop can specify and implement a change without asking who can abuse it. Security comments arrive after the plan is already frozen.

**The fix** is [`security-design-review`](./skills/security-design-review/SKILL.md) — **always before the spec** is finalised. It records credible `THREAT-*` paths and invariant-style `SEC-*` in the *consumer* repository.

### #2: "Looks fine" is not AppSec

A generic code-review pass will argue style and ticket fit. It will not pin a **fixed point** or insist on a credible attack path.

**The fix** is [`security-review`](./skills/security-review/SKILL.md) — **always after implement**, against a completed change. It publishes evidenced `SR-*` findings. When `SEC-*` exist, it records PASS or FAIL on that same design artefact.

They are a pair, not substitutes. Design review produces requirements; implementation review checks the diff and those requirements.

### #3: The agent said done; nobody ran the app

Implementation can be "finished" in git and still untested by a human. Automated tests do not replace opening the UI on a free port and clicking the thing you asked for.

**The fix** is [`smoke-test-list`](./skills/smoke-test-list/SKILL.md) — after implement, before you treat the change as done. The agent starts the branch locally when a UI exists, prints an unchecked checklist of what you can see, and waits. You work the list. Commits wait for you.

## Reference

These split on one axis: who can invoke them. **User-invoked** skills are reachable only when you type them. **Model-invoked** skills can be invoked by you *or* reached for automatically when the task fits. Everything in this collection is **model-invoked**. Agent process lives in `skills/<name>/SKILL.md`. This README does not repeat it.

### Application security

OWASP ASVS 5.0.0 is the verification framework, applied **by relevance**. Named requirements use the form `v5.0.0-X.X.X`. This collection does not copy ASVS requirement bodies.

**Model-invoked**

- **[security-design-review](./skills/security-design-review/SKILL.md)** — Preventive AppSec review of a change whose spec is not yet finalised. Writes `THREAT-*` and `SEC-*` to `docs/security/<feature-slug>.md` in the consumer repo. [Human guide](docs/engineering/security-design-review.md)
- **[security-review](./skills/security-review/SKILL.md)** — Adversarial AppSec review of a completed implementation against a **fixed point**. Publishes `SR-*` in the conversation; PASS/FAIL on originating `SEC-*` when they exist. [Human guide](docs/engineering/security-review.md)

### Delivery

After implement, a human still has to see the change.

**Model-invoked**

- **[smoke-test-list](./skills/smoke-test-list/SKILL.md)** — Start the implementation branch locally on a **free port** when a UI exists, then print an unchecked checklist of observable checks. Does not commit. [Human guide](docs/engineering/smoke-test-list.md)

## Traceability (AppSec pair)

1. `THREAT-*`: credible abuse paths from design review.
2. `SEC-*`: security invariants traced from those threats, written to `docs/security/<feature-slug>.md` in the **consumer** repository (not in this collection).
3. `SR-*`: evidenced findings from implementation review (conversation report).
4. Each located `SEC-*` is marked PASS or FAIL with evidence on that same consumer file.

Identifiers are local to the artefact file, starting at `001`.

## Status

See [CHANGELOG](CHANGELOG.md) and [CONTRIBUTING](CONTRIBUTING.md). Evaluation fixtures and a reasoning-quality harness are future work.

## License

Original collection text is MIT. See [`LICENSE`](LICENSE).

OWASP ASVS 5.0.0 is licensed under CC BY-SA 4.0. Attribution, and the statement that this project is not affiliated with or endorsed by OWASP or any other author, are in [`NOTICE`](NOTICE).
