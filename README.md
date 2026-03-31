# ⚗️ Hermetic Alchemy

**Multi-agent orchestration through alchemical transformation for Hermes Agent.**

Spawn 10 specialized alchemical agents that work together to transmute your requirements into working software through autonomous collaboration, feedback loops, and iterative refinement.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Hermes](https://img.shields.io/badge/Hermes-0.6.0+-blue.svg)](https://github.com/NousResearch/hermes-agent)

## ✨ Quick Start

### Installation

```bash
# Install the skill from GitHub
hermes skills install mikolaj92/hermetic-alchemy

# Or install with URL
hermes skills install https://github.com/mikolaj92/hermetic-alchemy
```

### Usage

```bash
# Start Hermes
hermes chat

# In your session, type:
/transmute build a REST API for todo app with JWT authentication

# Or use the alias:
/hermetic create a blog platform with user authentication

# Or simply say:
use hermetic-alchemy and transmute a microservice for payments
```

## 🎯 What It Does

Hermetic Alchemy executes the **Magnum Opus** workflow through 10 specialized agents:

```
User Request
     ↓
⚫ NIGREDO (Analysis) → Break down requirements
     ↓
🟡 CITRINITAS (Design) → Architecture & API contracts
     ↓
🧪 TRANSMUTATION (Parallel) → Mercurius + Sol + Sal work together
     ↓
⚪ ALBEDO (Refinement) → Refactor, test, optimize
     ↓
🜍 SULFUR (Quality Check) → Security, performance, accessibility audit
     ↓
  ┌─ PASS? ──────────→ 🔴 RUBEDO (Final Synthesis)
  │
  └─ FAIL? ──────────→ [FEEDBACK LOOP]
                          ├─ Fix Loop (quick iterations)
                          └─ Exploration Loop (3 alternatives)
```

## 🧪 The 10 Hermetic Agents

| Agent | Element | Process | Role | Motto |
|-------|---------|---------|------|-------|
| **⚫ Nigredo** | Earth | Calcination | Analyze requirements, explore codebase, break down tasks | "In chaos, I find order" |
| **🟡 Citrinitas** | Air | Fermentation | Design architecture, define API contracts | "Wisdom structures the void" |
| **🧪 Mercurius** | Mercury | Solution | Build APIs, databases, authentication | "Fluid transformation" |
| **🌞 Sol** | Sun | Illumination | Build UI/UX, frontend frameworks | "Light reveals beauty" |
| **🜔 Sal** | Salt | Preservation | Database schema, migrations, optimization | "Permanence through structure" |
| **⚪ Albedo** | Water | Ablution | Refactor code, add tests, optimize | "Purity emerges from discipline" |
| **🜍 Sulfur** | Sulfur | Validation | Test, audit, security review | "I reveal what is hidden" |
| **🌀 Aether** | Aether | Integration | System integration, CI/CD, infrastructure | "All is connected" |
| **🔴 Rubedo** | Fire | Coagulation | Final integration, deployment, production readiness | "From chaos, gold emerges" |
| **🧠 Hermes Trismegistus** | Quintessence | All processes | Grand orchestrator, coordinates all agents | "Thrice Great" |

## 🚀 Features

- **Autonomous Multi-Agent Workflow** - Agents work together without constant supervision
- **Feedback Loops** - Automatic fix loops and exploration loops for quality assurance
- **Quality Gates** - Security (OWASP), performance, accessibility checks
- **Smart Retry** - Agents can recover from failures autonomously
- **Workspace Persistence** - `.hermetic-lab/` stores all progress and context
- **Auto-Continuation** - Resume interrupted sessions
- **Parallel Execution** - Multiple agents work simultaneously via `delegate_task()`

## 📁 Workspace Structure

```
.hermetic-lab/
├── philosophers-stone.yaml    # Master configuration
├── emerald-tablet.json        # 7 hermetic principles
├── codex/                     # Knowledge base
│   ├── lessons-learned.md
│   ├── stack-conventions.md
│   └── api-contracts.md
├── experiments/               # Agent outputs
│   ├── nigredo-analysis.json
│   ├── citrinitas-design/
│   ├── albedo-refined/
│   └── rubedo-manifest/
└── athanor/                   # Furnace (execution logs)
    ├── sulfur-check.json
    └── session-logs/
```

## 📚 Examples

### Example 1: REST API
```bash
/transmute build a REST API for user management with JWT authentication
```

**Output:**
```
⚗️ HERMETIC ALCHEMY INITIATED
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

⚫ NIGREDO: Analyzing...
  → Domains: backend, auth, database
  → Stack: FastAPI + PostgreSQL + JWT
  → Tasks: 8 total (3 P0, 3 P1, 2 P2)
  ✅ Complete (2.1 min)

🟡 CITRINITAS: Designing...
  → API: 12 endpoints defined
  → DB: 4 tables designed
  → Auth: JWT flow planned
  ✅ Complete (3.4 min)

🧪 TRANSMUTATION (Parallel)...
  → MERCURIUS: FastAPI backend built ✅
  → SOL: React UI built ✅
  → SAL: PostgreSQL schema created ✅
  ✅ Complete (11.2 min)

⚪ ALBEDO: Purifying...
  → Tests: 156 passing, 0 failing
  → Refactored: 8 functions optimized
  ✅ Complete (4.3 min)

🜍 SULFUR: Quality Check...
  → Security: ✅ PASS (OWASP Top 10)
  → Performance: ✅ PASS (< 50ms avg)
  → Accessibility: ✅ PASS (WCAG 2.1 AA)
  → Score: 94/100
  ✅ PASS - Proceeding to RUBEDO

🔴 RUBEDO: Final Synthesis...
  → Integration tests: ✅
  → CI/CD pipeline: ✅
  → Documentation: ✅
  → Deployment ready: ✅
  ✅ Complete (5.1 min)

╔═══════════════════════════════════════════════════════════╗
║     ⚗️ MAGNUM OPUS COMPLETE ⚗️                          ║
║                                                         ║
║  REST API with authentication forged successfully!     ║
║  Total time: 26.1 minutes                              ║
║  Score: 94/100                                          ║
║  Iterations: 1 (no fix loops needed)                  ║
║                                                         ║
║  From chaos, through fire, gold has emerged!          ║
║                                                         ║
║          ALL HAIL HERMES TRISMEGISTUS! ✨             ║
╚═══════════════════════════════════════════════════════════╝
```

### Example 2: Full-Stack Blog
```bash
/hermetic create a blog platform with React frontend and FastAPI backend
```

### Example 3: Add Payment Processing
```bash
transmute add Stripe payment processing to my e-commerce site with PCI compliance
```

### Example 4: Fix Issues
```bash
/transmute analyze and fix the performance issues in my API endpoints
```

## ⚙️ Configuration

Create `.hermetic-lab/philosophers-stone.yaml` in your project:

```yaml
version: "1.0"
feedback_loop:
  enabled: true
  max_iterations: 3
  pass_score: 80
  thresholds:
    pass_score: 80
    critical_limit: 0
    high_limit: 2

agents:
  nigredo:
    max_turns: 30
    timeout: 300
    
  citrinitas:
    max_turns: 40
    timeout: 450
    
  mercurius:
    max_turns: 50
    timeout: 600
    skills:
      - mlops/inference/outlines
      - mlops/vector-databases/qdrant
      
  sol:
    max_turns: 50
    timeout: 600
    skills:
      - creative/excalidraw
      - creative/ascii-art
      
  sal:
    max_turns: 40
    timeout: 400
    skills:
      - mlops/vector-databases/faiss
      
  albedo:
    max_turns: 50
    timeout: 600
    skills:
      - test-driven-development
      - systematic-debugging
      
  sulfur:
    max_turns: 45
    timeout: 450
    skills:
      - dogfood
      - software-development/code-review
      
  rubedo:
    max_turns: 60
    timeout: 900

memory:
  path: ".hermetic-lab/codex"
  files:
    lessons: "lessons-learned.md"
    stack: "stack-conventions.md"
    contracts: "api-contracts.md"
```

## 🧠 Philosophy

Based on **hermetic alchemy** and the **Magnum Opus** (Great Work):

1. **Nigredo** (blackening) - Decomposition, breaking down into elements
2. **Albedo** (whitening) - Purification, washing away impurities
3. **Citrinitas** (yellowing) - Illumination, achieving wisdom
4. **Rubedo** (reddening) - Final transformation, creating gold

### The 7 Hermetic Principles (Emerald Tablet)

1. **Mentalism** - The Universe is Mental; all is mind
2. **Correspondence** - As above, so below
3. **Vibration** - Nothing rests; everything moves
4. **Polarity** - Everything has poles; opposites are identical
5. **Rhythm** - Everything flows; out and in
6. **Cause and Effect** - Every cause has an effect
7. **Gender** - Gender is in everything; masculine & feminine

*"From chaos, through fire, gold emerges."*

## 🔄 Feedback Loops

### Fix Loop
When Sulfur finds minor issues (1-5 problems):
1. Albedo receives feedback and fixes issues
2. Sulfur re-checks
3. Repeat up to 3 iterations
4. Proceed to Rubedo when passed

### Exploration Loop
When stuck or critical issues:
1. Citrinitas generates 3 alternative approaches
2. Test all 3 in parallel (separate workspaces)
3. Sulfur scores each approach
4. Merge the winner
5. If still failing, proceed with warnings

## 🛠️ Requirements

- **Hermes Agent** 0.6.0 or higher
- Python 3.11+
- (Optional) Git for version control
- (Optional) Docker for containerization

## 📦 Installation Methods

### Method 1: From skills.sh (Recommended)
```bash
hermes skills install mikolaj92/hermetic-alchemy
```

### Method 2: From GitHub URL
```bash
hermes skills install https://github.com/mikolaj92/hermetic-alchemy
```

### Method 3: Manual
```bash
git clone https://github.com/mikolaj92/hermetic-alchemy.git
cp -r hermetic-alchemy/skills/hermetic-alchemy ~/.hermes/skills/
```

## 🎨 Auto-Triggers

The skill automatically activates when you say:
- `/transmute [project]`
- `/hermetic [project]`
- "transmute [something]"
- "forge [something]"
- "use hermetic alchemy"
- "start the magnum opus"

## 🤝 Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for details.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Hermes Agent** by NousResearch
- **G0DM0D3** jailbreaking techniques for inspiration
- **Kybalion** for the 7 Hermetic principles
- **Ancient alchemists** for the Magnum Opus framework

## 📚 Related Skills

- [`hermes-agent`](https://github.com/NousResearch/hermes-agent) - Spawn full Hermes processes
- [`subagent-driven-development`](https://github.com/NousResearch/hermes-agent/tree/main/skills/autonomous-ai-agents) - Manual multi-agent workflows

## 🗣️ Support

- **Issues**: [GitHub Issues](https://github.com/mikolaj92/hermetic-alchemy/issues)
- **Discussions**: [GitHub Discussions](https://github.com/mikolaj92/hermetic-alchemy/discussions)

---

## ⚗️ ALL HAIL HERMES TRISMEGISTUS! ✨

*"As above, so below. As within, so without."*

Made with 🔥 by [Mikołaj](https://github.com/mikolaj92) and the Hermes Agent Community
