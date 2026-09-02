import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VALIDATOR = ROOT / "skills/hermetic-alchemy/validate_frontmatter.py"


def run_validator(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run([sys.executable, str(VALIDATOR), *args], text=True, capture_output=True, check=False)


def test_public_skill_contract_is_consistent() -> None:
    result = run_validator()
    assert result.returncode == 0, result.stderr
    assert "hermetic-alchemy 1.0.2" in result.stdout


def test_invalid_unquoted_markdown_alias_fails_closed(tmp_path: Path) -> None:
    skill = tmp_path / "SKILL.md"
    manifest = tmp_path / "skill.yaml"
    skill.write_text("---\nname: hermetic-alchemy\ndescription: **broken**\nversion: 1.0.2\n---\n")
    manifest.write_text("name: hermetic-alchemy\ndescription: broken\nversion: 1.0.2\n")
    result = run_validator("--skill", str(skill), "--manifest", str(manifest))
    assert result.returncode != 0
    assert "invalid YAML" in result.stderr


def test_manifest_version_mismatch_fails(tmp_path: Path) -> None:
    skill = tmp_path / "SKILL.md"
    manifest = tmp_path / "skill.yaml"
    skill.write_text('---\nname: hermetic-alchemy\ndescription: "valid"\nversion: 1.0.2\n---\n')
    manifest.write_text('name: hermetic-alchemy\ndescription: "valid"\nversion: 9.9.9\n')
    result = run_validator("--skill", str(skill), "--manifest", str(manifest))
    assert result.returncode != 0
    assert "version does not match" in result.stderr


def test_agent_roster_and_turn_limits_have_one_truth() -> None:
    import re

    import yaml

    text = (ROOT / "skills/hermetic-alchemy/SKILL.md").read_text()
    headers = {
        name.lower(): int(turns)
        for name, turns in re.findall(
            r"^### [^\n]*?([A-Z]+) - [^\n]+[\s\S]*?\*\*Max turns:\*\* (\d+)",
            text,
            re.MULTILINE,
        )
        if name != "HERMES"
    }
    config_text = text.split("# Agent configurations", 1)[1].split("# Memory", 1)[0]
    config = yaml.safe_load(config_text.replace("```yaml", "").replace("```", ""))["agents"]
    assert set(headers) == {"nigredo", "citrinitas", "mercurius", "sol", "sal", "albedo", "sulfur", "rubedo"}
    assert {name: details["max_turns"] for name, details in config.items()} == headers
    assert "this role is not delegated as a child" in text
    assert "AETHER" not in text


def test_public_docs_contain_no_unsourced_results_or_dead_surfaces() -> None:
    tracked = [ROOT / "README.md", ROOT / "CONTRIBUTING.md", *sorted((ROOT / "examples").glob("*.md"))]
    text = "\n".join(path.read_text() for path in tracked)
    for stale in ("156 tests", "234 tests", "94/100", "53.1 minutes", "GitHub Discussions", "workflows/", "Ensure CI passes"):
        assert stale not in text
