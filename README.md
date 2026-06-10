# Queue Management System (Prototype)

A modular, scalable, and secure system to tackle unorganized physical queues. Built with Streamlit and Supabase.

## Features

- **Admin Dashboard**: Configure entrances, exits, capacity, and service interaction times.
- **User Registration**: Secure a spot in the virtual line using an organization-provided User ID.
- **Real-time Wait Time**: Get estimated wait times based on your position and available service points (parallel service).
- **Entry Simulation**: Demonstrates the virtual-to-physical transition with a simulated QR scan button.

## Tech Stack

- **Frontend**: [Streamlit](https://streamlit.io/)
- **Backend Logic**: Python 3.10+
- **Database**: [Supabase](https://supabase.com/) (PostgreSQL + Real-time)

## Setup Instructions

### 1. Database Setup (Supabase)

Create the following tables in your Supabase project:

```sql
CREATE TABLE configurations (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    entrances INTEGER NOT NULL DEFAULT 1,
    exits INTEGER NOT NULL DEFAULT 1,
    max_capacity INTEGER NOT NULL DEFAULT 50,
    interaction_time INTEGER NOT NULL DEFAULT 5,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE TABLE queue_entries (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id TEXT NOT NULL,
    position SERIAL,
    status TEXT NOT NULL DEFAULT 'waiting',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    entered_at TIMESTAMP WITH TIME ZONE
);

INSERT INTO configurations (entrances, exits, max_capacity, interaction_time) VALUES (1, 1, 50, 5);
```

### 2. Environment Variables

Create a `.env` file in the project root:

```env
SUPABASE_URL="your-project-url"
SUPABASE_KEY="your-anon-key"
```

### 3. Installation

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 4. Running the Application

```bash
streamlit run main.py
```

### 5. Row Level Security (RLS) Setup

To allow the prototype to function without full Supabase Authentication, run the following SQL. This allows the `anon` role to manage entries.

```sql
-- 1. Enable RLS on tables
ALTER TABLE configurations ENABLE ROW LEVEL SECURITY;
ALTER TABLE queue_entries ENABLE ROW LEVEL SECURITY;

-- 2. Define Policies for 'configurations'
CREATE POLICY "Public read access for configurations" ON configurations FOR SELECT TO anon USING (true);
CREATE POLICY "Public update access for configurations" ON configurations FOR UPDATE TO anon USING (true) WITH CHECK (true);

-- 3. Define Policies for 'queue_entries'
CREATE POLICY "Public insert access for queue_entries" ON queue_entries FOR INSERT TO anon WITH CHECK (true);
CREATE POLICY "Public read access for queue_entries" ON queue_entries FOR SELECT TO anon USING (true);
CREATE POLICY "Public update access for queue_entries" ON queue_entries FOR UPDATE TO anon USING (true) WITH CHECK (true);
```

## Governance & Principles

This project follows the **Queue Management System Constitution (v0.1.0)**:
- **Modular Architecture**: Independent views and services.
- **Security First**: Environment-based secret management.
- **Scalable Architecture**: Horizontal scale via stateless frontend.
- **Test-Driven Development**: Core calculations verified by unit tests.
# queue-management-system
