import streamlit as st
import numpy as np
import pickle

model = pickle.load(open("aqi_model.pkl", "rb"))

st.title("AQI Prediction")

pm25 = st.number_input("PM2.5")
pm10 = st.number_input("PM10")
no = st.number_input("NO")
no2 = st.number_input("NO2")
nox = st.number_input("NOx")
nh3 = st.number_input("NH3")
co = st.number_input("CO")
so2 = st.number_input("SO2")
o3 = st.number_input("O3")

if st.button("Predict"):
    data = np.array([[pm25, pm10, no, no2, nox, nh3, co, so2, o3]])
    result = model.predict(data)

    aqi = result[0]

    if aqi <= 50:
        category = "Good "
    elif aqi <= 100:
        category = "Satisfactory "
    elif aqi <= 200:
        category = "Moderate "
    elif aqi <= 300:
        category = "Poor "
    elif aqi <= 400:
        category = "Very Poor "
    else:
        category = "Severe "

    st.success(f"AQI: {aqi:.2f}")
    st.info(f"Category: {category}")

    # st.slider("AQI Level", 0, 500, int(aqi))