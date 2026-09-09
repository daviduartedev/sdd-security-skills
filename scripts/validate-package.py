#!/usr/bin/env python3
"""Validate this collection's published package invariants."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
errors: list[str] = []


def fail(message: str) -> None:
    errors.append(message)


REQUIRED_MANIFEST_FIELDS = ("name", "description", "version", "license")
CLAUDE_PLUGIN = ".claude-plugin/plugin.json"
CURSOR_PLUGIN = ".cursor-plugin/plugin.json"
CLAUDE_ALLOWED_KEYS = frozenset(
    {
        "name",
        "description",
        "version",
        "author",
        "homepage",
        "repository",
        "license",
        "keywords",
    }
)
CURSOR_ALLOWED_KEYS = CLAUDE_ALLOWED_KEYS | frozenset({"displayName", "skills"})


def require_file(relative: str) -> Path | None:
    path = ROOT / relative
    if not path.is_file():
        fail(f"missing {relative}")
        return None
    return path


def load_json(relative: str) -> dict | None:
    path = require_file(relative)
    if path is None:
        return None
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        fail(f"{relative} is not valid JSON: {exc.msg}")
        return None
    if not isinstance(data, dict):
        fail(f"{relative} must be a JSON object")
        return None
    return data


def require_manifest_fields(relative: str, data: dict | None) -> None:
    if data is None:
        return
    for field in REQUIRED_MANIFEST_FIELDS:
        value = data.get(field)
        if not isinstance(value, str) or not value.strip():
            fail(f"{relative} missing required field {field}")


def require_gitignored(relative: str) -> None:
    result = subprocess.run(
        ["git", "check-ignore", "-q", "--", relative],
        cwd=ROOT,
    )
    if result.returncode != 0:
        fail(f"{relative} must be gitignored")


def require_untracked(*relatives: str) -> None:
    result = subprocess.run(
        ["git", "ls-files", "--", *relatives],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    for path in result.stdout.splitlines():
        if path:
            fail(f"{path} must not be tracked")


def require_allowed_keys(
    relative: str, data: dict | None, allowed: frozenset[str]
) -> None:
    if data is None:
        return
    extra = sorted(set(data) - allowed)
    if extra:
        fail(f"{relative} has non-observed fields: {', '.join(extra)}")


def forbid_path(relative: str) -> None:
    if (ROOT / relative).exists():
        fail(f"{relative} must not be present")


def main() -> int:
    require_file("LICENSE")
    claude = load_json(CLAUDE_PLUGIN)
    cursor = load_json(CURSOR_PLUGIN)
    require_manifest_fields(CLAUDE_PLUGIN, claude)
    require_manifest_fields(CURSOR_PLUGIN, cursor)
    require_allowed_keys(CLAUDE_PLUGIN, claude, CLAUDE_ALLOWED_KEYS)
    require_allowed_keys(CURSOR_PLUGIN, cursor, CURSOR_ALLOWED_KEYS)
    if cursor is not None:
        skills = cursor.get("skills")
        if skills != "./skills/":
            fail(f'{CURSOR_PLUGIN} must set "skills" to "./skills/"')
        if "hooks" in cursor:
            fail(f"{CURSOR_PLUGIN} must not declare hooks")
    require_file("skills/_shared/asvs-mapping.md")
    require_file("examples/nextjs-saas/README.md")
    require_gitignored(".agents/")
    require_gitignored("skills-lock.json")
    require_untracked(".agents", "skills-lock.json")
    forbid_path(".codex-plugin")
    forbid_path(".kimi-plugin")

    if errors:
        for message in errors:
            print(f"FAIL: {message}", file=sys.stderr)
        return 1
    print("OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
