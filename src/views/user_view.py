import streamlit as st
from src.services.database import DatabaseService

def user_registration():
    st.header("Register for the Queue")
    st.write("Join the virtual line to save your spot.")

    db = DatabaseService()
    
    with st.form("registration_form"):
        user_id = st.text_input("Enter your User ID (provided by organization)")
        submit = st.form_submit_button("Join Queue")

        if submit:
            if not user_id:
                st.error("User ID is required.")
            else:
                # T013/T014 integration
                entry = db.join_queue(user_id)
                if entry:
                    st.success(f"Successfully joined! Your position is {entry.get('position')}")
                    st.session_state.user_id = user_id
                    st.session_state.page = "User Status"
                    st.rerun()
                else:
                    st.error("Failed to join queue. Virtual line might be full or database is unavailable.")

from src.utils.calculations import calculate_wait_time

def user_status():
    st.header("Your Queue Status")
    
    if "user_id" not in st.session_state:
        st.warning("Please register first.")
        if st.button("Go to Registration"):
            st.session_state.page = "User Registration"
            st.rerun()
        return

    db = DatabaseService()
    user_id = st.session_state.user_id
    entry = db.get_queue_status(user_id)
    config = db.get_configuration()

    if not entry or entry["status"] != "waiting":
        st.info("You are not currently in the waiting queue.")
        if st.button("Register Again"):
            st.session_state.page = "User Registration"
            st.rerun()
        return

    st.subheader(f"User: {user_id}")
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Your Position", entry["position"])
    
    with col2:
        # T016 integration: calculate wait time
        exits = config.get("exits", 1)
        interaction_time = config.get("interaction_time", 5)
        
        # Position in line for wait time is entry["position"] - current_front_position
        # For simplicity, if positions are 1-based and sequential, and status='entered' rows are skipped.
        # Let's assume entry["position"] is their absolute position. 
        # We need to know how many people are in front of them with status 'waiting'.
        # Actually, simpler prototype logic: wait_time = (active_queue_length * interaction_time) / exits
        # But for specific user: wait_time = (position_in_waiting_list * interaction_time) / exits
        
        # Let's query active entries with position < current user's position
        response = db.supabase.table("queue_entries").select("*", count="exact").eq("status", "waiting").lt("position", entry["position"]).execute()
        people_in_front = response.count if response.count is not None else 0
        
        wait_time = calculate_wait_time(people_in_front, exits, interaction_time)
        st.metric("Est. Wait Time", f"{wait_time} mins")

    if st.button("Refresh Status"):
        st.rerun()
    
    # T018/T020 integration: Simulate QR Scan
    st.divider()
    if people_in_front == 0:
        st.success("It's your turn! Scan the QR code at the entrance.")
        if st.button("Simulate QR Scan", type="primary"):
            success = db.mark_entered(entry["id"])
            if success:
                st.success("Entry recorded! You are now in the physical queue.")
                st.rerun()
            else:
                st.error("Failed to record entry.")
    else:
        st.info(f"There are {people_in_front} people ahead of you.")
