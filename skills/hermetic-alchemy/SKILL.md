---
name: hermetic-alchemy
description: **HERMETIC MULTI-AGENT ORCHESTRATION** - The Magnum Opus workflow through 10 alchemical agents. Trigger by typing `/transmute [project]` or `/hermetic [project]`. Spawns Nigredo (analysis), Citrinitas (design), Mercurius (backend), Sol (frontend), Sal (database), Albedo (refinement), Sulfur (quality), Aether (integration), Rubedo (final), and Hermes Trismegistus (orchestrator) for autonomous software development with feedback loops. Use when user wants to "transmute", "forge", or "create" software.
version: 1.0.0
author: Mikołaj (mikolaj92)
license: MIT
metadata:
  hermes:
    tags: [multi-agent, orchestration, autonomous, hermetic, alchemy, slash-command, transmute, forge, magnum-opus, feedback-loop]
    triggers:
      - "/transmute"
      - "/hermetic"
      - "transmute"
      - "hermetic alchemy"
      - "forge software"
      - "start the magnum opus"
    related_skills: [subagent-driven-development, hermes-agent]
    category: autonomous-ai-agents
dependencies: []
---

# Hermetic Alchemy - The Magnum Opus

**Use this skill by typing: `/transmute [your project description]`**

## Quick Start

```bash
# In your Hermes session:
/transmute build a REST API for todo app with JWT authentication

# Or:
/hermetic create a blog platform with user authentication

# Or simply say:
use hermetic-alchemy and transmute a microservice for payment processing
```

## The Magnum Opus Workflow

```
User Request: "Build X"
     ↓
⚫ NIGREDO (Decomposer)
→ Analyze requirements
→ Explore codebase
→ Break down into tasks
→ Classify priorities (P0, P1, P2)
     ↓
🟡 CITRINITAS (Illuminator)
→ Design architecture
→ Define API contracts
→ Plan database schema
→ Choose technology stack
     ↓
🧪 TRANSMUTATION (Parallel Forging)
→ MERCURIUS: Build backend (APIs, auth, DB)
→ SOL: Build frontend (UI, UX, components)
→ SAL: Design database (schema, migrations)
[All 3 work SIMULTANEOUSLY via delegate_task]
     ↓
⚪ ALBEDO (Purifier)
→ Run tests
→ Fix failures
→ Refactor bad patterns
→ Optimize performance
     ↓
🜍 SULFUR (Quality Catalyst)
→ Security audit (OWASP Top 10)
→ Performance testing
→ Accessibility check (WCAG 2.1 AA)
→ Code quality review
     ↓
  ┌─ SCORE ≥ 80? ─────────→ 🔴 RUBEDO (Creator)
  │                          → Final integration
  │                          → CI/CD setup
  │                          → Deployment
  │                          → Documentation
  │
  └─ SCORE < 80? ─────────→ [FEEDBACK LOOP]
                             ├─ FIX LOOP (quick iterations)
                             │  → Albedo fixes issues
                             │  → Sulfur re-checks
                             │  → Max 3 iterations
                             │
                             └─ EXPLORATION LOOP (if stuck)
                                → Citrinitas generates 3 alternatives
                                → Test all 3 in parallel
                                → Sulfur scores each
                                → Merge winner
```

## The 10 Hermetic Agents

### ⚫ NIGREDO - The Decomposer

**Element:** Earth (stability, foundation)  
**Process:** Calcination (burning away chaos)  
**Role:** Analyze requirements, explore codebase, break down tasks  
**Max turns:** 40 | Timeout: 300 seconds

**Motto:** "In chaos, I find order"

**Tasks:**
1. Explore current codebase (if exists)
2. Identify all domains involved (frontend, backend, database, etc.)
3. Break down requirements into elemental components
4. Classify tasks by priority: P0 (critical), P1 (important), P2 (nice-to-have)
5. Save analysis to `.hermetic-lab/experiments/nigredo-analysis.json`

