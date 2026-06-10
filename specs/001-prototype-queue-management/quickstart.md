# Quickstart: Prototype Queue Management System

## Prerequisites
- Python 3.10+
- Supabase Account and Project
- `pip install streamlit supabase`

## Supabase Setup
1. Create a new project in Supabase.
2. Run the following SQL in the SQL Editor to create tables and enable security policies:
```sql
-- 1. Create Tables
CREATE TABLE IF NOT EXISTS configurations (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    entrances INTEGER NOT NULL DEFAULT 1,
    exits INTEGER NOT NULL DEFAULT 1,
    max_capacity INTEGER NOT NULL DEFAULT 50,
    interaction_time INTEGER NOT NULL DEFAULT 5,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS queue_entries (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id TEXT NOT NULL,
    position SERIAL,
    status TEXT NOT NULL DEFAULT 'waiting',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    entered_at TIMESTAMP WITH TIME ZONE
);

-- 2. Initial Data
INSERT INTO configurations (entrances, exits, max_capacity, interaction_time) 
SELECT 1, 1, 50, 5
WHERE NOT EXISTS (SELECT 1 FROM configurations);

-- 3. Enable Row-Level Security (RLS)
ALTER TABLE configurations ENABLE ROW LEVEL SECURITY;
ALTER TABLE queue_entries ENABLE ROW LEVEL SECURITY;

-- 4. Policies for 'configurations'
CREATE POLICY "Allow public read access" ON configurations FOR SELECT TO anon USING (true);
CREATE POLICY "Allow public update access" ON configurations FOR UPDATE TO anon USING (true) WITH CHECK (true);

-- 5. Policies for 'queue_entries'
CREATE POLICY "Allow public insert access" ON queue_entries FOR INSERT TO anon WITH CHECK (true);
CREATE POLICY "Allow public read access" ON queue_entries FOR SELECT TO anon USING (true);
CREATE POLICY "Allow public update access" ON queue_entries FOR UPDATE TO anon USING (true) WITH CHECK (true);
```

## Running the App
1. Set environment variables:
   ```bash
   export SUPABASE_URL="your-url"
   export SUPABASE_KEY="your-anon-key"
   ```
2. Run Streamlit:
   ```bash
   streamlit run app.py
   ```

## Development Workflow
- **Admin**: Access the sidebar or `/admin` route to configure settings.
- **User**: Enter `user_id` on the main page to join or view status.
- **Simulator**: Use the "Scan QR" button to simulate entry when position is 1.
