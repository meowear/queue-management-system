import os
from dotenv import load_dotenv

# Load environment variables from .env file if it exists
load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

if not SUPABASE_URL or not SUPABASE_KEY:
    # In a real app, we might want to raise an error, but for a prototype 
    # we'll just warn and rely on Streamlit secrets or direct env vars.
    print("Warning: SUPABASE_URL or SUPABASE_KEY not found in environment.")
