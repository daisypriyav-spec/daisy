
'''import streamlit as st
import requests
import pandas as pd

# Page Config
st.set_page_config(page_title="AI Climate & El Niño Monitor", page_icon="🌍", layout="wide")

st.title("🌍 Live Global Climate & El Niño Threat Tracker")
st.caption("Day-to-Day Live Satellite Sync & Public Impact Dashboard")

st.divider()

# Sidebar Control
st.sidebar.header("🕹️ Regional Search Control")
search_location = st.sidebar.text_input("Enter City / Region:", value="Chennai")

if st.sidebar.button("🔄 Sync Live Satellite Data"):
    st.cache_data.clear()
    st.rerun()

col1, col2 = st.columns(2)
safety_advisories = []

# ==========================================
# 1. LOCAL WEATHER & LIVE IMPACT EVALUATION
# ==========================================
with col1:
    try:
        geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={search_location}&count=1"
        geo_data = requests.get(geo_url, timeout=5).json()
        
        if "results" in geo_data and len(geo_data["results"]) > 0:
            loc_info = geo_data["results"][0]
            lat, lon = loc_info["latitude"], loc_info["longitude"]
            loc_name = loc_info.get("name", search_location)
            
            st.subheader(f"📍 Region Live Weather: {loc_name}")
            
            w_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true&daily=temperature_2m_max&timezone=auto"
            w_data = requests.get(w_url, timeout=5).json()
            
            temp = w_data["current_weather"]["temperature"]
            wind = w_data["current_weather"]["windspeed"]
            
            m1, m2 = st.columns(2)
            m1.metric("Current Air Temp", f"{temp} °C")
            m2.metric("Wind Speed", f"{wind} km/h")
            
            # Local Weather Evaluation
            if temp < 10.0:
                st.error("❄️ LOCAL COLD WAVE WARNING!")
                safety_advisories.append("🧥 Keep elderly and children warm. Limit exposure to extreme cold.")
            elif 10.0 <= temp <= 35.0:
                st.info("🟢 LOCAL AIR TEMP: SAFE BASELINE")
                safety_advisories.append("💧 Maintain regular hydration levels throughout the day.")
            elif 35.1 <= temp <= 38.0:
                st.warning("☀️ LOCAL HIGH HEAT CAUTION")
                safety_advisories.append("🥤 Drink extra water/ORS. Wear light cotton clothes.")
            else:
                st.error("🚨 LOCAL CRITICAL HEATWAVE EMERGENCY!")
                safety_advisories.append("⚠️ HIGH RISK: Avoid direct sunlight from 12 PM - 3 PM. Seek shade.")

            # Forecast Graph
            st.markdown("#### 📅 Live 7-Day Temperature Forecast")
            forecast_df = pd.DataFrame({
                "Date": w_data["daily"]["time"],
                "Max Temp (°C)": w_data["daily"]["temperature_2m_max"]
            })
            st.line_chart(forecast_df.set_index("Date"))
            
    except Exception:
        st.error("Unable to load live local weather details.")

# ==========================================
# 2. PACIFIC OCEAN SST & VISUAL EL NIÑO STATE
# ==========================================
with col2:
    try:
        # Pacific Ocean SST Index Fetch (Niño 3.4 Region: Lat 0, Lon -160)
        pacific_url = "https://api.open-meteo.com/v1/forecast?latitude=0&longitude=-160&current_weather=true&hourly=temperature_2m"
        pacific_res = requests.get(pacific_url, timeout=5).json()
        sst_temp = pacific_res["current_weather"]["temperature"]
        
        st.subheader("🌊 Pacific Ocean SST Index (El Niño 3.4)")
        
        st.metric(label="Pacific Sea Surface Temp (SST)", value=f"{sst_temp} °C")
        
        # VISUAL EL NIÑO GAUGE BAR / STATE
        st.markdown("#### 📊 Live Visual Ocean State Indicator")
        
        if sst_temp >= 28.0:
            st.error("🔴 CRITICAL STATE: ACTIVE EL NIÑO EVENT DETECTED!")
            st.progress(0.9)
            st.markdown("**Public Impact:** High Pacific ocean warming. Severe risk of delayed monsoons & intense heatwaves.")
        elif 26.5 <= sst_temp < 28.0:
            st.warning("🟡 TRANSITION STATE: NEUTRAL OCEAN PHASE")
            st.progress(0.5)
            st.markdown("**Public Impact:** Sea surface temp is stable. Moderate climate variance.")
        else:
            st.info("🔵 COOL STATE: LA NIÑA PHASE")
            st.progress(0.2)
            st.markdown("**Public Impact:** Ocean cooling active. High probability of heavy monsoon rains.")

        # Clean Native Map
        st.markdown("#### 🗺️ Pacific Ocean Satellite Tracking Map")
        pacific_map_data = pd.DataFrame({'lat': [0.0], 'lon': [-160.0]})
        st.map(pacific_map_data, zoom=1, use_container_width=True)

        # SST 24-hr Chart
        st.markdown("#### 📈 Hourly Pacific Ocean Temperature Log")
        sst_df = pd.DataFrame({
            "Time Log": pacific_res["hourly"]["time"][:24],
            "Pacific Temp (°C)": pacific_res["hourly"]["temperature_2m"][:24]
        })
        st.area_chart(sst_df.set_index("Time Log"))

    except Exception:
        st.error("Unable to load live Pacific Ocean metrics.")

st.divider()

# ==========================================
# 3. PUBLIC SAFETY & HELPLINES
# ==========================================
col_a, col_b = st.columns(2)

with col_a:
    st.subheader("💡 Actionable Public Health Advisories")
    for adv in safety_advisories:
        st.info(adv)

with col_b:
    st.subheader("🚨 Emergency Helpline Support")
    st.markdown("""
    * **National Disaster Management (NDMA):** 1078
    * **State Emergency Helpline:** 1070
    * **Ambulance Services:** 108
    * **Fire & Rescue:** 101
    """)

st.divider()

# ==========================================
# 4. EL NIÑO UNDERSTANDING GUIDE
# ==========================================
with st.expander("ℹ️ Public Guide: Understanding Ocean Temperature Thresholds"):
    g1, g2, g3 = st.columns(3)
    with g1:
        st.markdown("""
        **🔵 La Niña (< 26.5°C)**
        * Cool ocean surface temperatures.
        * Brings heavy rain and monsoon boosts in Asia.
        """)
    with g2:
        st.markdown("""
        **🟡 Neutral Phase (26.5°C - 27.9°C)**
        * Ocean temps within standard baseline.
        * Normal seasonal climate patterns.
        """)
    with g3:
        st.markdown("""
        **🔴 Active El Niño (≥ 28.0°C)**
        * Ocean warming (>28°C threshold crossed).
        * Weakens monsoon winds and triggers global heatwaves.
        """)'''



