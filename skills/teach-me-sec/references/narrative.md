# Narrative

How to write the explained companion. The ordered process lives in `SKILL.md`; this file is the method for the write.

## Banner

Open with a short banner: this file is an **explained companion**, derived from the AppSec source (`docs/security/<feature-slug>.md` and/or the `SR-*` conversation report). That AppSec artifact is the source of truth. This file adds no `THREAT-*`, `SEC-*`, or `SR-*`.

## Shape

Mirror the source's section order. Omit a section the source omitted. Keep working literacy: a term from the source may appear after a plain-language gloss in the same passage.

Use each `THREAT-*`, `SEC-*`, and `SR-*` from the source as a heading or in-line anchor so a reader can walk back to the AppSec file. Copy no new identifiers.

For each ASVS area the source recorded as applied or skipped, one plain sentence: what was in scope or why it was skipped. Name `v5.0.0-X.X.X` when the source did. Leave ASVS requirement bodies unquoted.

## Diagnosis

For each identifier, state what is going on, why it matters, and what goes wrong if it stays open. Point at the existing `SEC-*` or `SR-*`. Leave the implementation mechanism to the spec and the implementer.

## Two copies

The consumer file is en-UK. The conversation copy uses the teaching language from this run. Same sections and anchors; not a mandated line-by-line translation.

A later `teach-me-sec` run on the same slug replaces the explained companion. The AppSec file stays the file that skill already produced.
