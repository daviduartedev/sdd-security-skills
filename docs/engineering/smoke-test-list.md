# smoke-test-list

Human guide to the delivery skill in this collection. Agent instructions live in `skills/smoke-test-list/`. This page is for the engineer who decides when to run it and what to do with the result.

## What it does

The skill walks an agent through a **human** check of a completed implementation: start the app locally on a free port when a UI exists, then print an unchecked list of things you can see or do. It does not mark the work validated, and it does not commit.

## When to run it

After implement, before you treat the change as done. The agent can notice that slot from the skill description. You can also invoke it by name.

Skip it when there is nothing new to look at, or when you are still in design or AppSec review (`security-design-review`, `security-review`).

## Input

Whatever already exists for the change:

- The implementation branch
- Cycle docs when present (`request.md`, `plan.md` smoke, observable scenarios, user-visible tasks)
- How to start the app, if a local UI exists

Login profiles come from those sources or from you. The skill will not invent them.

## Output

One conversation block: title, local URL, documented logins, path through the UI, unchecked observable items, including a relevant negative check.

You work the list. When it holds, you ask for commits in a later message. That confirmation is yours; this skill never commits.

## Non-goals

- Implementation, AppSec review, or opening a pull request
- Tick-boxes filled in by the agent
- A second validation file beside your own process
- Hard-coded ports, packages, or demo passwords for a particular product
