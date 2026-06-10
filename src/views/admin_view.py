import streamlit as st
from src.services.database import DatabaseService

def admin_dashboard():
    st.header("Admin Configuration")
    st.write("Manage physical queue constraints and service parameters.")

    db = DatabaseService()
    config = db.get_configuration()

    if not config:
        st.error("No configuration found in database. Please initialize the 'configurations' table.")
        return

    with st.form("config_form"):
        st.subheader("Physical Constraints")
        entrances = st.number_input("Number of Entrances", min_value=1, value=config.get("entrances", 1))
        exits = st.number_input("Number of Exits (Service Points)", min_value=1, value=config.get("exits", 1))
        max_capacity = st.number_input("Maximum Virtual Queue Capacity", min_value=1, value=config.get("max_capacity", 50))
        
        st.subheader("Service Parameters")
        interaction_time = st.number_input("Estimated Interaction Time (minutes per person)", min_value=1, value=config.get("interaction_time", 5))
        
        submit = st.form_submit_state = st.form_submit_button("Save Configuration")

        if submit:
            # Validation (T011)
            if entrances <= 0 or exits <= 0 or max_capacity <= 0 or interaction_time <= 0:
                st.error("All values must be greater than zero.")
            else:
                success = db.update_configuration(entrances, exits, max_capacity, interaction_time)
                if success:
                    st.success("Configuration updated successfully!")
                    st.rerun()
                else:
                    st.error("Failed to update configuration.")

    st.divider()
    st.subheader("Current Settings")
    st.json(config)
