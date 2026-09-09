# teach-me-sec

Human guide to the AppSec companion in this collection. Agent instructions live in `skills/teach-me-sec/`. This page is for the engineer who decides when to run it and what to do with the result.

## What it does

The skill restates an existing `security-design-review` or `security-review` in working literacy: enough for product or engineering readers who are not AppSec specialists to follow what is at risk and talk to whoever will fix it. It writes a derived **explained companion** beside the AppSec file and prints the same narrative in the conversation.

The AppSec artifact remains the source of truth. This skill copies no new `THREAT-*`, `SEC-*`, or `SR-*`, and it does not prescribe a patch.

## When to run it

When you want a non-specialist explanation of a review that already exists, or of one you are willing to have run first. The skill is model-invoked (the agent can notice that ask from its description). You can also invoke it by name. The AppSec pair can point here when you ask for an explanation; those reviews are still done without this companion.

Skip it when you are the AppSec reader of the original file, or when the work is a smoke check (`smoke-test-list`).

## Input

- Teaching language for the conversation: pt-BR, es, or en-UK (default **en-UK** if you do not choose)
- A source, in this order: a path you supply, an `SR-*` report already in the conversation, or `docs/security/*.md` for this change

You may supply a **feature slug**. If you do not, the agent uses the source file's slug, then the branch, feature, or spec title, and asks if none of those exist.

If no source exists, the agent names `security-design-review` or `security-review` from the SDD slot and waits for a yes before running it in the same session, then teaches from that output. Declining stops the run; no explained companion is written.

## Output

Two copies of the same narrative:

1. A markdown file in the consumer repo at `docs/security/<feature-slug>-explained.md` (created or replaced, always en-UK), including when the source is only an `SR-*` conversation report
2. The same sections and identifier anchors printed in the conversation, in the teaching language

The AppSec file (`docs/security/<feature-slug>.md`) is left as the AppSec skill produced it. A later `teach-me-sec` run on the same slug replaces only the explained companion.

## Example

`docs/security/list-invoices.md` already holds `THREAT-001` and `SEC-001` (tenant-scoped invoice list). After `teach-me-sec`, `docs/security/list-invoices-explained.md` might open:

```markdown
> Explained companion of `docs/security/list-invoices.md`. That AppSec file is the source of truth.

## Threats/Abuse Cases

### THREAT-001

A signed-in user of tenant A can put tenant B's id in the request and read B's invoices. The list endpoint trusts the id the caller sends instead of the tenant on the session.

## Security Requirements

### SEC-001

Every operation on tenant-owned records must check the authenticated tenant. Until that holds, THREAT-001 stays open.
```

The conversation copy uses the teaching language you chose; the file stays en-UK.

## Non-goals

- A fourth AppSec review, or new `THREAT-*` / `SEC-*` / `SR-*`
- Rewriting or replacing `docs/security/<feature-slug>.md`
- A security course, or teaching in the absence of a review you declined to run
- Implementation steps, diffs, or a patch plan
- Smoke checks (`smoke-test-list`)
- Reproducing OWASP ASVS requirement bodies
