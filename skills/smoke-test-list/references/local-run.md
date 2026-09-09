# Local run

Load when starting (or skipping) the consumer app for a smoke checklist.

## Start command and URL

Use the first source that actually states a command or URL:

1. The user, in this conversation
2. Cycle `request.md` (URL, port, how to start)
3. The smoke section of `plan.md`
4. The consumer's documented dev script (`package.json` `scripts`, Makefile, README)

Record uncertainty when the command is inferred. Ask when none of those sources exist.

## Free port

Bind a port that is free on this machine. If the documented port already serves **this** implementation branch, reuse that server and print its URL. If that port is taken by something else, start on another free port and print the new URL.

Leave a healthy server on the right branch running. Stop a stale process on the intended port only when it is this app on the wrong code (old build, `EADDRINUSE` from a dead watcher).

## Credentials

Print login profiles only when `request.md` or the user stated them. Ask when a role is required and no profile is recorded. Never invent a password or a default user.
