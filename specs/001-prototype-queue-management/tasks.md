---

description: "Task list for Prototype Queue Management System implementation"
---

# Tasks: Prototype Queue Management System

**Input**: Design documents from `/specs/001-prototype-queue-management/`

**Prerequisites**: plan.md (required), spec.md (required), research.md, data-model.md, contracts/

**Tests**: Tests are MANDATORY for all core components as per the project constitution. TDD principles must be followed for wait time calculations.

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [X] T001 Create project structure: src/views, src/services, src/utils, tests/unit, tests/integration
- [X] T002 Initialize Python project with dependencies: streamlit, supabase in requirements.txt
- [X] T003 Configure environment variable management in src/config.py
- [X] T004 Create main entry point src/app.py with basic routing

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure and logic that MUST be complete before ANY user story

- [X] T005 [P] Implement wait time calculation logic in src/utils/calculations.py
- [X] T006 [P] Write unit tests for wait time calculations in tests/unit/test_calculations.py (TDD: Write first, ensure fail)
- [X] T007 [P] Implement Supabase integration service in src/services/database.py per contract
- [X] T008 [P] Write integration tests for database service in tests/integration/test_database.py

**Checkpoint**: Foundation ready - wait time logic verified and database connection established.

---

## Phase 3: User Story 1 - Admin Configuration (Priority: P1) 🎯 MVP

**Goal**: Allow admin to set queue constraints (entrances, exits, capacity, interaction time)

**Independent Test**: Admin can save settings in Streamlit and verify they persist in Supabase.

- [X] T009 [US1] Create admin configuration dashboard in src/views/admin_view.py
- [X] T010 [US1] Integrate admin dashboard with database service in src/views/admin_view.py
- [X] T011 [US1] Add validation for configuration inputs (must be > 0) in src/views/admin_view.py

**Checkpoint**: US1 complete - system is configurable.

---

## Phase 4: User Story 2 - User Registration (Priority: P1) 🎯 MVP

**Goal**: Allow users to register for the queue with a `user_id`

**Independent Test**: User registers and receives a sequential position saved in Supabase.

- [X] T012 [US2] Create user registration interface in src/views/user_view.py
- [X] T013 [US2] Implement queue joining logic in src/services/database.py (join_queue)
- [X] T014 [US2] Integrate registration interface with database service in src/views/user_view.py

**Checkpoint**: US2 complete - users can join the virtual queue.

---

## Phase 5: User Story 3 - Wait Time Estimation (Priority: P2)

**Goal**: Show users their current position and estimated wait time

**Independent Test**: UI reflects correct wait time using parallel service formula.

- [X] T015 [US3] Implement status dashboard for registered users in src/views/user_view.py
- [X] T016 [US3] Integrate status dashboard with wait time calculation utility in src/views/user_view.py
- [X] T017 [US3] Add real-time update trigger for position/wait time in src/views/user_view.py

**Checkpoint**: US3 complete - users receive live feedback on their status.

---

## Phase 6: User Story 4 - Entry Placeholder (Priority: P3)

**Goal**: Simulate QR code scan for queue entry

**Independent Test**: Clicking "Scan QR" button updates status to 'entered' and reflects in queue length.

- [X] T018 [US4] Add "Simulate QR Scan" button to user status dashboard in src/views/user_view.py
- [X] T019 [US4] Implement status update logic in src/services/database.py (mark_entered)
- [X] T020 [US4] Integrate simulation button with status update logic in src/views/user_view.py

**Checkpoint**: US4 complete - full prototype lifecycle demonstrable.

---

## Phase N: Polish & Cross-Cutting Concerns

- [X] T021 Generate project README.md with setup and usage instructions
- [X] T022 Final cross-view navigation and styling cleanup in src/app.py
- [X] T023 Verify all requirements from spec.md are met and test cases pass

---

## Dependencies & Execution Order

### Phase Dependencies
- Phase 1 (Setup) -> Phase 2 (Foundational)
- Phase 2 (Foundational) -> Phase 3 (US1) & Phase 4 (US2)
- Phase 3 (US1) & Phase 4 (US2) -> Phase 5 (US3)
- Phase 5 (US3) -> Phase 6 (US4)

### Parallel Opportunities
- Foundational tasks T005, T006, T007, T008 can run in parallel.
- Admin dashboard (Phase 3) and User registration (Phase 4) can run in parallel once Foundation is ready.

---

## Implementation Strategy

### MVP First (User Story 1 & 2)
1. Complete Setup and Foundational phases.
2. Implement Admin Configuration (US1).
3. Implement User Registration (US2).
4. **STOP and VALIDATE**: Verify a user can be added and settings are persisted.

### Incremental Delivery
- Add US3 (Wait Time) to provide user feedback.
- Add US4 (QR Simulation) to complete the prototype lifecycle.
- Finish with README.md for documentation.
