# Example: Full-Stack Blog Platform

## Command

```bash
/hermetic create a blog platform with React frontend and FastAPI backend
```

## Expected Output

```
⚗️ HERMETIC ALCHEMY INITIATED
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Project: create a blog platform with React frontend and FastAPI backend

⚫ NIGREDO (Decomposer): Analyzing requirements...
  → Domains identified: backend, frontend, database
  → Tech stack selected:
     - Backend: FastAPI (Python)
     - Frontend: React + TypeScript + TailwindCSS
     - Database: PostgreSQL
     - State: React Query
     - Forms: React Hook Form + Zod
  → Tasks broken down: 14 total
     - P0 (Critical): 8 tasks
     - P1 (Important): 4 tasks
     - P2 (Nice-to-have): 2 tasks
  ✅ Complete (2.8 min)

🟡 CITRINITAS (Illuminator): Designing architecture...
  → System architecture: SPA + REST API
  → API endpoints: 18 endpoints
     Auth: register, login, logout, refresh
     Posts: create, read (list, detail), update, delete
     Comments: create, read, delete
     Users: profile, update
  → Database schema: 6 tables
     - users, posts, comments, tags, post_tags, refresh_tokens
  → Frontend routes: 8 pages
     - home, login, register, post-detail, create-post, edit-post, profile, settings
  → Authentication flow: JWT with HTTP-only cookies
  ✅ Complete (4.2 min)

🧪 TRANSMUTATION (Parallel Forging):
  → MERCURIUS (Backend Alchemist):
     - FastAPI application ✅
     - JWT auth middleware ✅
     - Blog CRUD endpoints ✅
     - Comment system ✅
     - Tag/category system ✅
     - Pagination support ✅
     - Search functionality ✅
     ✅ Complete (13.4 min)

  → SOL (Frontend Illuminator):
     - React app with Vite ✅
     - Routing (React Router) ✅
     - Authentication pages ✅
     - Blog pages (list, detail) ✅
     - Post editor (Markdown) ✅
     - Comment system UI ✅
     - Responsive design ✅
     - Dark mode support ✅
     ✅ Complete (14.7 min)

  → SAL (Data Guardian):
     - Database schema ✅
     - Migrations ✅
     - Indexes optimization ✅
     - Relationships configured ✅
     ✅ Complete (10.1 min)

⚪ ALBEDO (Purifier): Refining and testing...
  → Backend tests: 142 tests, 142 passing
  → Frontend tests: 68 tests, 68 passing
  → E2E tests: 24 tests, 24 passing
  → Refactoring:
     - Extracted services layer ✅
     - Added error boundaries ✅
     - Improved loading states ✅
  → Code coverage: 91% (backend), 87% (frontend)
  ✅ Complete (5.8 min)

🜍 SULFUR (Quality Catalyst): Running quality audit...
  → SECURITY: 96/100
  → PERFORMANCE: 92/100
  → ACCESSIBILITY: 94/100 (WCAG 2.1 AA)
  → CODE QUALITY: 90/100
  
  OVERALL SCORE: 93/100
  STATUS: ✅ PASS
  ✅ Complete (5.9 min)

🔴 RUBEDO (Creator): Final synthesis...
  → Integration testing: ✅
  → Production config: ✅
  → CI/CD pipeline: ✅
  → Documentation: ✅
  → Deployment ready: ✅
  ✅ Complete (6.2 min)

╔═══════════════════════════════════════════════════════════╗
║     ⚗️ MAGNUM OPUS COMPLETE ⚗️                          ║
║                                                         ║
║  Full-stack blog platform forged successfully!         ║
║                                                         ║
║  Total time: 53.1 minutes                               ║
║  Score: 93/100                                          ║
║  Iterations: 1 (no fix loops needed)                  ║
║                                                         ║
║  Deliverables:                                         ║
║  ✅ FastAPI backend (18 endpoints)                    ║
║  ✅ React frontend (8 pages)                          ║
║  ✅ PostgreSQL database (6 tables)                    ║
║  ✅ Authentication (JWT + cookies)                    ║
║  ✅ 234 tests passing                                 ║
║  ✅ CI/CD pipeline ready                              ║
║  ✅ Production deployment ready                       ║
║                                                         ║
║  Features:                                             ║
║  ✅ User authentication                               ║
║  ✅ Create/edit/delete posts                          ║
║  ✅ Comment system                                    ║
║  ✅ Tag system                                        ║
║  ✅ Search functionality                              ║
║  ✅ Markdown editor                                   ║
║  ✅ Dark mode                                         ║
║  ✅ Responsive design                                 ║
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
│   │   │   │   ├── posts.py
│   │   │   │   ├── comments.py
│   │   │   │   └── users.py
│   │   ├── core/
│   │   │   ├── config.py
│   │   │   ├── security.py
│   │   │   └── database.py
│   │   ├── models/
│   │   │   ├── user.py
│   │   │   ├── post.py
│   │   │   └── comment.py
│   │   ├── schemas/
│   │   │   └── ...
│   │   └── services/
│   │       └── ...
│   ├── tests/
│   ├── alembic/
│   └── Dockerfile
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── hooks/
│   │   ├── services/
│   │   ├── types/
│   │   └── main.tsx
│   ├── public/
│   ├── index.html
│   ├── package.json
│   └── vite.config.ts
├── docker-compose.yml
├── .github/
│   └── workflows/
│       ├── backend-ci.yml
│       └── frontend-ci.yml
└── README.md
```

## Features

- **Authentication**: JWT with HTTP-only cookies
- **Posts**: Create, read, update, delete with Markdown support
- **Comments**: Nested comment threads
- **Tags**: Categorize posts with tags
- **Search**: Full-text search across posts
- **Dark Mode**: Toggle between light/dark themes
- **Responsive**: Mobile-first design
- **Real-time**: WebSocket for live updates (optional)

## Tech Stack

### Backend
- FastAPI 0.104+
- PostgreSQL 15+
- SQLAlchemy 2.0+
- Alembic (migrations)
- Pytest (testing)

### Frontend
- React 18+
- TypeScript 5+
- Vite (build tool)
- React Router 6+
- React Query (data fetching)
- React Hook Form + Zod (forms)
- TailwindCSS (styling)

## Usage

```bash
# Start everything
docker-compose up -d

# Backend API
http://localhost:8000/docs

# Frontend
http://localhost:3000

# Run tests
cd backend && pytest
cd frontend && npm test
```
