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

# --- PAGE RENDERING ---
if selected == "🏠 Home":
    from pages import home
    home.app()
elif selected == "👨‍⚕️ Specialists":
    from pages import specialists
    specialists.app()
elif selected == "🗓️ Book Appointment":
    from pages import book_appointment
    book_appointment.app()
elif selected == "📑 My Appointments":
    from pages import my_appointments
    my_appointments.app()



