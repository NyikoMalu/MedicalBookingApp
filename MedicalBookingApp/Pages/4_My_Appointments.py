import streamlit as st

def app(client):
    st.title("📑 My Appointments")
    st.caption("View your booked appointments.")

    if client:
        try:
            query = """
                SELECT a.AppointmentID, p.FirstName, p.LastName, d.Date, t.Label AS TimeSlot
                FROM `medical-booking-system-473907.MedicalBookingDB.Appointments` a
                JOIN `medical-booking-system-473907.MedicalBookingDB.Patients` p
                ON a.PatientID = p.PatientID
                JOIN `medical-booking-system-473907.MedicalBookingDB.Dates` d
                ON a.DateKey = d.DateKey
                JOIN `medical-booking-system-473907.MedicalBookingDB.TimeSlots` t
                ON a.TimeSlotID = t.TimeSlotID
            """
            df = client.query(query).to_dataframe()
            if not df.empty:
                st.dataframe(df)
            else:
                st.info("ℹ️ No appointments found.")
        except Exception as e:
            st.error(f"❌ Error fetching appointments: {e}")




