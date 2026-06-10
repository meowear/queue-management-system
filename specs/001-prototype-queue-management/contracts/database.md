# Database Contract: Prototype Queue Management System

## Overview
The system relies on Supabase for persistence. All interactions with the database must go through a centralized service to ensure consistency.

## Interfaces

### `get_configuration() -> Configuration`
Retrieves the current queue settings.

### `update_configuration(config: Configuration)`
Updates settings and triggers wait time recalculations in the UI.

### `join_queue(user_id: string) -> QueueEntry`
- Assigns the next available position.
- Returns the entry details including current position.

### `get_queue_status(user_id: string) -> QueueEntry`
Returns the current status and position for a user.

### `mark_entered(entry_id: UUID)`
- Sets status to `entered`.
- Updates `entered_at` timestamp.

### `get_active_queue_length() -> Integer`
Returns the count of users with status `waiting`.

## Real-time Events
The database service must expose a way to subscribe to:
- **Queue Changes**: Triggered when anyone joins or enters.
- **Config Changes**: Triggered when admin updates settings.
