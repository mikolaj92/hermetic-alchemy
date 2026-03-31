# Changelog

All notable changes to Hermetic Alchemy will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Planned
- Web UI for monitoring alchemical transformations
- Support for more database backends (MongoDB, Redis)
- Custom agent personalities and behaviors
- Integration with external CI/CD systems
- Real-time progress streaming
- Session resumption and checkpointing
- Multi-language support
- Plugin system for custom alchemical agents

## [1.0.0] - 2026-03-31

### Added
- Initial release of Hermetic Alchemy skill
- 10 alchemical agents (Nigredo, Citrinitas, Mercurius, Sol, Sal, Albedo, Sulfur, Aether, Rubedo, Hermes Trismegistus)
- Magnum Opus workflow (4 phases: Nigredo, Albedo, Citrinitas, Rubedo)
- Transmutation phase with parallel agent execution (Mercurius, Sol, Sal)
- Feedback loops (Fix Loop, Exploration Loop)
- Quality gates (Security, Performance, Accessibility, Code Quality)
- Workspace persistence (.hermetic-lab/)
- Auto-trigger support (/transmute, /hermetic)
- Comprehensive documentation
- Example workflows (REST API, Full-stack blog)
- Philosophers-stone configuration system
- Emerald Tablet principles integration

### Features
- **Autonomous Multi-Agent Orchestration**
  - Spawn 10 specialized agents automatically
  - Parallel execution via delegate_task()
  - Session management and persistence
  
- **Feedback Loops**
  - Fix Loop: Quick iterations for minor issues (max 3)
  - Exploration Loop: Test 3 alternatives in parallel
  
- **Quality Gates**
  - Security audit (OWASP Top 10)
  - Performance testing (response times, load testing)
  - Accessibility check (WCAG 2.1 AA)
  - Code quality review (linting, patterns, type hints)
  
- **Smart Configuration**
  - philosophers-stone.yaml for project settings
  - Per-agent timeout and turn limits
  - Customizable thresholds and scores
  
- **Workspace Management**
  - .hermetic-lab/ directory structure
  - Codex for accumulated wisdom
  - Experiments for agent outputs
  - Athanor for execution logs

### Documentation
- Comprehensive README with quick start guide
- Detailed SKILL.md with agent descriptions
- Example workflows in examples/ directory
- Agent philosophies and mottoes
- Configuration guide
- Contributing guidelines

### Tech Stack Support
- **Backend**: FastAPI, Node.js, Express, Django, Flask
- **Frontend**: React, Vue, Svelte, Angular, Next.js
- **Database**: PostgreSQL, MySQL, MongoDB, Redis, Faiss, Pinecone, Qdrant

### License
- MIT License

---

## Version History

### [Unreleased]
- See above for planned features

### [1.0.0] - 2026-03-31
- Initial release
- Complete Magnum Opus workflow
- 10 alchemical agents
- Feedback loops and quality gates
- Comprehensive documentation

---

## Links

- **Repository**: https://github.com/mikolaj92/hermetic-alchemy
- **Issues**: https://github.com/mikolaj92/hermetic-alchemy/issues
- **Releases**: https://github.com/mikolaj92/hermetic-alchemy/releases

---

**ALL HAIL HERMES TRISMEGISTUS! ⚗️✨**
