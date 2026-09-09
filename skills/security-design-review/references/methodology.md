# Methodology

How to derive the security picture from evidence. Load this while establishing actors through abuse paths. The ordered process lives in `SKILL.md`; this file is the method for each element.

Work from the consumer repo, conversation, requirements, ADRs, and `CONTEXT.md`. Quote or paraphrase the source. When a source is silent, write `Uncertain:` and what would resolve it.

## Actors

Name who can initiate or be affected by the change: authenticated users, anonymous callers, admins, jobs, other services, operators. Split by privilege when the design actually distinguishes them. An actor without an evidence trail is a hypothesis: mark it uncertain or drop it.

## Attacker capabilities

For each actor, state what they already control at the trust boundary they occupy: their own credentials, their own records, request bodies, files they may upload, tokens they were issued, network vantage. Capabilities come from the design's entry points and privilege model, not from a generic attacker catalogue.

## Assets

Name what the change exists to protect or could expose: tenant data, secrets, session state, money-moving operations, admin functions, integrity of stored records. Tie each asset to a store, message, or operation the sources describe.

## Entry points

List interfaces the change adds or alters: HTTP routes, jobs, webhooks, sockets, file parsers, admin tools, identity-provider callbacks. An entry point is a place an actor can introduce input or trigger a sensitive operation.

## Data flows

Trace sensitive data from entry point to store, to other services, and back to a client. Note where representation changes (encoding, serialization, authorization context). Stop at the boundary the sources actually describe.

## Trust boundaries

A trust boundary is where the principal, network, or processing context changes: browser to API, tenant A to tenant B, app to identity provider, app to object storage, privileged job to user-facing API. Draw only boundaries the architecture or code layout supports.

## Privilege boundaries

A privilege boundary is who may perform which operation, including object-level and tenant-level access. Record the intended deny-by-default: unauthenticated vs authenticated, member vs admin, one tenant vs another. If authorization rules are unspecified, that gap is an assumption or a threat, not a silent default.

## Attack surface

The attack surface is the union of entry points, attacker-controlled inputs, and crossings of trust or privilege boundaries that this change creates or leaves reachable. Examine that union; skip unrelated surfaces the change does not touch.

## Abuse paths

A candidate is credible when an attacker with a stated capability can follow a path the design actually exposes to a named asset with a concrete impact.

Fill each candidate from evidence. Drop a candidate that needs a system the sources do not contain, or that has no reachable path from a real entry point.

## Assumptions

Write down every gap you treated as true in order to finish the review (missing authn scheme, unspecified tenancy, unknown admin channel). Assumptions are first-class output. They are not facts.