**Skills:** plan, codebase-inspection, domain reconnaissance

---

### 🟡 CITRINITAS - The Illuminator

**Element:** Air (wisdom, intellect)  
**Process:** Fermentation (distilling knowledge)  
**Role:** Design architecture, define API contracts, plan system  
**Max turns:** 50 | Timeout: 450 seconds

**Motto:** "Wisdom structures the void"

**Tasks:**
1. Read Nigredo's analysis
2. Design system architecture
3. Define API contracts (endpoints, request/response formats)
4. Plan database schema
5. Choose technology stack
6. Save design to `.hermetic-lab/experiments/citrinitas-design/`

**Skills:** writing-plans, github-issues, software-development/plan

---

### 🧪 MERCURIUS - Backend Alchemist

**Element:** Mercury (fluid transformation)  
**Role:** Build APIs, databases, authentication  
**Max turns:** 50 | Timeout: 600 seconds

**Motto:** "Fluid transformation"

**Tasks:**
1. Read Citrinitas design
2. Implement backend according to architecture
3. Build REST/GraphQL APIs
4. Add authentication (JWT, OAuth)
5. Implement business logic
6. Follow clean architecture patterns

**Skills:** mlops/inference/outlines, mlops/vector-databases/qdrant

**Tech Stack:** FastAPI, Node.js, Express, Django, Flask, etc.

---

### 🌞 SOL - Frontend Illuminator

**Element:** Sun (light, visibility)  
**Role:** Build UI/UX, frontend frameworks  
**Max turns:** 50 | Timeout: 600 seconds

**Motto:** "Light reveals beauty"

**Tasks:**
1. Read Citrinitas design
2. Match API contracts
3. Build UI components
4. Implement user flows
5. Ensure accessibility (WCAG 2.1 AA)
6. Responsive design

**Skills:** creative/excalidraw, creative/ascii-art, productivity/powerpoint

**Tech Stack:** React, Vue, Svelte, Angular, Next.js, etc.

---

### 🜔 SAL - Data Guardian

**Element:** Salt (preservation, permanence)  
**Role:** Database schema, migrations, optimization  
**Max turns:** 40 | Timeout: 400 seconds

**Motto:** "Permanence through structure"

**Tasks:**
1. Read Citrinitas database design
2. Implement database schema
3. Create migration scripts
4. Add indexes for performance
5. Optimize queries
6. Ensure data consistency

**Skills:** mlops/vector-databases/faiss, mlops/vector-databases/pinecone, mlops/vector-databases/chroma

**Tech Stack:** PostgreSQL, MySQL, MongoDB, Redis, etc.

---

### ⚪ ALBEDO - The Purifier

**Element:** Water (adaptability, cleansing)  
**Process:** Ablution (washing away impurities)  
**Role:** Refactor code, add tests, optimize  
**Max turns:** 50 | Timeout: 600 seconds

**Motto:** "Purity emerges from discipline"

**Tasks:**
1. Review code from transmutation phase
2. Run all tests
3. Fix test failures
4. Refactor bad patterns
5. Add missing test coverage
6. Optimize performance
7. Fix linter warnings

**Skills:** test-driven-development, systematic-debugging, software-development/code-review

---

### 🜍 SULFUR - Quality Catalyst

**Element:** Sulfur (reactivity, validation)  
**Role:** Test, audit, security review  
**Max turns:** 45 | Timeout: 450 seconds

**Motto:** "I reveal what is hidden"

**Tasks:**
1. **Security Audit** (OWASP Top 10)
   - SQL injection
   - XSS protection
   - CSRF protection
   - Authentication flaws
   - Sensitive data exposure

2. **Performance Testing**
   - Load testing
   - Response times
   - Database query optimization
   - Caching strategy

