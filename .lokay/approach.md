# Approach plan

<!-- lokay-approach source=deterministic repo=mikolaj92/hermetic-alchemy issue=11 -->

Repository: `mikolaj92/hermetic-alchemy`  
Issue: #11 — Quick Start z skills.sh: skillu nie ma w rejestrze

## Goal

Make the documented skills.sh Quick Start install a real, discoverable skill.

`npx skills add mikolaj92/hermetic-alchemy` must find `skills/hermetic-alchemy` (valid `SKILL.md` frontmatter with `name` + `description`). README Method 1 should use that command, not the non-working `hermes skills install`.

## Files likely touched

- `skills/hermetic-alchemy/SKILL.md` — quote/sanitize YAML frontmatter (`**...**` was parsed as an alias)
- `skills/hermetic-alchemy/skill.yaml` — keep version in sync
- `README.md` — document `npx skills add mikolaj92/hermetic-alchemy -a hermes-agent -g`
- `CHANGELOG.md` / `CONTRIBUTING.md` — record the parse requirement

## Test plan

- Parse `SKILL.md` frontmatter with PyYAML
- `npx skills add . --list` must report `hermetic-alchemy`

## Non-goals

- Cannot mint the live `https://www.skills.sh/mikolaj92/hermetic-alchemy` page from this PR; skills.sh indexes after a successful `npx skills add` of a valid skill.
- Do not invent a custom registry or copy `www.skills.sh` into the repo.

## Notes

- Root cause confirmed: `npx skills add mikolaj92/hermetic-alchemy --list` cloned the repo, then skipped the skill (`YAML parse error` / `No valid skills found`).
- Trust intentional issue; this plan is evidence for later review, not a human gate.
