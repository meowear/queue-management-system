import os
import sys
from supabase import create_client
from dotenv import load_dotenv

def test_supabase_connection():
    load_dotenv()
    url = os.getenv("SUPABASE_URL")
    key = os.getenv("SUPABASE_KEY")

    if not url or not key:
        print("x Error: SUPABASE_URL or SUPABASE_KEY not found in environment.")
        return

    print(f"Connecting to: {url}")
    try:
        supabase = create_client(url, key)

        # Try to read configurations
        print("Testing SELECT on 'configurations'...")
        res = supabase.table("configurations").select("*").limit(1).execute()
        print("v SELECT successful.")
        
        # Try to insert a test entry
        print("Testing INSERT on 'queue_entries'...")
        res = supabase.table("queue_entries").insert({
            "user_id": "debug_user_123",
            "status": "waiting"
        }).execute()
        print("v INSERT successful! RLS is correctly configured.")
        
        # Clean up
        if res.data:
            supabase.table("queue_entries").delete().eq("user_id", "debug_user_123").execute()
            print("v Cleanup successful.")

    except Exception as e:
        print("\nCONNECTION TEST FAILED")
        print(f"Error details: {e}")
        
        if "42501" in str(e) or "row-level security" in str(e).lower():
            print("\nDIAGNOSIS: Row-Level Security (RLS) is blocking the INSERT.")
            print("The policies in your README.md expect a JWT 'sub' claim that the app is not sending.")
            print("\nFIX: Run this in your Supabase SQL Editor:")
            print("ALTER TABLE queue_entries DISABLE ROW LEVEL SECURITY;")
            print("ALTER TABLE configurations DISABLE ROW LEVEL SECURITY;")
            print("-- OR (Better) --")
            print("CREATE POLICY \"Allow anon insert\" ON queue_entries FOR INSERT TO anon WITH CHECK (true);")

if __name__ == "__main__":
    test_supabase_connection()