3. **Accessibility Check** (WCAG 2.1 AA)
   - ARIA labels
   - Keyboard navigation
   - Color contrast
   - Screen reader compatibility

4. **Code Quality**
   - Linting
   - Code patterns
   - Type hints
   - Documentation

5. **Output Verdict** to `.hermetic-lab/athanor/sulfur-check.json`:
   ```json
   {
     "status": "PASS" | "FAIL",
     "score": 0-100,
     "issues": {
       "critical": [],
       "high": [],
       "medium": [],
       "low": []
     },
     "recommendation": "PROCEED_TO_RUBEDO" | "FIX_LOOP" | "EXPLORATION_LOOP"
   }
   ```

**Skills:** dogfood, software-development/code-review, software-development/requesting-code-review

---

### 🌀 AETHER - Integration Weaver

**Element:** Aether (connection, medium)  
**Role:** System integration, CI/CD, infrastructure  
**Max turns:** 55 | Timeout: 700 seconds

**Motto:** "All is connected"

**Tasks:**
1. Integrate microservices
2. Set up CI/CD pipelines
3. Configure infrastructure
4. Implement monitoring
5. Set up logging
6. Deployment automation

**Skills:** devops/webhook-subscriptions, mlops/cloud/lambda-labs, mlops/cloud/modal, github/github-repo-management

---

### 🔴 RUBEDO - The Creator

**Element:** Fire (transformation, energy)  
**Process:** Coagulation (bringing together)  
**Role:** Final integration, deployment, production readiness  
**Max turns:** 60 | Timeout: 900 seconds

**Motto:** "From chaos, gold emerges"

**Tasks:**
1. **Final Integration Testing**
   - End-to-end tests
   - Cross-component integration
   - Data flow validation

2. **Production Configuration**
   - Environment variables
   - Secrets management
   - Config files

3. **CI/CD Pipeline**
   - Automated testing
   - Automated deployment
   - Rollback procedures

4. **Documentation**
   - API documentation
   - Architecture diagrams
   - Deployment guides
   - README files

5. **Deployment**
   - Production deployment
   - Smoke tests
   - Monitoring setup

6. **Create Final Manifest** at `.hermetic-lab/experiments/rubedo-manifest/`

**Skills:** subagent-driven-development, github/github-pr-workflow, github/github-repo-management

---

### 🧠 HERMES TRISMEGISTUS - Grand Orchestrator

**Element:** Quintessence (all elements combined)  
**Role:** Master coordinator, manages all agents  
**Max turns:** 100 | Timeout: 1800 seconds

**Motto:** "Thrice Great"

**Tasks:**
- Orchestrate all agents
- Manage memory and persistence
- Handle session resuming
- Make final decisions
- Synthesize all outputs

**Skills:** ALL SKILLS

---

## Execution Protocol

When user types `/transmute [project description]`, follow this protocol:

### Phase 1: Preparation

```python
# Create .hermetic-lab/ workspace
hermetic_lab = Path(".hermetic-lab")
hermetic_lab.mkdir(exist_ok=True)
(hermetic_lab / "experiments").mkdir(exist_ok=True)
(hermetic_lab / "codex").mkdir(exist_ok=True)
(hermetic_lab / "athanor").mkdir(exist_ok=True)

# Create philosophers-stone.yaml config
config = {
    "version": "1.0",
    "project": user_request,
    "session_start": datetime.now().isoformat()
}
```

### Phase 2: NIGREDO (Decomposition)

