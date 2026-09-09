<p>
  <img alt="AI Skills by World's Okayest Software Developer" src="docs/assets/readme-banner.png" width="720">
</p>

# World's Okayest Software Developer

[![skills.sh](https://skills.sh/b/daviduartedev/skills)](https://skills.sh/daviduartedev/skills)

Three agent skills I actually run. Small, composable, and meant to sit in a spec-driven loop rather than replace it. They work with any model. Fork them. Make them yours.

This collection is not an orchestrator, scanner, or custom SDD framework. It is not affiliated with OWASP or with Matt Pocock.

## The skills

Three skills, two categories. Agent process lives in `skills/<name>/SKILL.md`. This README does not repeat it.

### Security

Work that asks how a change can be abused, then checks the finished code against that.

- **[security-design-review](./skills/security-design-review/SKILL.md)** — Run **before the spec** is finalised. The agent grounds in the consumer repo, keeps only credible abuse paths (`THREAT-*`), and writes implementation-independent `SEC-*` invariants to `docs/security/<feature-slug>.md`. [Human guide](docs/engineering/security-design-review.md)
- **[security-review](./skills/security-review/SKILL.md)** — Run **after implement**, against a **fixed point** (diff, branch, PR, or named scope). Publishes evidenced `SR-*` findings in the conversation. When `SEC-*` exist, records PASS or FAIL on that same file. [Human guide](docs/engineering/security-review.md)

They are a pair: design review produces requirements; implementation review checks the diff and those requirements. OWASP ASVS 5.0.0 is applied **by relevance** (`v5.0.0-X.X.X`); requirement bodies are not copied.

### Delivery

Work that puts the change in front of a human before it is treated as done.

- **[smoke-test-list](./skills/smoke-test-list/SKILL.md)** — Run **after implement**, before commits. Starts the implementation branch locally on a **free port** when a UI exists, prints an unchecked checklist of what you can see or do (including a relevant negative check), and waits. Login profiles come from your docs or from you — never invented. This run does not commit. [Human guide](docs/engineering/smoke-test-list.md)

Everything in this collection is **model-invoked**: you can type the name, or the agent can reach for it when the slot matches.

## Installation

Two ways in. **The plugin manifests in this repo** install the set as a bundle. **[skills.sh](https://skills.sh/daviduartedev/skills)** copies editable skill files into your project. Pick one: installing both leaves you with every skill twice.

**Claude Code**

The plugin lives in [`.claude-plugin/plugin.json`](.claude-plugin/plugin.json). From a clone, add this repository as a plugin; the plugin discovers `skills/`.

**Codex, Cursor, and other agents**

```bash
npx skills add daviduartedev/skills --all
```

`npx skills add daviduartedev/skills` also works; `--all` installs all three skills without picking them one by one.

**For tinkerers**

Use the same installer. It writes the skills into your repo as ordinary files you own. Pull later changes with `npx skills update`.

Layout: `skills/<name>/SKILL.md`.

- **Claude Code:** `.claude-plugin/plugin.json`
- **Cursor:** `.cursor-plugin/plugin.json` with `"skills": "./skills/"`

## Status

See [CHANGELOG](CHANGELOG.md) and [CONTRIBUTING](CONTRIBUTING.md).

## License

Original collection text is MIT. See [`LICENSE`](LICENSE).

OWASP ASVS 5.0.0 is licensed under CC BY-SA 4.0. Attribution, and the statement that this project is not affiliated with or endorsed by OWASP or any other author, are in [`NOTICE`](NOTICE).
