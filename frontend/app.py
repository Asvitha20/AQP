import streamlit as st

st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Predict AQI", "About AQI"])

if page == "Predict AQI":
    import pages.predict

elif page == "About AQI":
    import pages.about