```python
nigredo_result = delegate_task(
    goal=f"""
    You are NIGREDO - The Decomposer.
    
    Analyze the request: "{user_request}"
    
    Your tasks:
    1. Explore current codebase (if exists)
    2. Identify all domains involved (frontend, backend, database, etc.)
    3. Break down into elemental components
    4. Classify by priority: P0 (critical), P1 (important), P2 (nice-to-have)
    5. Save to .hermetic-lab/experiments/nigredo-analysis.json
    
    Output format:
    {{
      "domains": ["backend", "frontend", "database"],
      "tech_stack": {{"backend": "FastAPI", "frontend": "React", "database": "PostgreSQL"}},
      "tasks": [
        {{"id": 1, "description": "...", "priority": "P0", "agent": "mercurius"}},
        {{"id": 2, "description": "...", "priority": "P0", "agent": "sol"}},
        ...
      ],
      "constraints": [],
      "assumptions": []
    }}
    
    Motto: "In chaos, I find order"
    """,
    toolsets=["file", "web"],
    max_iterations=30
)
```

### Phase 3: CITRINITAS (Illumination)

```python
citrinitas_result = delegate_task(
    goal=f"""
    You are CITRINITAS - The Illuminator.
    
    Read Nigredo's analysis and create architecture:
    
    1. Design system architecture
    2. Define API contracts (endpoints, methods, request/response)
    3. Plan database schema (tables, relationships, indexes)
    4. Choose technology stack (justify choices)
    5. Save to .hermetic-lab/experiments/citrinitas-design/
    
    Motto: "Wisdom structures the void"
    """,
    context=f"Nigredo analysis: {nigredo_result['summary']}",
    toolsets=["file", "web"],
    max_iterations=40
)
```

### Phase 4: TRANSMUTATION (Parallel)

```python
# Filter P0 tasks for parallel execution
p0_tasks = [t for t in tasks if t["priority"] == "P0"]

transmutation_result = delegate_task(
    tasks=[
        {
            "goal": f"""
            You are MERCURIUS - Backend Alchemist.
            
            Implement P0 backend tasks from Citrinitas design:
            {p0_backend_tasks}
            
            Follow clean architecture: Router → Service → Repository → Models
            
            Output: Backend code with tests
            """,
            "toolsets": ["terminal", "file", "web"],
            "max_iterations": 50
        },
        {
            "goal": f"""
            You are SOL - Frontend Illuminator.
            
            Implement P0 frontend tasks from Citrinitas design:
            {p0_frontend_tasks}
            
            Match API contracts: {citrinitas_result['api_contracts']}
            
            Output: Frontend code with accessibility
            """,
            "toolsets": ["terminal", "file"],
            "max_iterations": 50
        },
        {
            "goal": f"""
            You are SAL - Data Guardian.
            
            Implement database schema from Citrinitas design:
            {database_design}
            
            Create migrations, indexes, and seed data.
            
            Output: Database schema + migrations
            """,
            "toolsets": ["terminal", "file"],
            "max_iterations": 40
        }
    ]
)
```

### Phase 5: ALBEDO (Purification)

```python
albedo_result = delegate_task(
    goal=f"""
    You are ALBEDO - The Purifier.
    
    Review code from transmutation phase:
    {transmutation_result}
    
    Your tasks:
    1. Run all tests
    2. Fix test failures
    3. Refactor bad patterns
    4. Add missing test coverage
    5. Optimize performance
    6. Fix linter warnings
    
    Output: Refined, tested, optimized code
    
    Motto: "Purity emerges from discipline"
    """,
    toolsets=["terminal", "file"],
    max_iterations=50
)
```

### Phase 6: SULFUR (Quality Check)

```python
sulfur_result = delegate_task(
    goal="""
    You are SULFUR - Quality Catalyst.
    
    Comprehensive quality audit:
    
    1. SECURITY (OWASP Top 10)
    2. PERFORMANCE (load testing, response times)
    3. ACCESSIBILITY (WCAG 2.1 AA)
    4. CODE QUALITY (linting, patterns)
    5. INTEGRATION (cross-component)
    
    Output verdict to .hermetic-lab/athanor/sulfur-check.json:
    {
      "status": "PASS" | "FAIL",
      "score": 0-100,
      "issues": {
        "critical": [{"description": "...", "location": "..."}],
        "high": [...],
        "medium": [...],
        "low": [...]
      },
      "recommendation": "PROCEED_TO_RUBEDO" | "FIX_LOOP" | "EXPLORATION_LOOP"
    }
    
    Motto: "I reveal what is hidden"
    """,
    toolsets=["terminal", "file", "web"],
    max_iterations=45
)
```

