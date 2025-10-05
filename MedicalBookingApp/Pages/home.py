import streamlit as st
import plotly.express as px

def app(client):
    st.title("🏥 Medical Booking System")
    st.caption("Your one-stop platform for booking medical specialists.")

    # --- Metrics ---
    col1, col2, col3 = st.columns(3)
    col1.metric("👨‍⚕️ Specialists", "50+", "Available")
    col2.metric("🗓️ Appointments", "200+", "This Month")
    col3.metric("😊 Patients", "100+", "Active Users")

    st.divider()

    # --- Appointments Trend ---
    if client:
        try:
            query = """
                SELECT d.Date AS appointment_date, COUNT(a.AppointmentID) AS total
                FROM `medical-booking-system-473907.MedicalBookingDB.Appointments` a
                JOIN `medical-booking-system-473907.MedicalBookingDB.Dates` d
                ON a.DateKey = d.DateKey
                GROUP BY d.Date
                ORDER BY d.Date
            """
            df = client.query(query).to_dataframe()
            if not df.empty:
                st.subheader("📈 Appointments Over Time")
                fig = px.line(df, x="appointment_date", y="total", markers=True,
                              title="Appointments Over Time", color_discrete_sequence=["#2E86DE"])
                st.plotly_chart(fig, use_container_width=True)
        except Exception as e:
            st.error(f"❌ Error fetching appointments trend: {e}")

