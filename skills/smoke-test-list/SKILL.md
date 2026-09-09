---
name: smoke-test-list
description: "Use when a completed implementation needs a local run and a human-observable smoke checklist before commits."
---

# smoke-test-list

After a completed implementation, start the app on a **free port** when a local UI exists, and print an **unchecked** checklist of what a human can see or do. Stop before commits. Wait for the human.

## Process

1. Establish the implementation branch: the branch the user named; otherwise a `feat/<slug>` recorded in cycle `request.md`; otherwise the current branch when it already holds that work. Stop if the working tree is on a different piece of work.

2. Resolve how to run the app, in this order: the command and URL the user supplied; cycle `request.md` then the smoke section of `plan.md`; the consumer's documented dev script. Load [local run](references/local-run.md) for free-port, reuse, and credential rules. If those sources show no local UI, skip the start and say so.

3. Start on a free port. Print the URL. Wait until the process is ready (a ready log, or a successful fetch). Leave a healthy server on this branch running.

4. Build one unchecked checklist of observable checks. Sources in that order: `request.md` (locked copy, roles, what is out of scope), `plan.md` smoke section, observable scenarios, then user-visible tasks. Include one relevant negative check. Named login profiles only when those sources state them; ask if a role is required and none is recorded.

5. Print the block in the conversation. One line after it: the human works the list, then confirms before any commit.

## Output

Primary: the conversation checklist (title, URL, login profiles when documented, path through the UI, unchecked items).

This run does not commit, open a pull request, or write a validation file.

## Completion criteria

The run is done when all of the following hold:

- Implementation branch established, or the run stopped because the working tree was other work
- Local URL printed, or the run states there is no local UI to start
- Every checklist item is something a human can see or do; none is ticked
- Documented login profiles included when the sources named them; otherwise none invented
- Conversation states that commits wait for the human
