---
name: teach-me-sec
description: "Use when the human wants a non-specialist explanation of a security-design-review or security-review."
---

# teach-me-sec

Working-literacy companion of a **security-design-review** or **security-review**. Restate that review so product or engineering readers who are not AppSec specialists can follow what is at risk. The AppSec artifact stays the source of truth.

## Process

1. Ask the teaching language for this conversation: pt-BR, es, or en-UK. Use **en-UK** when the human does not choose.

2. Resolve the source in this order: (1) an explicit path the user supplied, (2) an `SR-*` report or review already in this conversation, (3) consumer `docs/security/*.md` tied to this change. No source: load [dispatch](references/dispatch.md).

3. Resolve the feature slug: the value the user supplied; otherwise the source file's slug; otherwise the branch, feature, or spec title; otherwise ask before writing.

4. Write or replace `docs/security/<feature-slug>-explained.md` in the consumer repository (en-UK) and print the same narrative in the conversation in the teaching language. Load [narrative](references/narrative.md) for the banner, section order, identifier anchors, ASVS lines, and diagnosis-only wording. Among consumer security files, write only that explained companion.

## Output

Path in the consumer repo: `docs/security/<feature-slug>-explained.md` (en-UK), including when the source is only an `SR-*` conversation report.

Conversation: the same narrative in the teaching language.

## Completion criteria

The run is done when all of the following hold:

- Teaching language asked; en-UK used when the human did not choose
- Source in hand: an existing artifact or `SR-*` report, or an AppSec skill dispatched in this session completed and produced output
- `docs/security/<feature-slug>-explained.md` written or replaced in en-UK; among consumer security files, only that path written
- The same narrative printed in the conversation in the teaching language
- Every `THREAT-*`, `SEC-*`, and `SR-*` on the source appears as an anchor; every identifier in the companion exists on the source
- Each risk points at an existing `SEC-*` or `SR-*`; the companion is diagnosis
- Banner states that the AppSec artifact is the source of truth
- When the human declined dispatch: the run stopped; no explained companion written
