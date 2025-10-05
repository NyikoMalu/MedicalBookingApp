import streamlit as st
import pandas as pd
import plotly.express as px

def app():
    st.title("🏥 Medical Booking System")
    st.markdown("Welcome to your one-stop platform for booking medical specialists!")

    # --- METRICS ---
    col1, col2, col3 = st.columns(3)
    col1.metric("👨‍⚕️ Specialists", "50+", delta="Available")
    col2.metric("🗓️ Appointments", "200+", delta="This Month")
    col3.metric("😊 Patients", "100+", delta="Active Users")
    
    st.divider()

    # --- APPOINTMENTS TREND CHART ---
    df = pd.DataFrame({
        "Date": pd.date_range(start="2025-10-01", periods=7),
        "Appointments": [5, 10, 8, 12, 15, 7, 9]
    })

    st.subheader("📈 Appointments Over Time")
    fig = px.line(df, x="Date", y="Appointments", markers=True, 
                  title="Appointments Trend", 
                  color_discrete_sequence=["#2E86DE"])
    st.plotly_chart(fig, use_container_width=True)




