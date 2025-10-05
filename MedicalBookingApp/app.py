import streamlit as st
from streamlit_option_menu import option_menu

# --- SIDEBAR MENU ---
with st.sidebar:
    selected = option_menu(
        "📋 Navigation",
        ["🏠 Home", "👨‍⚕️ Specialists", "🗓️ Book Appointment", "📑 My Appointments"],
        icons=["house", "person-badge", "calendar-plus", "journal-text"],
        menu_icon="cast",
        default_index=0,
    )

# --- Import pages based on selection ---
if selected == "🏠 Home":
    from Pages import _1_Home as home
    home.app()
elif selected == "👨‍⚕️ Specialists":
    from Pages import _2_Specialists as specialists
    specialists.app()
elif selected == "🗓️ Book Appointment":
    from Pages import _3_Book_Appointment as book
    book.app()
elif selected == "📑 My Appointments":
    from Pages import _4_My_Appointments as my_appointments
    my_appointments.app()




