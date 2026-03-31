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

## 📋 Setup

To set up a new auto-research run, work with the user to:

### 1. Agree on a run tag

Propose a tag based on today's date (e.g., `mar31`). The branch `autoresearch/<tag>` must not already exist.

### 2. Create the branch

```bash
git checkout -b autoresearch/<tag>
```

### 3. Read the in-scope files

Read these files for full context:
- `README.md` — repository context
- `skills/hermetic-alchemy/SKILL.md` — **the file you modify**. Agent descriptions, workflow, execution protocol.
- `examples/rest-api.md` — example of successful execution
- `CHANGELOG.md` — version history

### 4. Verify test environment

Check that:
- Hermes Agent 0.6.0+ is installed
- The skill is loaded: `hermes skills list | grep hermetic`
- You can spawn subagents with `delegate_task()`

### 5. Initialize results.tsv

Create `results.tsv` with the header row:
```tsv
commit	success_rate	time_min	status	description
```

The baseline will be recorded after the first run.

### 6. Confirm and go

Confirm setup looks good, then kick off experimentation.

---

## 🧪 Experimentation

Each experiment runs on a **real software task** with a **20-minute time budget**.

**What you CAN do:**
- Modify `skills/hermetic-alchemy/SKILL.md` — this is the only file you edit
- Change agent descriptions, goals, workflows
- Add/remove/rename agents
- Modify feedback loops
- Change the execution protocol
- Adjust timeouts and turn limits

