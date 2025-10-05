import streamlit as st
import plotly.express as px
import pandas as pd

def app():
    st.title("🏥 Medical Booking System")
    st.write("Welcome to the Medical Booking System!")
    
    # Example metrics
    col1, col2, col3 = st.columns(3)
    col1.metric("👨‍⚕️ Specialists", "50+")
    col2.metric("🗓️ Appointments", "200+")
    col3.metric("😊 Patients", "100+")

    # Example chart
    df = pd.DataFrame({
        "Date": pd.date_range(start="2025-10-01", periods=7),
        "Appointments": [5, 10, 8, 12, 15, 7, 9]
    })

    fig = px.line(df, x="Date", y="Appointments", title="Appointments Over Time", markers=True)
    st.plotly_chart(fig, use_container_width=True)


