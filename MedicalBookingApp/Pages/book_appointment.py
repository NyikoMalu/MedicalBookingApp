import streamlit as st

def app():
    st.title("🗓️ Book Appointment")
    st.markdown("Schedule a visit with a specialist.")

    # --- Booking Form ---
    with st.form("appointment_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Email")
        specialty = st.selectbox("Select Specialty", ["Cardiology", "Dermatology", "Neurology", "Pediatrics", "Orthopedics"])
        date = st.date_input("Choose Date")
        submit = st.form_submit_button("Book Appointment")

        if submit:
            st.success(f"✅ Appointment booked for {name} with {specialty} on {date}")


