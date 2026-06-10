import streamlit as st
from src.views.admin_view import admin_dashboard
from src.views.user_view import user_registration, user_status

st.set_page_config(page_title="Queue Management System", layout="wide")

def main():
    st.title("Queue Management System")
    
    # Basic routing logic using query params or session state
    if "page" not in st.session_state:
        st.session_state.page = "User Registration"

    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["User Registration", "User Status", "Admin Dashboard"], 
                            index=["User Registration", "User Status", "Admin Dashboard"].index(st.session_state.page))
    st.session_state.page = page

    # Sample Credentials for Testing (T022)
    st.sidebar.divider()
    with st.sidebar.expander("🛠️ Testing Credentials (RLS)", expanded=False):
        st.write("**Admin IDs:**")
        st.code("admin_demo_1\nadmin_demo_2")
        st.write("**User IDs:**")
        st.code("user_demo_1\nuser_demo_2\nuser_demo_3")
        st.info("Use these IDs in the registration/login fields to test RLS policies.")

    if st.session_state.page == "User Registration":
        user_registration()
        
    elif st.session_state.page == "User Status":
        user_status()
        
    elif st.session_state.page == "Admin Dashboard":
        admin_dashboard()

if __name__ == "__main__":
    main()
