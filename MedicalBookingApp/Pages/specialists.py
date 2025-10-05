import streamlit as st
import pandas as pd
import plotly.express as px

def app():
    st.title("👨‍⚕️ Specialists")
    st.markdown("Browse all available specialists.")

    # Sample specialists data
    data = {
        "Specialist": ["Dr. Smith", "Dr. Johnson", "Dr. Lee", "Dr. Patel", "Dr. Kim"],
        "Specialty": ["Cardiology", "Dermatology", "Neurology", "Pediatrics", "Orthopedics"],
        "Experience (yrs)": [10, 7, 15, 5, 12]
    }
    df = pd.DataFrame(data)

    st.table(df)

    # Top specialties chart
    st.subheader("🏆 Specialists by Specialty")
    specialty_count = df["Specialty"].value_counts().reset_index()
    specialty_count.columns = ["Specialty", "Count"]
    fig = px.bar(specialty_count, x="Specialty", y="Count", 
                 color="Specialty", text="Count",
                 color_discrete_sequence=px.colors.qualitative.Bold)
    fig.update_traces(textposition="outside")
    st.plotly_chart(fig, use_container_width=True)





