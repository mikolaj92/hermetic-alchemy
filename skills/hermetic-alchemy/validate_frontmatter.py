#!/usr/bin/env python3
"""Validate the complete public skill manifest contract."""

from __future__ import annotations

import argparse
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent


def load_mapping(path: Path) -> dict[str, object]:
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
    except yaml.YAMLError as exc:
        raise SystemExit(f"{path.name} is invalid YAML: {exc}") from exc
    if not isinstance(data, dict):
        raise SystemExit(f"{path.name} must contain a YAML mapping")
    return data


def load_frontmatter(path: Path) -> dict[str, object]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise SystemExit("SKILL.md must start with YAML frontmatter (---)")
    end = text.find("\n---\n", 4)
    if end == -1:
        raise SystemExit("SKILL.md is missing a closing frontmatter fence")
    try:
        data = yaml.safe_load(text[4:end])
    except yaml.YAMLError as exc:
        raise SystemExit(f"{path.name} is invalid YAML: {exc}") from exc
    if not isinstance(data, dict):
        raise SystemExit(f"{path.name} frontmatter must contain a YAML mapping")
    return data


def validate(skill_path: Path, manifest_path: Path) -> None:
    skill = load_frontmatter(skill_path)
    manifest = load_mapping(manifest_path)
    for key in ("name", "description", "version"):
        value = skill.get(key)
        if not isinstance(value, str) or not value.strip():
            raise SystemExit(f"SKILL.md frontmatter is missing a string {key}")
        if manifest.get(key) != value:
            raise SystemExit(f"skill.yaml {key} does not match SKILL.md")
    if skill["name"] != "hermetic-alchemy":
        raise SystemExit(f"unexpected skill name: {skill['name']}")
    print(f"ok: {skill['name']} {skill['version']}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--skill", type=Path, default=ROOT / "SKILL.md")
    parser.add_argument("--manifest", type=Path, default=ROOT / "skill.yaml")
    args = parser.parse_args()
    validate(args.skill, args.manifest)


if __name__ == "__main__":
    main()
