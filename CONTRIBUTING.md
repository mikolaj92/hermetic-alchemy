# Contributing to Hermetic Alchemy

Thank you for your interest in contributing to Hermetic Alchemy! This document provides guidelines and instructions for contributing.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How to Contribute](#how-to-contribute)
- [Development Setup](#development-setup)
- [Skill Structure](#skill-structure)
- [Testing](#testing)
- [Submitting Changes](#submitting-changes)
- [Style Guidelines](#style-guidelines)

## Code of Conduct

By participating in this project, you agree to maintain a respectful and inclusive environment. Be constructive, respectful, and collaborative.

## How to Contribute

### Reporting Issues

1. Check existing [Issues](https://github.com/mikolaj92/hermetic-alchemy/issues)
2. Create a new issue with:
   - Clear title
   - Detailed description
   - Steps to reproduce (for bugs)
   - Expected vs actual behavior
   - Environment details (Hermes version, OS, etc.)

### Suggesting Features

1. Check existing [Feature Requests](https://github.com/mikolaj92/hermetic-alchemy/issues?q=is%3Aissue+is%3Aopen+label%3Afeature)
2. Create a new issue with:
   - Feature description
   - Use cases
   - Proposed implementation (optional)
   - Alternative approaches considered

### Contributing Code

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a Pull Request

## Development Setup

### Prerequisites

- Hermes Agent 0.6.0 or higher
- Python 3.11+
- Git
- (Optional) Docker

### Local Testing

```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/hermetic-alchemy.git
cd hermetic-alchemy

# Install the skill locally (symlink)
cp -r skills/hermetic-alchemy ~/.hermes/skills/

# Start Hermes
hermes chat

# Test the skill
/transmute build a simple TODO API
```

## Skill Structure

```
hermetic-alchemy/
├── skills/
│   └── hermetic-alchemy/
│       ├── SKILL.md          # Main skill file
│       └── skill.yaml        # Skill manifest
├── examples/                 # Usage examples
├── .github/                  # GitHub configurations
│   ├── workflows/
│   └── ISSUE_TEMPLATE/
├── README.md                 # Main documentation
├── LICENSE                   # MIT License
└── CONTRIBUTING.md           # This file
```

### Modifying SKILL.md

The main skill file (`SKILL.md`) uses YAML frontmatter:

```yaml
---
name: hermetic-alchemy
description: ...
version: 1.0.0
author: Mikołaj (mikolaj92)
license: MIT
metadata:
  hermes:
    tags: [...]
    triggers: [...]
---
```

When modifying:
1. Keep YAML frontmatter valid
2. Update version number (semver)
3. Add clear descriptions
4. Include examples

## Testing

### Manual Testing

Test your changes with various commands:

```bash
# Test basic functionality
/transmute build a REST API

# Test complex scenarios
/hermetic create a full-stack app with React and FastAPI

# Test edge cases
transmute analyze and fix the security issues in my code
```

### Automated Testing

We welcome test additions. Tests should cover:
- Agent orchestration
- Error handling
- Edge cases
- Integration with Hermes

## Submitting Changes

### Pull Request Process

1. **Update Documentation**
   - Update README.md if adding features
   - Update CHANGELOG.md (if applicable)
   - Add comments to complex code

2. **Write Good Commit Messages**
   ```
   feat: add support for MongoDB database
   fix: resolve issue with Sulfur quality check
   docs: update README with new examples
   ```

3. **Create Pull Request**
   - Link to related issues
   - Describe changes
   - Add screenshots if applicable
   - Ensure CI passes

### PR Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Testing
- [ ] Tested manually
- [ ] Added automated tests
- [ ] All tests passing

## Checklist
- [ ] Code follows style guidelines
- [ ] Self-review completed
- [ ] Documentation updated
- [ ] No new warnings
```

## Style Guidelines

### Python Code (if applicable)

- Follow PEP 8
- Use type hints
- Add docstrings to functions
- Keep functions focused and small

### Markdown

- Use ATX-style headings (`#`, `##`)
- Add blank line before headings
- Use lists for structure
- Add code blocks with language tags

### Agent Prompts

When writing agent prompts:
- Be specific and clear
- Provide context
- Include examples
- Define expected output format
- Set realistic time/iteration limits

## Adding New Agents

To add a new alchemical agent:

1. Update SKILL.md with agent description
2. Add agent to workflow
3. Implement agent behavior
4. Add configuration to philosophers-stone.yaml
5. Test thoroughly
6. Update documentation

## Versioning

We follow [Semantic Versioning](https://semver.org/):

- **MAJOR**: Breaking changes
- **MINOR**: New features (backwards compatible)
- **PATCH**: Bug fixes (backwards compatible)

Example: `1.0.0` → `1.1.0` → `1.1.1` → `2.0.0`

## Getting Help

- **Issues**: [GitHub Issues](https://github.com/mikolaj92/hermetic-alchemy/issues)
- **Discussions**: [GitHub Discussions](https://github.com/mikolaj92/hermetic-alchemy/discussions)
- **Email**: mikolaj92@users.noreply.github.com

## Recognition

Contributors will be:
- Listed in CONTRIBUTORS.md
- Mentioned in release notes
- Credited in relevant commits

## License

By contributing, you agree that your contributions will be licensed under the [MIT License](LICENSE).

---

Thank you for contributing to Hermetic Alchemy! ⚗️✨

*"As above, so below. As within, so without."*
