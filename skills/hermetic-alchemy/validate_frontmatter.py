#!/usr/bin/env python3
"""Fail if SKILL.md frontmatter is not valid YAML with name + description.

The skills.sh CLI (`npx skills add`) skips skills whose frontmatter cannot be
parsed. Unquoted markdown like `**bold**` is one known breaker.
"""

from __future__ import annotations

from pathlib import Path
import sys

try:
    import yaml
except ImportError:  # pragma: no cover - stdlib fallback is enough for CI-less repos
    yaml = None


ROOT = Path(__file__).resolve().parent
SKILL_MD = ROOT / "SKILL.md"
MANIFEST = ROOT / "skill.yaml"


def load_frontmatter(text: str) -> dict:
    if not text.startswith("---\n"):
        raise SystemExit("SKILL.md must start with YAML frontmatter (---)")
    end = text.find("\n---\n", 3)
    if end == -1:
        raise SystemExit("SKILL.md is missing a closing frontmatter fence")
    body = text[4:end]
    if yaml is None:
        data: dict = {}
        for line in body.splitlines():
            if not line or line.startswith(" ") or line.startswith("\t") or ":" not in line:
                continue
            key, value = line.split(":", 1)
            data[key.strip()] = value.strip().strip('"').strip("'")
        return data
    try:
        data = yaml.safe_load(body)
    except yaml.YAMLError as exc:
        raise SystemExit(f"SKILL.md frontmatter is invalid YAML: {exc}") from exc
    if not isinstance(data, dict):
        raise SystemExit("SKILL.md frontmatter must be a mapping")
    return data


def main() -> int:
    skill = load_frontmatter(SKILL_MD.read_text(encoding="utf-8"))
    for key in ("name", "description"):
        value = skill.get(key)
        if not isinstance(value, str) or not value.strip():
            raise SystemExit(f"SKILL.md frontmatter is missing a string {key}")
    if skill["name"] != "hermetic-alchemy":
        raise SystemExit(f"unexpected skill name: {skill['name']}")
    if yaml is not None:
        manifest = yaml.safe_load(MANIFEST.read_text(encoding="utf-8"))
        if manifest.get("name") != skill["name"]:
            raise SystemExit("skill.yaml name does not match SKILL.md")
        if manifest.get("version") != skill.get("version"):
            raise SystemExit("skill.yaml version does not match SKILL.md")
    print(f"ok: {skill['name']} {skill.get('version', '')}".rstrip())
    return 0


if __name__ == "__main__":
    sys.exit(main())