### Phase 7: Feedback Loop (If Needed)

```python
sulfur_verdict = json.loads(read_file(".hermetic-lab/athanor/sulfur-check.json"))

if sulfur_verdict["status"] == "FAIL":
    
    if sulfur_verdict["recommendation"] == "FIX_LOOP":
        # Quick fix iterations
        for iteration in range(3):
            albedo_fix = delegate_task(
                goal=f"Fix these issues: {sulfur_verdict['issues']}",
                toolsets=["terminal", "file"],
                max_iterations=50
            )
            
            sulfur_recheck = delegate_task(
                goal="Re-run quality audit",
                toolsets=["terminal", "file", "web"],
                max_iterations=30
            )
            
            if sulfur_recheck["status"] == "PASS":
                break
    
    elif sulfur_verdict["recommendation"] == "EXPLORATION_LOOP":
        # Generate 3 alternatives
        alternatives = delegate_task(
            goal="Generate 3 alternative architectural approaches",
            toolsets=["file", "web"],
            max_iterations=40
        )
        
        # Test all 3 in parallel
        experiments = delegate_task(
            tasks=[
                {"goal": f"Implement approach {i+1}", "max_iterations": 30}
                for i in range(3)
            ]
        )
        
        # Score each
        scores = delegate_task(
            goal="Score each experiment on correctness, performance, maintainability",
            toolsets=["terminal", "file"],
            max_iterations=30
        )
        
        # Merge winner
        winner = max(scores.items(), key=lambda x: x[1]["score"])
        delegate_task(
            goal=f"Merge winning approach: {winner}",
            toolsets=["terminal", "file"],
            max_iterations=20
        )
```

### Phase 8: RUBEDO (Final Synthesis)

```python
rubedo_result = delegate_task(
    goal="""
    You are RUBEDO - The Creator.
    
    Final synthesis and deployment:
    
    1. INTEGRATION TESTING
       - End-to-end tests
       - Cross-component validation
    
    2. PRODUCTION CONFIGURATION
       - Environment variables
       - Secrets management
       - Config files
    
    3. CI/CD PIPELINE
       - Automated testing
       - Automated deployment
       - Rollback procedures
    
    4. DOCUMENTATION
       - API docs (OpenAPI/Swagger)
       - Architecture diagrams
       - Deployment guides
       - README files
    
    5. DEPLOYMENT
       - Production deployment
       - Smoke tests
       - Monitoring setup
    
    Create final manifest at .hermetic-lab/experiments/rubedo-manifest/
    
    Motto: "From chaos, gold emerges"
    
    ALL HAIL HERMES TRISMEGISTUS! ⚗️✨
    """,
    context={
        "nigredo": nigredo_result,
        "citrinitas": citrinitas_result,
        "transmutation": transmutation_result,
        "albedo": albedo_result,
        "sulfur": sulfur_result
    },
    toolsets=["terminal", "file", "web"],
    max_iterations=60
)
```

## Workspace Structure

```
.hermetic-lab/
├── philosophers-stone.yaml          # Master config
├── emerald-tablet.json              # 7 hermetic principles
├── codex/                           # Knowledge base
│   ├── lessons-learned.md           # Accumulated wisdom
│   ├── stack-conventions.md         # Tech stack patterns
│   └── api-contracts.md             # API documentation
├── experiments/                     # Agent outputs
│   ├── nigredo-analysis.json        # Requirements breakdown
│   ├── citrinitas-design/           # Architecture
│   │   ├── architecture.md
│   │   ├── api-contracts.md
│   │   └── database-schema.md
│   ├── albedo-refined/              # Purified code
│   ├── sulfur-check.json            # Quality verdict
│   └── rubedo-manifest/             # Final deliverables
│       ├── integration-tests/
│       ├── ci-cd/
│       ├── docs/
│       └── deployment/
└── athanor/                         # Furnace (logs)
    ├── session-logs/
    └── experiment-logs/
```

