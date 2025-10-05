import streamlit as st
import pandas as pd

def app():
    st.title("📑 My Appointments")
    st.markdown("Track your booked appointments here.")

    # Sample booked appointments
    data = {
        "Name": ["Alice", "Bob", "Charlie"],
        "Specialist": ["Dr. Smith", "Dr. Patel", "Dr. Lee"],
        "Specialty": ["Cardiology", "Pediatrics", "Neurology"],
        "Date": ["2025-10-06", "2025-10-08", "2025-10-10"]
    }
    df = pd.DataFrame(data)

    st.table(df)






