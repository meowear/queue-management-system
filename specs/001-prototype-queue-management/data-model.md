# Data Model: Prototype Queue Management System

## Entities

### Configuration
Store the global settings for the queue management system.

| Field | Type | Description |
| :--- | :--- | :--- |
| `id` | UUID | Primary Key |
| `entrances` | Integer | Number of physical entrances |
| `exits` | Integer | Number of service points (exits) |
| `max_capacity` | Integer | Maximum number of people allowed in virtual queue |
| `interaction_time` | Integer | Estimated minutes per person |
| `updated_at` | Timestamp | Last modified date |

### QueueEntry
Tracks individuals in the queue.

| Field | Type | Description |
| :--- | :--- | :--- |
| `id` | UUID | Primary Key |
| `user_id` | String | Organization-provided ID |
| `position` | Integer | Sequential position in line |
| `status` | Enum | `waiting`, `entered`, `exited` |
| `created_at` | Timestamp | When they joined the virtual queue |
| `entered_at` | Timestamp | When they scanned to enter physical queue |

## Relationships
- A single **Configuration** record governs all **QueueEntry** logic.
- **QueueEntry** records are processed sequentially based on `position`.

## Validation Rules
- `entrances`, `exits`, `max_capacity`, `interaction_time` must be > 0.
- `user_id` must not be empty.
- `position` is auto-incremented per registration.
