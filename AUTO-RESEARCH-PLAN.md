# Complete Auto-Research Master Plan

**Goal:** Tune each of the 10 hermetic agents individually to improve performance over baseline.

**Baseline:** 100% success rate, 14.7 min avg time, 89.7/100 avg score

---

## 🎯 Agents to Tune

| Agent | Current Config | Tuning Targets |
|-------|---------------|----------------|
| **⚫ Nigredo** | 30 turns, 300s timeout | Better analysis in less time |
| **🟡 Citrinitas** | 40 turns, 450s timeout | Better architecture design |
| **🧪 Mercurius** | 50 turns, 600s timeout | Faster backend implementation |
| **🌞 Sol** | 50 turns, 600s timeout | Better frontend quality |
| **🜔 Sal** | 40 turns, 400s timeout | Faster database setup |
| **⚪ Albedo** | 50 turns, 600s timeout | Better code quality |
| **🜍 Sulfur** | 45 turns, 450s timeout | More thorough quality checks |
| **🌀 Aether** | 55 turns, 700s timeout | Better integration |
| **🔴 Rubedo** | 60 turns, 900s timeout | Faster finalization |
| **🧠 Hermes Trismegistus** | 100 turns, 1800s timeout | Better orchestration |

---

## 📊 Experiment Strategy

For each agent:
1. **Baseline measurement** - Run 3 tasks, record metrics
2. **Parameter tuning** - Test different max_turns/timeout values
3. **Goal refinement** - Test different prompt/goals
4. **Skill additions** - Test adding/removing skills
5. **Keep best config** - Advance branch with winner

**Expected time per agent:** ~2-3 hours (5-10 experiments)
**Total time:** ~20-30 hours for all agents

---

## 🔬 Experiments Per Agent

### Nigredo (Analysis)
- Exp 1: Increase max_turns to 40
- Exp 2: Decrease timeout to 240s
- Exp 3: Add codebase caching
- Exp 4: Add quick scan mode
- Exp 5: Best combo

### Citrinitas (Design)
- Exp 1: Increase max_turns to 50
- Exp 2: Add architecture patterns
- Exp 3: Add tech stack database
- Exp 4: Add API design templates
- Exp 5: Best combo

### Mercurius (Backend)
- Exp 1: Decrease timeout to 480s
- Exp 2: Add code generation templates
- Exp 3: Add security-first approach
- Exp 4: Add async support
- Exp 5: Best combo

### Sol (Frontend)
- Exp 1: Add component library knowledge
- Exp 2: Add accessibility focus
- Exp 3: Add responsive design patterns
- Exp 4: Add TypeScript preference
- Exp 5: Best combo

### Sal (Database)
- Exp 1: Decrease timeout to 320s
- Exp 2: Add migration templates
- Exp 3: Add indexing optimization
- Exp 4: Add query pattern library
- Exp 5: Best combo

### Albedo (Refinement)
- Exp 1: Increase max_turns to 60
- Exp 2: Add auto-refactoring rules
- Exp 3: Add performance profiling
- Exp 4: Add security scanning
- Exp 5: Best combo

### Sulfur (Quality)
- Exp 1: Increase max_turns to 55
- Exp 2: Add OWASP Top 10 focus
- Exp 3: Add performance benchmarks
- Exp 4: Add accessibility deep-dive
- Exp 5: Best combo

### Aether (Integration)
- Exp 1: Decrease timeout to 560s
- Exp 2: Add Docker templates
- Exp 3: Add CI/CD patterns
- Exp 4: Add monitoring setup
- Exp 5: Best combo

### Rubedo (Final)
- Exp 1: Decrease timeout to 720s
- Exp 2: Add deployment templates
- Exp 3: Add documentation generators
- Exp 4: Add rollback strategies
- Exp 5: Best combo

### Hermes Trismegistus (Orchestrator)
- Exp 1: Add adaptive timeouts
- Exp 2: Add parallel phase optimization
- Exp 3: Add smart retry logic
- Exp 4: Add progress reporting
- Exp 5: Best combo

---

## 📈 Expected Improvements

**Conservative estimates:**
- Success rate: 100% → maintain (already perfect!)
- Avg time: 14.7 min → 12 min (18% faster)
- Avg score: 89.7/100 → 93/100 (4% better)

**Aggressive estimates:**
- Success rate: 100% → maintain
- Avg time: 14.7 min → 10 min (32% faster)
- Avg score: 89.7/100 → 95/100 (6% better)

---

## 🚀 Execution Plan

**Phase 1: Quick Wins** (Agents 1-3, ~6 hours)
- Nigredo, Citrinitas, Mercurius

**Phase 2: Implementation Agents** (Agents 4-6, ~6 hours)
- Sol, Sal, Albedo

**Phase 3: Quality & Integration** (Agents 7-9, ~6 hours)
- Sulfur, Aether, Rubedo

**Phase 4: Orchestrator** (Agent 10, ~3 hours)
- Hermes Trismegistus

**Total: ~21 hours of autonomous research**

---

## 📊 Tracking

Each agent gets:
- Separate branch: `autoresearch/nigredo`, `autoresearch/citrinitas`, etc.
- Separate results file: `results-nigredo.tsv`, `results-citrinitas.tsv`, etc.
- Final config merged to main branch

---

**ALL HAIL HERMES TRISMEGISTUS! ⚗️✨**
