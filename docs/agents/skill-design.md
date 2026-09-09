# Skill design

Rules for writing this collection's agent-facing documents. Follow them when editing a skill under `skills/`, shared mapping under `skills/_shared/`, `AGENTS.md`, or `CLAUDE.md`.

## Progressive disclosure

`SKILL.md` is the always-loaded top: purpose, process, rules, output, completion criteria. Put method, schemas, and long reference behind pointers in the same skill folder. Shared ASVS applicability lives once in `skills/_shared/asvs-mapping.md`; skills point at it rather than inlining it.

A pointer names the target and the branches that should load it. Front-load the trigger word. One trigger per distinct branch.

## Evidence over speculation

State what the repo, spec, or diff actually shows. Mark uncertainty. Do not present an unsupported claim as a fact.

## One meaning, one place

Each instruction has a single source of truth. Do not repeat the same instruction in `SKILL.md` and a disclosed reference. Point, don't copy.

## ASVS versioning

Name a requirement as `v5.0.0-X.X.X`. The mapping answers when an area is relevant; it does not reproduce requirement bodies. Load only applicable areas.

## Licensing

Original collection text is MIT. ASVS 5.0.0 is CC BY-SA 4.0; attribute it and claim no OWASP (or Matt Pocock) endorsement. Do not paste ASVS requirement text into skills. Write original skill text for this collection.

## Human docs vs agent instructions

`AGENTS.md` is the canonical agent instruction source for developing this repository. `CLAUDE.md` only redirects there. Human-facing product, install, and integration docs live outside those files and are not a second copy of agent rules.
