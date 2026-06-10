# Research: Prototype Queue Management System

## Technical Decisions

### Decision 1: Backend Implementation
- **Decision**: Python (FastAPI or pure Streamlit logic)
- **Rationale**: User requested Python backend. For a Streamlit prototype, keeping logic within Python modules is idiomatic and simplifies deployment.
- **Alternatives considered**: Node.js (also requested, but Python is more native to Streamlit).

### Decision 2: Wait Time Calculation with Parallel Exits
- **Decision**: Parallel Service Formula: `Wait Time = (Position / Number of Exits) * Interaction Time`.
- **Rationale**: This is the standard queuing theory approach for parallel service points. It accurately reflects that multiple people can be served simultaneously.
- **Alternatives considered**: Sequential service (too conservative), fixed buffer (too simplistic).

### Decision 3: User ID Validation
- **Decision**: Open Entry for Prototype.
- **Rationale**: User requested a "basic prototype". Restricting entry might block testing. Any non-empty string provided by the organization will be accepted initially.
- **Alternatives considered**: Pre-validation (too much overhead for v1), Domain check (good for later).

### Decision 4: Database Integration
- **Decision**: Supabase (PostgreSQL + PostgREST).
- **Rationale**: User explicitly requested Supabase. It provides real-time capabilities which are perfect for queue updates.
- **Alternatives considered**: SQLite (local only), Firebase (NoSQL).

## Research Tasks

- **Supabase Real-time**: Investigate how to use Supabase real-time subscriptions with Streamlit to update the queue status without page refreshes.
- **Streamlit Session State**: Best practices for managing user registration state and admin settings across sessions.
- **Modular Structure**: Define clear boundaries between `admin_view.py`, `user_view.py`, and `database_service.py`.
