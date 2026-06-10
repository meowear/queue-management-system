# Implementation Plan: Prototype Queue Management System

**Branch**: `001-prototype-queue-management` | **Date**: 2026-06-10 | **Spec**: [specs/001-prototype-queue-management/spec.md](specs/001-prototype-queue-management/spec.md)

**Input**: Feature specification from `/specs/001-prototype-queue-management/spec.md`

**Note**: This template is filled in by the `/speckit.plan` command. See `.specify/templates/plan-template.md` for the execution workflow.

## Summary
The goal is to implement a basic Queue Management System prototype using Streamlit and Supabase. The system allows an admin to configure physical queue constraints (entrances, exits, capacity) and interaction times. Users can register with a `user_id`, view their position in line, and receive an estimated wait time based on parallel service points (exits). A "Scan QR" simulation button handles transitions from virtual to physical queue.

## Technical Context

**Language/Version**: Python 3.10+

**Primary Dependencies**: Streamlit, Supabase-py, Pandas (optional for data display)

**Storage**: Supabase (PostgreSQL)

**Testing**: pytest

**Target Platform**: Web (Streamlit Cloud or any Python-capable server)

**Project Type**: Prototype/Web-service

**Performance Goals**: Support up to 1000 concurrent virtual queue entries; real-time updates within 5 seconds.

**Constraints**: "Scan QR" is a simulation button; template-based approach for non-functional components.

**Scale/Scope**: Single queue instance for prototype.

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- [x] **Modular Architecture**: The system is decomposed into Views (Streamlit), Services (Supabase interactions), and Logic (Wait time calculations).
- [x] **Security First**: SUPABASE_URL and SUPABASE_KEY managed via environment variables; non-empty `user_id` validation.
- [x] **Scalable Architecture**: Stateless frontend and distributed Supabase backend ensure basic horizontal scalability.
- [x] **Test-Driven Development**: Research tasks and Phase 2 tasks include pytest setup for core calculation logic.

## Project Structure

### Documentation (this feature)

```text
specs/001-prototype-queue-management/
├── plan.md              # This file
├── research.md          # Technical decisions and research tasks
├── data-model.md        # Supabase schema and entity definitions
├── quickstart.md        # Setup and running instructions
├── contracts/           
│   └── database.md      # Database service interface contract
└── tasks.md             # To be created by /speckit.tasks
```

### Source Code (repository root)

```text
src/
├── app.py               # Main Streamlit entry point
├── views/
│   ├── admin_view.py    # Admin configuration dashboard
│   └── user_view.py     # User registration and status dashboard
├── services/
│   └── database.py      # Supabase integration layer
├── utils/
│   └── calculations.py  # Wait time estimation logic
└── config.py            # Environment variable management

tests/
├── unit/
│   └── test_calculations.py
└── integration/
    └── test_database.py
```

**Structure Decision**: Option 1 (Single Project) - Best for a Streamlit prototype where all components reside in the same repository.

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
| :--- | :--- | :--- |
| None | N/A | N/A |
