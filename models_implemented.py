import streamlit as st

def display():
    st.title("Models Implemented")
    st.write("""
    In this section, we present the three main objectives for which models were implemented. 
    """)

    # Buttons for navigation
    if st.button("Highest Tidal Level Prediction"):
        st.session_state["page"] = "highest_tidal_level"
        st.rerun()

    if st.button("Mean Sea Level Prediction"):
        st.session_state["page"] = "mean_sea_level"
        st.rerun()

    if st.button("Seasonal & Temporal Analysis"):
        st.session_state["page"] = "seasonal_temporal_analysis"
        st.rerun()