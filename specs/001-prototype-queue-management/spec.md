# Feature Specification: Prototype Queue Management System

**Feature Branch**: `001-prototype-queue-management`

**Created**: 2026-06-10

**Status**: Implemented

**Input**: User description: "i want to make a queue management system. to tackle the issue of unorganised queues. it will ask the admin to specify the number of entrances number of exits the maximum people capacity in every queue and it will tell the users to register for any line through a user_id provided by the organisation, connect this to a db a supabase db, and it will tell people to scan a qr at the queue entrance to enter the queue, and it will also tell estimated time for them to be able to join the physical queue, based on estimated interaction time as specified by admin, make the tech stack streamlit, and backend node js or python backend.. make a basic prototype for now, don't implement the qr code scanner for now just let it be a template, generate README.md also for this"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Admin Configuration (Priority: P1)

As an administrator, I want to configure the queue parameters so that the system can manage people flow according to physical constraints.

**Why this priority**: Core setup required for any queue logic.

**Independent Test**: Verify that configuration (entrances, exits, capacity, interaction time) is saved to the database and can be retrieved.

**Acceptance Scenarios**:

1. **Given** an authenticated admin, **When** they enter 2 entrances, 1 exit, 50 capacity, and 5-minute interaction time, **Then** the configuration is persisted in Supabase.
2. **Given** existing configuration, **When** the admin updates the interaction time to 10 minutes, **Then** the system recalculates estimated wait times for all pending users.

---

### User Story 2 - User Registration (Priority: P1)

As an organization member, I want to register for a queue using my ID so that I can secure my spot without standing in a physical line.

**Why this priority**: Primary value proposition for users to avoid unorganized queues.

**Independent Test**: Verify that a user with a valid `user_id` can join a queue and receives a unique position.

**Acceptance Scenarios**:

1. **Given** a valid organization `user_id`, **When** the user joins the queue, **Then** they are assigned a sequential position.
2. **Given** a user already in a queue, **When** they try to join again, **Then** the system notifies them of their current position instead of creating a duplicate.

---

### User Story 3 - Wait Time Estimation (Priority: P2)

As a registered user, I want to see an estimated time to join the physical queue so that I can manage my time effectively.

**Why this priority**: Essential for the "organized" aspect of the system.

**Independent Test**: Verify that the estimated time updates as people enter/exit the queue.

**Acceptance Scenarios**:

1. **Given** a user at position 10 and a 5-minute interaction time per person, **When** they check their status, **Then** they see an estimated wait time of 50 minutes (if only 1 exit/service point).

---

### User Story 4 - Entry Placeholder (Priority: P3)

As a user at the front of the virtual queue, I want a placeholder for "scanning a QR" so that the prototype demonstrates the intended entry flow.

**Why this priority**: Demonstrates the full lifecycle for the prototype.

**Independent Test**: Verify that a "Scan QR" button simulation transitions the user state from "waiting" to "active".

**Acceptance Scenarios**:

1. **Given** a user whose turn has arrived, **When** they click the "Simulate QR Scan" button, **Then** their status changes to "entered" and a spot opens up in the virtual queue for others.

### Edge Cases

- **Queue at Capacity**: What happens when the virtual queue reaches the maximum people capacity specified by the admin? (Assumption: System stops accepting new registrations).
- **Multiple Entrances/Exits**: The number of exits acts as parallel service points. Wait time is calculated by dividing position by number of exits and multiplying by interaction time.
- **Invalid User ID**: For the prototype, any non-empty string provided by the organization is accepted as a valid `user_id`.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: Admin dashboard for setting number of entrances, exits, max capacity, and interaction time.
- **FR-002**: User registration interface accepting a `user_id`.
- **FR-003**: Integration with Supabase for persisting configuration and queue state.
- **FR-004**: Real-time calculation of estimated wait time: `(Position / Service Points) * Interaction Time`.
- **FR-005**: Status dashboard for users showing current position and estimated wait time.
- **FR-006**: Simulation button for QR entry that updates user status in the database.

### Key Entities

- **QueueConfiguration**: Entrances, exits, max_capacity, interaction_time_per_person.
- **QueueEntry**: User_id, position, status (waiting/entered/exited), registration_timestamp, entry_timestamp.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Users can register for a queue in under 30 seconds.
- **SC-002**: Estimated wait time is updated within 5 seconds of any state change in the queue.
- **SC-003**: Admin can update configuration and see it reflected immediately in new wait time calculations.
- **SC-004**: System handles up to the maximum specified capacity without data corruption.

## Assumptions

- **Tech Stack**: Frontend is Streamlit; Backend/Logic is Python; Database is Supabase.
- **User Identification**: `user_id` is the primary key for users; no complex auth for prototype.
- **Single Queue**: Prototype handles a single queue per instance.
- **Service Rate**: The number of "exits" specified by the admin acts as the number of parallel service points for wait time calculation.
