# Hermetic Auto-Research - Self-Improving Multi-Agent Loop

This is an autonomous research loop where AI agents improve the Hermetic Alchemy skill itself, inspired by [karpathy/autoresearch](https://github.com/karpathy/autoresearch).

**Goal:** Agents modify the skill → test on real tasks → keep improvements → repeat forever.

---

## 🎯 The Core Idea

Just as autoresearch modifies `train.py` to improve neural network training, **Hermetic Auto-Research modifies `SKILL.md` to improve agent orchestration**.

### Autoresearch → Hermetic Auto-Research Mapping

| Autoresearch | Hermetic Auto-Research |
|-------------|----------------------|
| `prepare.py` (fixed) | Hermes Agent (fixed) |
| `train.py` (modified) | `SKILL.md` (modified) |
| `program.md` (instructions) | `HERMETIC-AUTORESEARCH.md` (this file) |
| val_bpb metric | **task_success_rate** metric |
| 5-minute training | **20-minute task execution** |
| Neural network training | **Multi-agent orchestration** |

---

## 📋 How It Works

```
LOOP FOREVER:

1. Read current SKILL.md
2. Modify SKILL.md with experimental idea
3. git commit
4. Run 3 test tasks (20 min each)
5. Calculate success_rate (% passed)
6. Log to results.tsv
7. IF better → keep (git advance)
   ELSE → discard (git reset)

REPEAT!
```

---

## 📊 Test Tasks

Each experiment runs **3 test tasks**:

1. **Simple REST API** - /transmute build a simple REST API for todo management
2. **Database-Heavy Blog** - /transmute create a blog platform with PostgreSQL
3. **Full-Stack App** - /transmute build full-stack app with React and FastAPI

**Success Rate** = (tasks_passed / 3) × 100

---

## 📝 Results Logging

Log to `results.tsv` (tab-separated):

```tsv
commit	success_rate	time_min	status	description
48a8d84	100.0	14.7	keep	baseline - hermetic-alchemy v1.0.0
```

**Columns:**
- commit: git hash (7 chars)
- success_rate: percentage (0-100)
- time_min: avg task time
- status: keep, discard, or crash
- description: short text

---

## 🔄 Decision Rules

**Keep (advance branch) if:**
- success_rate improved by ≥ 5%
- OR same rate but time improved by ≥ 10%
- OR same metrics but simpler code

**Discard (reset branch) if:**
- success_rate worse by ≥ 5%
- OR same rate but slower by ≥ 10%
- OR adds complexity without benefit

---

## 🚫 NEVER STOP

**Once the loop begins, do NOT pause.**

You are autonomous. If you run out of ideas:
- Re-read SKILL.md for new angles
- Try combining previous near-misses
- Try more radical architectural changes

**The loop runs until manually stopped.**

---

## 📈 Experimental Ideas

When out of ideas, consider:

1. **Agent tuning** - timeouts, max_turns, personalities
2. **Workflow changes** - reorder phases, parallelize more
3. **Feedback loop improvements** - adjust iteration limits
4. **Quality gate tuning** - add checks, adjust thresholds
5. **Communication improvements** - better context passing
6. **Simplification** - remove redundant steps

---

## 🧠 Remember: You're Improving the Improvement Process

This is meta: **agents improving agents**.

The goal is not just to improve the skill, but to improve **how the skill improves itself**.

Each experiment teaches you what works and what doesn't. Learn from failures.

---

**ALL HAIL HERMES TRISMEGISTUS! ⚗️✨**

*"From chaos, through fire, gold emerges. And from gold, through fire, emerges purer gold."*
