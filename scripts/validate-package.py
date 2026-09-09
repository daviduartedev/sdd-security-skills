#!/usr/bin/env python3
"""Validate this collection's published package invariants."""

from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
errors: list[str] = []
FRONTMATTER = re.compile(r"\A---\r?\n(.*?)\r?\n---(?:\r?\n|$)", re.DOTALL)
MARKDOWN_LINK = re.compile(r"\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")


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


def require_nonempty_file(relative: str) -> Path | None:
    path = require_file(relative)
    if path is None:
        return None
    if not path.read_text(encoding="utf-8").strip():
        fail(f"{relative} is empty")
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


def parse_frontmatter_map(block: str) -> dict[str, str]:
    data: dict[str, str] = {}
    for line in block.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#") or ":" not in line:
            continue
        key, _, raw = line.partition(":")
        value = raw.strip()
        if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
            value = value[1:-1]
        data[key.strip()] = value
    return data


def relative_link_targets(text: str) -> list[str]:
    targets: list[str] = []
    seen: set[str] = set()
    for raw in MARKDOWN_LINK.findall(text):
        if raw.startswith(("#", "http://", "https://", "mailto:")):
            continue
        if raw in seen:
            continue
        seen.add(raw)
        targets.append(raw)
    return targets


def published_skill_names() -> list[str]:
    skills_root = ROOT / "skills"
    if not skills_root.is_dir():
        fail("missing skills/")
        return []
    names: list[str] = []
    for path in sorted(skills_root.iterdir()):
        if path.is_dir() and not path.name.startswith("_") and not path.name.startswith("."):
            names.append(path.name)
    return names


def validate_published_skill(skill_name: str) -> None:
    relative = f"skills/{skill_name}/SKILL.md"
    path = require_file(relative)
    if path is None:
        return
    text = path.read_text(encoding="utf-8")
    match = FRONTMATTER.match(text)
    if match is None:
        fail(f"{relative} missing YAML frontmatter")
        return
    meta = parse_frontmatter_map(match.group(1))
    name = meta.get("name", "")
    if name != skill_name:
        fail(f"{relative} frontmatter name {name!r} must equal {skill_name!r}")
    description = meta.get("description", "").strip()
    if not description:
        fail(f"{relative} missing frontmatter description")
    if description.lower().count("use when") != 1:
        fail(f"{relative} description must contain exactly one 'Use when'")
    if "V1 Encoding and Sanitization; V2 Validation" in text:
        fail(f"{relative} must not inline the ASVS area roster")
    skill_dir = path.parent
    root = ROOT.resolve()
    for target in relative_link_targets(text):
        resolved = (skill_dir / target).resolve()
        try:
            resolved.relative_to(root)
        except ValueError:
            fail(f"{relative} link escapes package: {target}")
            continue
        if not resolved.is_file():
            fail(f"{relative} missing linked file {target}")


def main() -> int:
    require_file("LICENSE")
    require_nonempty_file("README.md")
    require_nonempty_file("CHANGELOG.md")
    require_nonempty_file("CONTRIBUTING.md")
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
    expected = (
        "security-design-review",
        "security-review",
        "smoke-test-list",
    )
    published = published_skill_names()
    for name in expected:
        if name not in published:
            fail(f"missing published skill {name}")
    for name in published:
        validate_published_skill(name)
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