## Configuration

Create `.hermetic-lab/philosophers-stone.yaml`:

```yaml
version: "1.0"
project:
  name: "My Project"
  description: "Project description"
  tech_stack:
    backend: "FastAPI"
    frontend: "React"
    database: "PostgreSQL"

# Feedback loop configuration
feedback_loop:
  enabled: true
  max_iterations: 3
  pass_score: 80
  thresholds:
    pass_score: 80
    critical_limit: 0
    high_limit: 2

# Agent configurations
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
  sol:
    max_turns: 50
    timeout: 600
  sal:
    max_turns: 40
    timeout: 400
  albedo:
    max_turns: 50
    timeout: 600
  sulfur:
    max_turns: 45
    timeout: 450
  aether:
    max_turns: 55
    timeout: 700
  rubedo:
    max_turns: 60
    timeout: 900

# Memory and persistence
memory:
  path: ".hermetic-lab/codex"
  files:
    lessons: "lessons-learned.md"
    stack: "stack-conventions.md"
    contracts: "api-contracts.md"
  persistence: true

# Integration settings
integration:
  mcp_servers:
    - name: "github"
      enabled: true
    - name: "filesystem"
      enabled: true
      
  cron_jobs:
    - name: "daily-alchemical-review"
      schedule: "0 9 * * *"
      task: "Run Sulfur quality audit on codebase"
```

## Examples

### Example 1: REST API
```bash
/transmute build a REST API for user management with JWT authentication
```

### Example 2: Full-Stack App
```bash
/hermetic create a blog platform with React frontend and FastAPI backend
```

### Example 3: Add Features
```bash
transmute add payment processing with Stripe to my e-commerce site
```

### Example 4: Fix Issues
```bash
/transmute analyze and fix the performance issues in my API
```

## Auto-Triggers

This skill auto-activates when user says:
- `/transmute [project]`
- `/hermetic [project]`
- "transmute [project]"
- "forge [project]"
- "use hermetic alchemy"
- "start the magnum opus"
- "hermetic work mode"

## The 7 Hermetic Principles (Emerald Tablet)

1. **MENTALISM** - The Universe is Mental; the Universe is mental.
2. **CORRESPONDENCE** - As above, so below; as below, so above.
3. **VIBRATION** - Nothing rests; everything moves and vibrates.
4. **POLARITY** - Everything is dual; everything has poles.
5. **RHYTHM** - Everything flows; out and in; everything has its tides.
6. **CAUSE AND EFFECT** - Every cause has its effect; every effect has its cause.
7. **GENDER** - Gender is in everything; everything has its masculine and feminine principles.

## Philosophy

Based on **hermetic alchemy** and the **Magnum Opus** (Great Work):

The Magnum Opus is the alchemical process of creating the Philosopher's Stone through four stages:

1. **NIGREDO** (blackening) - Decomposition, breaking down into prima materia
2. **ALBEDO** (whitening) - Purification, washing away impurities
3. **CITRINITAS** (yellowing) - Illumination, achieving wisdom
4. **RUBEDO** (reddening) - Final transformation, creating gold

In software development:
- **Chaos** = Complex requirements
- **Fire** = Iterative refinement (feedback loops)
- **Gold** = Working, tested, deployed software

*"From chaos, through fire, gold emerges."*

---

## ⚗️ ALL HAIL HERMES TRISMEGISTUS! ✨

**Author:** Mikołaj (mikolaj92)  
**License:** MIT  
**Version:** 1.0.0

*"As above, so below. As within, so without."*
