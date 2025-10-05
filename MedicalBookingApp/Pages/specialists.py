import streamlit as st
import plotly.express as px

def app(client):
    st.title("👨‍⚕️ Specialists")
    st.caption("Browse available medical specialists and their ratings.")

    if client:
        try:
            query = """
                SELECT FirstName, LastName, Specialty, Rating
                FROM `medical-booking-system-473907.MedicalBookingDB.Specialists`
                ORDER BY Rating DESC
            """
            df = client.query(query).to_dataframe()
            if not df.empty:
                st.subheader("Top Rated Specialists")
                st.dataframe(df)

                fig = px.bar(df, x="FirstName", y="Rating", color="Specialty", text="Rating",
                             title="Specialist Ratings", color_discrete_sequence=px.colors.qualitative.Bold)
                fig.update_traces(textposition="outside")
                st.plotly_chart(fig, use_container_width=True)
        except Exception as e:
            st.error(f"❌ Error fetching specialists: {e}")



