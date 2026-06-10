-- Full Setup Script for Prototype Queue Management System

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

-- 3. Enable Row-Level Security
ALTER TABLE configurations ENABLE ROW LEVEL SECURITY;
ALTER TABLE queue_entries ENABLE ROW LEVEL SECURITY;

-- 4. Policies for 'configurations'
-- Allow everyone to read settings
CREATE POLICY "Allow public read access" ON configurations
    FOR SELECT TO anon USING (true);

-- Allow everyone to update settings (for prototype purposes)
CREATE POLICY "Allow public update access" ON configurations
    FOR UPDATE TO anon USING (true) WITH CHECK (true);

-- 5. Policies for 'queue_entries'
-- Allow users to join the queue
CREATE POLICY "Allow public insert access" ON queue_entries
    FOR INSERT TO anon WITH CHECK (true);

-- Allow users to view queue status
CREATE POLICY "Allow public read access" ON queue_entries
    FOR SELECT TO anon USING (true);

-- Allow users to update their status (for 'Scan QR' simulation)
CREATE POLICY "Allow public update access" ON queue_entries
    FOR UPDATE TO anon USING (true) WITH CHECK (true);
