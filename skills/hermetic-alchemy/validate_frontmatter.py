#!/usr/bin/env python3
"""Validate the complete public skill manifest contract."""

from __future__ import annotations

import argparse
import ast
import re
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


def validate_agents(body: str) -> None:
    cards = re.findall(
        r"^### [^\n]*?([A-Z]+) - [^\n]+(?:(?!^### ).)*?\*\*Max turns:\*\* (\d+)",
        body,
        re.MULTILINE | re.DOTALL,
    )
    limits = {}
    for name, turns in cards:
        if name in limits:
            raise SystemExit(f"SKILL.md duplicate agent card: {name}")
        limits[name] = int(turns)
    configurations = []
    for block in re.findall(r"^```yaml\n(.*?)^```", body, re.MULTILINE | re.DOTALL):
        try:
            configuration = yaml.safe_load(block)
        except yaml.YAMLError as exc:
            raise SystemExit(f"SKILL.md configuration is invalid YAML: {exc}") from exc
        if isinstance(configuration, dict) and "agents" in configuration:
            configurations.append(configuration["agents"])
    if len(configurations) != 1 or not isinstance(configurations[0], dict):
        raise SystemExit("SKILL.md must contain exactly one agents configuration")
    configured = configurations[0]
    if {name.lower() for name in limits} != set(configured):
        raise SystemExit("SKILL.md agents configuration does not match agent cards")
    for name, turns in limits.items():
        details = configured[name.lower()]
        if (
            not isinstance(details, dict)
            or type(details.get("max_turns")) is not int
            or details["max_turns"] != turns
            or turns <= 0
        ):
            raise SystemExit(f"SKILL.md {name} max_turns does not match agent card")
    delegated = set()
    helpers = {
        "Generate 3 alternative architectural approaches",
        "Implement approach \0",
        "Score each experiment on correctness, performance, maintainability",
        "Merge winning approach: \0",
    }
    for block in re.findall(r"^```python\n(.*?)^```", body, re.MULTILINE | re.DOTALL):
        try:
            tree = ast.parse(block)
        except SyntaxError as exc:
            raise SystemExit(f"SKILL.md protocol syntax is invalid: {exc}") from exc
        for call in ast.walk(tree):
            if not isinstance(call, ast.Call) or not isinstance(call.func, ast.Name):
                continue
            if call.func.id != "delegate_task":
                continue
            if call.args or any(keyword.arg is None for keyword in call.keywords):
                raise SystemExit("SKILL.md delegation has ambiguous arguments")
            fields = {}
            for keyword in call.keywords:
                if keyword.arg in fields:
                    raise SystemExit(f"SKILL.md delegation has duplicate {keyword.arg}")
                fields[keyword.arg] = keyword.value
            tasks = [fields]
            if "tasks" in fields:
                if "goal" in fields or "max_iterations" in fields:
                    raise SystemExit("SKILL.md parallel delegation has ambiguous limits")
                entries = fields["tasks"]
                if isinstance(entries, ast.ListComp):
                    entries = [entries.elt]
                elif isinstance(entries, ast.List):
                    entries = entries.elts
                else:
                    raise SystemExit("SKILL.md parallel tasks must be a static list")
                tasks = []
                for entry in entries:
                    if not isinstance(entry, ast.Dict):
                        raise SystemExit("SKILL.md parallel task must be a mapping")
                    task = {}
                    for key, value in zip(entry.keys, entry.values):
                        if not isinstance(key, ast.Constant) or not isinstance(key.value, str):
                            raise SystemExit("SKILL.md parallel task has ambiguous fields")
                        if key.value in task:
                            raise SystemExit(f"SKILL.md parallel task has duplicate {key.value}")
                        task[key.value] = value
                    tasks.append(task)
            for task in tasks:
                goal = task.get("goal")
                if isinstance(goal, ast.Constant) and isinstance(goal.value, str):
                    text = goal.value
                elif isinstance(goal, ast.JoinedStr):
                    text = "".join(
                        part.value if isinstance(part, ast.Constant) else "\0"
                        for part in goal.values
                    )
                else:
                    raise SystemExit("SKILL.md delegation goal must identify a static agent")
                names = re.findall(r"\bYou are\s+(\S+)", text)
                if not names and text in helpers:
                    continue
                if len(names) != 1:
                    raise SystemExit("SKILL.md delegation must identify exactly one agent")
                name = names[0]
                if name not in limits:
                    raise SystemExit(f"SKILL.md delegation has unknown agent: {name}")
                budget = task.get("max_iterations")
                if (
                    not isinstance(budget, ast.Constant)
                    or type(budget.value) is not int
                    or budget.value != limits[name]
                ):
                    raise SystemExit(
                        f"SKILL.md {name} delegation max_iterations must equal {limits[name]}"
                    )
                delegated.add(name)
    if delegated != set(limits):
        raise SystemExit(f"SKILL.md agents missing delegations: {sorted(set(limits) - delegated)}")


def validate_verdict_paths(documents: dict[str, str]) -> None:
    expected = ".hermetic-lab/athanor/sulfur-check.json"
    for name, contents in documents.items():
        directories = []
        paths = []
        tree_paths = []
        for line in contents.splitlines():
            if line.strip() == ".hermetic-lab/":
                directories = [".hermetic-lab"]
            entry = re.match(r"^([ │]*)(?:├── |└── )(\S+)", line)
            if entry:
                depth = len(entry[1]) // 4
                directories = directories[:depth + 1]
                if entry[2].endswith("/"):
                    directories.append(entry[2].rstrip("/"))
                elif entry[2] == "sulfur-check.json":
                    path = "/".join([*directories, entry[2]])
                    paths.append(path)
                    tree_paths.append(path)
            else:
                paths.extend(re.findall(r"[\w./-]*sulfur-check\.json", line))
        if (
            tree_paths != [expected]
            or len(paths) != contents.count("sulfur-check.json")
            or set(paths) != {expected}
        ):
            raise SystemExit(f"{name} Sulfur verdict paths must all be {expected}")


def validate(skill_path: Path, manifest_path: Path) -> None:
    skill = load_frontmatter(skill_path)
    manifest = load_mapping(manifest_path)
    for key in ("name", "description", "version"):
        value = skill.get(key)
        if not isinstance(value, str) or not value.strip():
            raise SystemExit(f"SKILL.md frontmatter is missing a string {key}")
        if manifest.get(key) != value:
            raise SystemExit(f"skill.yaml {key} does not match SKILL.md")
    body = skill_path.read_text(encoding="utf-8").split("\n---\n", 1)[1]
    footer_versions = re.findall(r"^[ \t]*\*\*Version:\*\*[ \t]*(.*)$", body, re.MULTILINE)
    if len(footer_versions) != 1:
        raise SystemExit("SKILL.md must contain exactly one **Version:** footer declaration")
    footer_version = footer_versions[0].strip()
    if footer_version != skill["version"]:
        raise SystemExit(
            f"SKILL.md footer version {footer_version!r} does not match "
            f"frontmatter version {skill['version']!r}"
        )
    validate_agents(body)
    validate_verdict_paths({
        "SKILL.md": skill_path.read_text(encoding="utf-8"),
        "README.md": (ROOT.parents[1] / "README.md").read_text(encoding="utf-8"),
    })
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
