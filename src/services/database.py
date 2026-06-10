import os
from supabase import create_client, Client
from src.config import SUPABASE_URL, SUPABASE_KEY

class DatabaseService:
    def __init__(self):
        self.supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

    def get_configuration(self):
        """Retrieves the current queue settings."""
        response = self.supabase.table("configurations").select("*").limit(1).execute()
        if response.data:
            return response.data[0]
        return None

    def update_configuration(self, entrances: int, exits: int, max_capacity: int, interaction_time: int):
        """Updates settings in the database."""
        # For simplicity in this prototype, we assume there's only one config row
        # We can update the row with ID if known, or just update all if it's the only one.
        config = self.get_configuration()
        if config:
            response = self.supabase.table("configurations").update({
                "entrances": entrances,
                "exits": exits,
                "max_capacity": max_capacity,
                "interaction_time": interaction_time,
                "updated_at": "now()"
            }).eq("id", config["id"]).execute()
            return response.data
        return None

    def join_queue(self, user_id: str):
        """Registers a user for the queue."""
        # Position is handled by SERIAL in SQL, but let's check current count for UI convenience if needed
        # Or just let Supabase handle it.
        response = self.supabase.table("queue_entries").insert({
            "user_id": user_id,
            "status": "waiting"
        }).execute()
        return response.data[0] if response.data else None

    def get_queue_status(self, user_id: str):
        """Returns the current status and position for a user."""
        response = self.supabase.table("queue_entries").select("*").eq("user_id", user_id).order("created_at", desc=True).limit(1).execute()
        return response.data[0] if response.data else None

    def mark_entered(self, entry_id: str):
        """Marks a user as having entered the physical queue."""
        response = self.supabase.table("queue_entries").update({
            "status": "entered",
            "entered_at": "now()"
        }).eq("id", entry_id).execute()
        return response.data

    def get_active_queue_length(self):
        """Returns the count of users with status 'waiting'."""
        response = self.supabase.table("queue_entries").select("*", count="exact").eq("status", "waiting").execute()
        return response.count
