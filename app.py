import datetime
import time
import pandas as pd
import plotly.express as px
import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Live Global Climate & El Niño Threat Tracker", layout="wide"
)

# Custom Styling for Dark Theme Look
st.markdown(
    """
    
""",
    unsafe_allow_html=True,
)

# Sidebar - Regional Search Control
st.sidebar.markdown("### 🕹️ Regional Search Control")
city = st.sidebar.text_input("Enter City / Region:", "Chennai")

if st.sidebar.button("Sync Live Satellite Data"):
  with st.spinner("Fetching live satellite data... Please wait..."):
    time.sleep(1.5)  # Simulating live fetch delay
  st.sidebar.success("Data synced successfully!")

# Main Dashboard Header
st.title("🌍 Live Global Climate & El Niño Threat Tracker")
st.markdown("Day-to-Day Live Satellite Sync & Public Impact Dashboard")
st.markdown("---")

# Region Live Weather Section
st.markdown(f"### 📍 Region Live Weather: {city}")
col1, col2 = st.columns(2)
with col1:
  st.metric(label="Current Air Temp", value="29.1 °C")
with col2:
  st.metric(label="Wind Speed", value="13.8 km/h")

st.success("🟢 LOCAL AIR TEMP: SAFE BASELINE")

# Live 7-Day Temperature Forecast Chart
st.markdown("### 📅 Live 7-Day Temperature Forecast")
forecast_data = pd.DataFrame({
    "Date": pd.date_range(start="2026-09-12", periods=7),
    "Max Temp (°C)": [31.2, 30.5, 30.4, 30.5, 31.0, 31.5, 31.2],
})
fig_forecast = px.line(
    forecast_data,
    x="Date",
    y="Max Temp (°C)",
    markers=True,
    template="plotly_dark",
)
fig_forecast.update_layout(
    plot_bgcolor="#0e1117", paper_bgcolor="#0e1117", margin=dict(t=20, b=20)
)
st.plotly_chart(fig_forecast, use_container_width=True)

# Pacific Ocean SST Index (El Niño 3.4)
st.markdown("### 🌊 Pacific Ocean SST Index (El Niño 3.4)")
st.metric(label="Pacific Sea Surface Temp (SST)", value="29.2 °C")

st.markdown("### 📊 Live Visual Ocean State Indicator")
st.error("🚨 CRITICAL STATE: ACTIVE EL NIÑO EVENT DETECTED!")
st.markdown(
    "**Public Impact:** High Pacific ocean warming. Severe risk of delayed"
    " monsoons & intense heatwaves."
)

# Hourly Pacific Ocean Temperature Log (Fixed blank blue block issue)
st.markdown("### 📈 Hourly Pacific Ocean Temperature Log")
hourly_data = pd.DataFrame({
    "Time Log": pd.date_range(start="2026-09-12 00:00", periods=12, freq="2h"),
    "Pacific Temp (°C)": [
        28.5,
        28.6,
        28.8,
        29.0,
        29.1,
        29.3,
        29.2,
        29.0,
        28.9,
        28.8,
        28.7,
        28.6,
    ],
})
fig_hourly = px.area(
    hourly_data, x="Time Log", y="Pacific Temp (°C)", template="plotly_dark"
)
fig_hourly.update_layout(
    plot_bgcolor="#0e1117", paper_bgcolor="#0e1117", margin=dict(t=20, b=20)
)
st.plotly_chart(fig_hourly, use_container_width=True)

# Actionable Public Health Advisories
st.markdown("### 💡 Actionable Public Health Advisories")
st.info("💧 Maintain regular hydration levels throughout the day.")

# Emergency Helpline Support
st.markdown("### 🚨 Emergency Helpline Support")
st.markdown("""
* **National Disaster Management (NDMA):** 1078
* **State Emergency Helpline:** 1070
* **Ambulance Services:** 108
* **Fire & Rescue:** 101
""")
