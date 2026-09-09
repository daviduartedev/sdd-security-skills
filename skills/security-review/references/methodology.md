# Methodology

How to pin a **fixed point**, keep reading scoped, validate candidates, grade evidence, and check `SEC-*`. The ordered process lives in `SKILL.md`; this file is the method for those elements.

## Fixed point

The range is the user-stated implementation, or the inferred current working-tree diff, branch comparison, or pull-request diff.

Resolve the ref before reading code. An unresolvable ref is an empty scope: stop and ask. A resolved comparison with no changed files or hunks is also empty: stop, and leave unrelated directories unread.

Prefer the smallest range that still covers the completed work. Name the command or source you used (three-dot branch diff, `gh pr diff`, staged plus unstaged working tree) in the report so a later session can replay it.

## Scoped reading

Start from files and hunks inside the range. Open a caller, callee, middleware, policy, or schema outside the hunk only when a trust or privilege boundary cannot be understood from the change itself.

Record why that extra file was opened. Close the extra read once the boundary is clear. The rest of the repository is out of scope.

## Candidate validation

Fill every slot from the range before treating a candidate as a finding:

- **Attacker**: which actor, at which privilege, already sits on which side of a trust boundary.
- **Control**: the check, encoding, binding, or isolation that is missing, bypassed, or applied to the wrong object.
- **Preconditions**: what must already be true (authenticated member, knowledge of an id, reachable route).
- **Vulnerable path**: the concrete steps through this change's entry points.
- **Asset**: the data, operation, or integrity property at risk.
- **Exploit**: how the attacker actually causes the control to fail in this code.
- **Impact**: what becomes possible against the asset.
- **Code evidence**: a citation inside the range (and any extra boundary file you had to open).

A slot filled only by a generic class name (injection, IDOR, XSS) is empty. Keep filling from this change or drop the candidate.

## Evidence

Grade each observation:

- **Verified**: read in the range (or in the extra boundary file you opened).
- **Inference**: a conclusion that follows from verified facts and the visible control flow.
- **Uncertain**: a gap (missing authn scheme, unseen gateway, unshown store). Write `Uncertain:` and what would resolve it.

Present Verified, Inference, and Uncertain as distinct labels. An unsupported claim is not a fact.

## False-positive rejection

Drop a candidate when any validation slot stays empty, when the path needs a component this range does not contain, when a control in the range already blocks the path, or when the only impact is maintainability or style.

Theoretical chains that skip a holding control are rejected, not downgraded.

## Checking SEC requirements

Search order and write-back live in `SKILL.md`. This section is how to judge and record a result.

A consumer file is tied to this change when the user named it, when the originating spec or conversation points at it, or when its feature slug matches the branch, pull request, or spec title of the range. Do not walk unrelated historical reviews.

For each located `SEC-*`, decide from the range:

- **PASS**: the invariant holds on the reachable paths this change introduces or leaves open. Cite the enforcement.
- **FAIL**: a reachable path violates the invariant. Cite the missing or bypassed control.

Write Status and Evidence on that same requirement in the artifact. Then append a **Verification** section that names the fixed point, each `SEC-*` result, and a one-line summary of each published `SR-*`.

When the search finds no `SEC-*`, say so in the conversation. Leave PASS/FAIL and Verification unwritten. The diff review still runs.
