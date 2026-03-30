import streamlit as st
import plotly.graph_objects as go


st.title("Air Quality Index (AQI)")

st.markdown("###  What does the air you breathe actually contain?")

st.markdown("""
<p style="font-size:17px; color:#cccccc;">
AQI tells you <b>how safe or harmful your air is</b> — in one simple number.
</p>
""", unsafe_allow_html=True)

st.markdown("### ⚡ Why it matters")

st.markdown("""
-  Affects your lungs and breathing  
-  Impacts heart health over time  
-  Sensitive for children & elderly  
-  Reflects environmental condition  
""")

st.markdown("###  Simple rule")

st.markdown("""
<div style="
padding:12px;
border-radius:10px;
background-color:#1c1c1c;
color:#e6e6e6;
font-size:16px;
margin-bottom:10px;">
⬇ Lower AQI = Cleaner air
</div>

<div style="
padding:12px;
border-radius:10px;
background-color:#1c1c1c;
color:#e6e6e6;
font-size:16px;">
⬆ Higher AQI = More pollution
</div>
""", unsafe_allow_html=True)
st.set_page_config(page_title="AQI Dashboard", layout="centered")

st.markdown("<br><br>", unsafe_allow_html=True) 
st.subheader("What if AQI is...?")

aqi = st.number_input("Enter AQI Value", min_value=0, max_value=500, value=0)

def get_aqi_status(aqi):
    if aqi <= 50:
        return "Good "
    elif aqi <= 100:
        return "Satisfactory "
    elif aqi <= 200:
        return "Moderate "
    elif aqi <= 300:
        return "Poor "
    elif aqi <= 400:
        return "Very Poor "
    else:
        return "Severe "

status = get_aqi_status(aqi)
fig = go.Figure(go.Indicator(
    mode="gauge+number",
    value=aqi,
    title={'text': "AQI Level"},
    gauge={
        'axis': {'range': [0, 500]},
        'bar': {'color': "black"},  
        'steps': [
            {'range': [0, 50], 'color': "green"},
            {'range': [50, 100], 'color': "yellow"},
            {'range': [100, 200], 'color': "orange"},
            {'range': [200, 300], 'color': "red"},
            {'range': [300, 400], 'color': "purple"},
            {'range': [400, 500], 'color': "maroon"}
        ],
    }
))

st.plotly_chart(fig, use_container_width=True)
st.subheader(f"Status: {status}")
with st.expander("About AQI"):
    st.write("""
    AQI (Air Quality Index) measures how polluted the air is.

    - Lower AQI → Cleaner air  
    - Higher AQI → More pollution  
    """)

st.subheader("Health Advice")
if aqi <= 50:
    st.success("Air is clean. Safe for everyone.")
elif aqi <= 100:
    st.info("Air is acceptable. Minor concern for sensitive people.")
elif aqi <= 200:
    st.warning("Sensitive groups may feel discomfort.")
elif aqi <= 300:
    st.warning("Avoid prolonged outdoor exposure.")
else:
    st.error("Health risk! Stay indoors and wear a mask.")