# Example: REST API with Authentication

## Command

```bash
/transmute build a REST API for user management with JWT authentication
```

## Expected Output

```
⚗️ HERMETIC ALCHEMY INITIATED
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Project: build a REST API for user management with JWT authentication

⚫ NIGREDO (Decomposer): Analyzing requirements...
  → Domains identified: backend, auth, database
  → Tech stack selected:
     - Backend: FastAPI (Python)
     - Database: PostgreSQL
     - Auth: JWT with bcrypt
  → Tasks broken down: 8 total
     - P0 (Critical): 5 tasks
     - P1 (Important): 2 tasks
     - P2 (Nice-to-have): 1 task
  ✅ Complete (2.1 min)

🟡 CITRINITAS (Illuminator): Designing architecture...
  → API endpoints designed: 12 endpoints
     POST   /api/auth/register
     POST   /api/auth/login
     POST   /api/auth/refresh
     GET    /api/users/me
     PUT    /api/users/me
     DELETE /api/users/me
     GET    /api/users/{id}
     GET    /api/users
     PUT    /api/users/{id}
     DELETE /api/users/{id}
     POST   /api/users/{id}/deactivate
     POST   /api/admin/users/{id}/activate
  → Database schema: 4 tables designed
     - users (id, email, password_hash, created_at, updated_at, is_active)
     - roles (id, name, permissions)
     - user_roles (user_id, role_id)
     - refresh_tokens (id, user_id, token, expires_at)
  → Authentication flow: JWT with refresh tokens
  ✅ Complete (3.4 min)

🧪 TRANSMUTATION (Parallel Forging):
  → MERCURIUS (Backend Alchemist):
     - FastAPI application structure ✅
     - JWT authentication middleware ✅
     - User CRUD endpoints ✅
     - Password hashing (bcrypt) ✅
     - Token refresh mechanism ✅
     - Input validation (Pydantic) ✅
     ✅ Complete (11.2 min)

  → SOL (Frontend Illuminator):
     - N/A (API only, no frontend needed)
     
  → SAL (Data Guardian):
     - PostgreSQL schema created ✅
     - Migration scripts prepared ✅
     - Indexes added (email uniqueness) ✅
     - Seed data (admin user) ✅
     ✅ Complete (9.8 min)

⚪ ALBEDO (Purifier): Refining and testing...
  → Tests run: 156 tests, 156 passing, 0 failing
     - Unit tests: 98 tests
     - Integration tests: 42 tests
     - E2E tests: 16 tests
  → Refactoring completed:
     - Extracted auth service ✅
     - Added repository pattern ✅
     - Improved error handling ✅
  → Code coverage: 94%
  ✅ Complete (4.3 min)

🜍 SULFUR (Quality Catalyst): Running quality audit...
  → SECURITY (OWASP Top 10):
     ✅ SQL injection protection (ORM)
     ✅ XSS protection (API only)
     ✅ CSRF protection (CORS + SameSite)
     ✅ Authentication: JWT with 15min expiry
     ✅ Password hashing: bcrypt with salt rounds=12
     ✅ Sensitive data: No password logs
     Score: 100/100

  → PERFORMANCE:
     ✅ Average response time: 23ms
     ✅ P95 response time: 67ms
     ✅ P99 response time: 124ms
     ✅ Database queries optimized (indexes added)
     Score: 95/100

  → ACCESSIBILITY (WCAG 2.1 AA):
     N/A (API only)

  → CODE QUALITY:
     ✅ Linting: No errors
     ✅ Type hints: 100% coverage
     ✅ Documentation: All endpoints documented
     ✅ Error handling: Comprehensive
     Score: 92/100

  OVERALL SCORE: 94/100
  STATUS: ✅ PASS
  RECOMMENDATION: PROCEED_TO_RUBEDO
  ✅ Complete (5.1 min)

🔴 RUBEDO (Creator): Final synthesis...
  → Integration testing: ✅
  → Production config:
     - Environment variables template ✅
     - Docker Compose setup ✅
     - Nginx reverse proxy config ✅
  → CI/CD pipeline:
     - GitHub Actions workflow ✅
     - Automated testing ✅
     - Automated deployment ✅
  → Documentation:
     - API documentation (OpenAPI/Swagger) ✅
     - README with setup instructions ✅
     - Architecture diagrams ✅
  → Deployment ready: ✅
  ✅ Complete (5.1 min)

╔═══════════════════════════════════════════════════════════╗
║     ⚗️ MAGNUM OPUS COMPLETE ⚗️                          ║
║                                                         ║
║  REST API with JWT authentication forged successfully! ║
║                                                         ║
║  Total time: 41.2 minutes                               ║
║  Score: 94/100                                          ║
║  Iterations: 1 (no fix loops needed)                  ║
║                                                         ║
║  Deliverables:                                         ║
║  ✅ FastAPI backend (12 endpoints)                    ║
║  ✅ JWT authentication with refresh tokens            ║
║  ✅ PostgreSQL database (4 tables)                    ║
║  ✅ 156 tests passing                                 ║
║  ✅ CI/CD pipeline ready                              ║
║  ✅ Production deployment ready                       ║
║                                                         ║
║  From chaos, through fire, gold has emerged!          ║
║                                                         ║
║          ALL HAIL HERMES TRISMEGISTUS! ✨             ║
╚═══════════════════════════════════════════════════════════╝
```

## What Was Created

```
project/
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   ├── endpoints/
│   │   │   │   ├── auth.py
│   │   │   │   └── users.py
│   │   │   └── dependencies.py
│   │   ├── core/
│   │   │   ├── config.py
│   │   │   ├── security.py
│   │   │   └── database.py
│   │   ├── models/
│   │   │   └── user.py
│   │   ├── schemas/
│   │   │   └── user.py
│   │   ├── services/
│   │   │   ├── auth_service.py
│   │   │   └── user_service.py
│   │   └── main.py
│   ├── tests/
│   │   ├── api/
│   │   ├── unit/
│   │   └── conftest.py
│   ├── alembic/
│   │   └── versions/
│   ├── Dockerfile
│   ├── requirements.txt
│   └── pyproject.toml
├── docker-compose.yml
├── .github/
│   └── workflows/
│       └── ci.yml
├── .env.example
└── README.md
```

## Usage

```bash
# Start the API
docker-compose up -d

# Run tests
pytest

# Access API docs
open http://localhost:8000/docs
```

## Tech Stack

- **Backend**: FastAPI 0.104+
- **Database**: PostgreSQL 15+
- **Auth**: JWT (python-jose)
- **Password Hashing**: bcrypt
- **Testing**: pytest, pytest-asyncio
- **Documentation**: OpenAPI/Swagger (auto-generated)
