import streamlit as st
import pandas as pd

def app(client):
    st.title("🗓️ Book Appointment")
    st.caption("Select a specialist and choose an available date/time.")

    if client:
        try:
            # Fetch specialists
            specialists_query = """
                SELECT SpecialistID, FirstName, LastName, Specialty
                FROM `medical-booking-system-473907.MedicalBookingDB.Specialists`
            """
            specialists = client.query(specialists_query).to_dataframe()
            
            selected_specialist = st.selectbox(
                "Select Specialist",
                specialists['FirstName'] + " " + specialists['LastName'] + " (" + specialists['Specialty'] + ")"
            )

            # Fetch available dates
            dates_query = "SELECT DateKey, Date FROM `medical-booking-system-473907.MedicalBookingDB.Dates` ORDER BY Date"
            dates = client.query(dates_query).to_dataframe()
            selected_date = st.selectbox("Select Date", dates['Date'])

            # Time slots
            times_query = "SELECT TimeSlotID, Label FROM `medical-booking-system-473907.MedicalBookingDB.TimeSlots`"
            times = client.query(times_query).to_dataframe()
            selected_time = st.selectbox("Select Time Slot", times['Label'])

            if st.button("Book Appointment"):
                st.success(f"✅ Appointment booked with {selected_specialist} on {selected_date} at {selected_time}")
        except Exception as e:
            st.error(f"❌ Error fetching booking info: {e}")