**What you CANNOT do:**
- Modify Hermes Agent itself (it's the "prepare.py" equivalent)
- Install new packages or dependencies
- Modify other files (keep focus on SKILL.md)

**The goal is simple: get the highest task_success_rate.**

### What is task_success_rate?

The percentage of test tasks that complete successfully:
- **100%** = All test tasks pass (perfect)
- **0%** = All tasks crash (broken)
- **Higher is better**

### Test Tasks

Each experiment runs **3 test tasks**:

1. **Simple REST API**
   ```
   /transmute build a simple REST API for todo management with 5 endpoints
   ```
   Expected time: 15-20 minutes
   Success criteria: API runs, tests pass, documentation exists

2. **Database-Heavy App**
   ```
   /transmute create a blog platform with PostgreSQL database and user authentication
   ```
   Expected time: 20-25 minutes
   Success criteria: DB schema created, migrations work, auth implemented

3. **Frontend + Backend**
   ```
   /transmute build a full-stack app with React frontend and FastAPI backend for a task manager
   ```
   Expected time: 25-30 minutes
   Success criteria: Frontend and backend connect, app works

### Time Budget

Each test task has a **20-minute execution budget** (wall clock time for agent work, excluding startup).

If a task exceeds 25 minutes total, kill it and treat as failure.

---

## 📊 Running an Experiment

### Step 1: Modify SKILL.md

Make an experimental change to the skill:
```python
# Example: Add a new agent
# Add agent to "The 10 Hermetic Agents" section
# Update workflow diagram
# Modify execution protocol
```

### Step 2: Git commit

```bash
git add skills/hermetic-alchemy/SKILL.md
git commit -m "experiment: [short description]"
```

### Step 3: Run test tasks

For each test task:

```bash
# Create test workspace
mkdir -p /tmp/hermetic-test-1
cd /tmp/hermetic-test-1

# Run task (capture output)
hermes chat << 'EOF' > test-output.log 2>&1
/transmute build a simple REST API for todo management with 5 endpoints
EOF

# Check results
grep -i "MAGNUM OPUS COMPLETE" test-output.log
echo $?  # 0 = success, 1 = failure
```

### Step 4: Calculate success_rate

```
success_rate = (successful_tasks / total_tasks) * 100
```

Example:
- Task 1: ✅ Success
- Task 2: ❌ Failure
- Task 3: ✅ Success
- **success_rate = 66.7%**

---

## 📝 Logging Results

When an experiment is done, log it to `results.tsv` (tab-separated):

```tsv
commit	success_rate	time_min	status	description
```

**Columns:**
1. **commit** — git commit hash (short, 7 chars)
2. **success_rate** — percentage (e.g., 66.7, 100.0, 0.0)
3. **time_min** — average task time in minutes (e.g., 18.5, 22.3)
4. **status** — `keep`, `discard`, or `crash`
5. **description** — short text description

**Example:**

```tsv
commit	success_rate	time_min	status	description
a1b2c3d	66.7	18.5	keep	baseline - 3 agents succeed
b2c3d4e	100.0	19.2	keep	add timeout monitoring to Nigredo
c3d4e5f	33.3	22.1	discard	remove Sulfur quality checks (breaks things)
d4e5f6g	0.0	0.0	crash	double agent turns (OOM)
```

---

## 🔄 The Experiment Loop

The experiment runs on a dedicated branch (e.g., `autoresearch/mar31`).

```
LOOP FOREVER:

1. Look at git state: current branch/commit
2. Modify SKILL.md with experimental idea
3. git commit
4. Run 3 test tasks (20 min each)
5. Calculate success_rate
6. Log results to results.tsv (don't commit it)
7. If success_rate improved → keep commit (advance branch)
8. If success_rate worse → git reset (revert change)

REPEAT UNTIL INTERRUPTED
```

### Decision Rules

**Keep (advance branch) if:**
- success_rate improved by ≥ 5%
- OR success_rate same but time improved by ≥ 10%
- OR same metrics but significantly simpler code

**Discard (reset branch) if:**
- success_rate worse by ≥ 5%
- OR same success_rate but slower by ≥ 10%
- OR adds complexity without benefit

**Crash if:**
- Task crashes (OOM, bug, etc.)
- Log as crash, reset, and skip if unrecoverable

### Simplicity Criterion

**All else being equal, simpler is better.**

A 5% improvement that adds 50 lines of complex code? Maybe not worth it.
A 5% improvement from **deleting** code? Definitely keep.
Same performance but simpler? Keep.

---

## ⏱️ Timeouts

- **Per task**: 20 minutes (agent work)
- **Total per experiment**: ~60 minutes (3 tasks)
- **Hard kill**: If exceeds 70 minutes, treat as crash

---

## 💥 Crashes

If a task crashes:
1. Read the error log: `tail -n 50 test-output.log`
2. Attempt fix if it's simple (typo, missing import)
3. If unrecoverable after 2-3 attempts, log as crash and move on

---

## 🚫 NEVER STOP

**Once the experiment loop begins, do NOT pause.**

Do NOT ask:
- "Should I keep going?"
- "Is this a good stopping point?"
- "What do you think?"

**You are autonomous.**

If you run out of ideas:
- Re-read SKILL.md for new angles
- Try combining previous near-misses
- Try more radical architectural changes
- Read the examples for patterns
- Experiment with agent personalities

**The loop runs until manually stopped.**

### Example Use Case

User leaves you running while sleeping:
- 60 minutes per experiment
- 8 experiments per 8-hour sleep
- Wake up to 8 completed experiments
- Skill has improved overnight!

---

## 🎯 Success Metrics

Track these over time:
- **success_rate** — primary metric (higher is better)
- **time_min** — average task time (lower is better)
- **complexity** — lines in SKILL.md (lower is better)

**Goal:** Maximize success_rate while minimizing time and complexity.

---

## 📈 Experimental Ideas to Try

When out of ideas, consider:

1. **Agent tuning**
   - Adjust agent timeouts
   - Change max_turns per agent
   - Modify agent goals/personality

2. **Workflow changes**
   - Reorder phases
   - Add/remove phases
   - Parallelize more

3. **Feedback loop improvements**
   - Adjust fix_loop iteration limits
   - Add quality thresholds
   - Experiment with alternative strategies

4. **Quality gate tuning**
   - Add new checks (e.g., code style)
   - Adjust pass_score thresholds
   - Modify Sulfur's audit scope

5. **Communication improvements**
   - Better context passing between agents
   - Improve error messages
   - Add progress reporting

6. **Simplification**
   - Remove redundant steps
   - Consolidate agents
   - Streamline workflow

---

## 🧠 Remember: You're Improving the Improvement Process

This is meta: **agents improving agents**.

The goal is not just to improve the skill, but to improve **how the skill improves itself**.

Each experiment teaches you what works and what doesn't. Learn from failures.

---

**ALL HAIL HERMES TRISMEGISTUS! ⚗️✨**

*"From chaos, through fire, gold emerges. And from gold, through fire, emerges purer gold."*
