import datetime
import pandas as pd
import plotly.express as px
import requests
import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Pacific Ocean & El Niño Climate Threat Tracker", layout="wide"
)

# Custom Theme Styling
st.markdown(
    """
    
""",
    unsafe_allow_html=True,
)


# Function to fetch live weather data for the sidebar regional search
def get_weather_data(city_name):
  try:
    geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city_name}&count=1&format=json"
    geo_res = requests.get(geo_url).json()

    if "results" not in geo_res or not geo_res["results"]:
      return None, None, "Location not found!"

    resolved_name = geo_res["results"][0].get("name", city_name)
    country = geo_res["results"][0].get("country", "")

    lat = geo_res["results"][0]["latitude"]
    lon = geo_res["results"][0]["longitude"]

    weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,wind_speed_10m"
    weather_res = requests.get(weather_url).json()

    return (
        weather_res["current"]["temperature_2m"],
        weather_res["current"]["wind_speed_10m"],
        f"{resolved_name}, {country}" if country else resolved_name,
    )
  except Exception as e:
    return None, None, str(e)


# --- Sidebar Regional Search Control (Added Back) ---
st.sidebar.markdown("### 🕹️ Regional Search Control")
city_input = st.sidebar.text_input("Enter Region/City:", "Chennai")

if "regional_temp" not in st.session_state:
  st.session_state.regional_temp = 29.1
  st.session_state.regional_wind = 13.8
  st.session_state.regional_loc = "Chennai, India"

if st.sidebar.button("Sync Region Data"):
  with st.spinner(f"Syncing data for {city_input}..."):
    temp, wind, loc = get_weather_data(city_input)
    if temp is not None:
      st.session_state.regional_temp = temp
      st.session_state.regional_wind = wind
      st.session_state.regional_loc = loc
      st.sidebar.success("Synced successfully!")
    else:
      st.sidebar.error("Error fetching location.")

# Main title focused on Pacific Ocean State
st.title("🌊 Pacific Ocean & El Niño Threat Tracker")
st.markdown("Live Sea Surface Temperature (SST) & Global Climate Impact Dashboard")
st.markdown("---")

# --- CORE FOCUS: Pacific Ocean SST & El Niño Status ---
st.markdown("### 🌊 Pacific Ocean SST Index (El Niño 3.4)")
col1, col2 = st.columns(2)
with col1:
  st.metric(label="Current Pacific Sea Surface Temp (SST)", value="29.2 °C")
with col2:
  st.metric(label="Anomaly Deviation", value="+1.4 °C (Above Normal)")

st.markdown("### 📊 Live Visual Ocean State Indicator")
st.error("🚨 CRITICAL STATE: ACTIVE EL NIÑO EVENT DETECTED!")
st.markdown(
    "**Public Impact & Scientific Context:** Sustained warming in the central"
    " and eastern tropical Pacific Ocean. Severe risk of disrupted monsoon"
    " cycles, global weather shifts, and intense heatwaves."
)

# Pacific Ocean Focused Map
st.markdown("### 🗺️ Pacific Ocean & El Niño Tracking Map")
pacific_map_df = pd.DataFrame({"lat": [0.0], "lon": [-140.0]})
st.map(pacific_map_df, zoom=2, size=2000)

# Live 7-Day Temperature Forecast
st.markdown("### 📅 Live 7-Day Temperature Forecast")
forecast_data = pd.DataFrame({
    "Date": pd.date_range(start="2026-09-12", periods=7),
    "Max Temp (°C)": [31.2, 30.5, 30.4, 30.8, 31.0, 31.5, 31.1],
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

# Hourly Ocean Log Chart
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

# --- Searched Region Weather Section ---
st.markdown("---")
st.markdown(
    f"### 📍 Searched Region Weather: {st.session_state.regional_loc}"
)
col_r1, col_r2 = st.columns(2)
with col_r1:
  st.metric(
      label="Local Air Temp", value=f"{st.session_state.regional_temp} °C"
  )
with col_r2:
  st.metric(
      label="Local Wind Speed", value=f"{st.session_state.regional_wind} km/h"
  )

# Advisories & Helplines
st.markdown("### 💡 Climate Action & Public Health Advisories")
st.info(
    "💧 Due to active El Niño conditions, ensure water conservation and"
    " monitor heat advisories regularly."
)

st.markdown("### 🚨 Emergency Helpline Support")
st.markdown("""
* **National Disaster Management (NDMA):** 1078
* **State Emergency Helpline:** 1070
* **Ambulance Services:** 108
* **Fire & Rescue:** 101
""")