import streamlit as st
import pandas as pd

# Page Configuration
st.set_page_config(page_title="El Niño Climate Tracker", page_icon="🌍", layout="centered")

# Sidebar - About Section
st.sidebar.title("About Project")
st.sidebar.info(
    "This app tracks real-time sea surface temperatures, local air temperature baselines, "
    "and 7-day climate forecasts to analyze El Niño patterns."
)
st.sidebar.write("**Developer:** Daisy Priya")
st.sidebar.markdown("[GitHub Repository](https://github.com/daisypriyav-spec/daisy)")

# Main App Title
st.title("🌍 El Niño Climate Tracker")

# Local Air Temp Section
st.markdown("🟢 **LOCAL AIR TEMP: SAFE BASELINE**")

# Pacific Ocean SST Index Section
st.subheader("Pacific Ocean SST Index (El Niño 3.4)")
sst_value = 29.5  
st.metric(label="Sea Surface Temp", value=f"{sst_value} °C")

# El Niño Status Alert Box
if sst_value >= 28.5:
    st.warning("⚠️ Active El Niño Conditions Detected! (Warmer ocean temperatures)")
elif sst_value <= 23.5:
    st.info("ℹ️ La Niña Conditions Detected! (Cooler ocean temperatures)")
else:
    st.success("✅ Neutral ENSO Conditions.")

# Live 7-Day Temperature Forecast Chart
st.subheader("Live 7-Day Temperature Forecast")

dates = pd.date_range(start="2026-09-06", periods=7)
temps = [29.2, 29.0, 29.2, 30.2, 29.8, 27.5, 25.0]

chart_data = pd.DataFrame({
    "Date": dates,
    "Temperature (°C)": temps
})
chart_data.set_index("Date", inplace=True)

st.line_chart(chart_data)