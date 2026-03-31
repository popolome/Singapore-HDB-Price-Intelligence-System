import streamlit as st
import pandas as pd
import joblib
import numpy as np
import requests
import math

# This is the page config
st.set_page_config(page_title="HDB Price Intelligence", page_icon='🏢', layout='centered')

# This is the title and description
st.title("SG Singapore HDB Price Intelligence System")
st.markdown("""
Estimate the resale value of an HDB flat using my XGBoost machine learning model.
Adjust the key property features below to see how they impact the final valuation.
""")

# This is the constants for the Distance Calculation, this is the Raffles Place MRT estimated coordinates
cbd_coords = (1.2830, 103.8513)

# Other MRTs coordinates
mrt_stations = {
  "Jurong East": (1.331, 103.7423),
  "Woodlands": (1.4369, 103.7865),
  "Bishan": (1.3508, 103.8481),
  "Tampines": (1.3533, 103.9452),
  "Paya Lebar": (1.3178, 103.8924),
  "Clementi": (1.3151, 103.7652),
  "Serangoon": (1.3500, 103.8736),
  "Outram Park": (1.2804, 103.8395)
}

# This is the OneMap Helper Function to fetch lat and long from OneMap API
def get_coordinates(search_val):
  url = f"https://www.onemap.gov.sg/api/common/elastic/search?searchVal={search_val}&returnGeom=Y&getAddrDetails=Y&pageNum=1"
  response = requests.get(url)
  if response.status_code == 200:
    data = response.json()
    if data['found'] > 0:
      result = data['results'][0]
      lat = float(data['results']['LATITUDE'])
      lon = float(data['results']['LONGITUDE'])
      address = result['ADDRESS']
      return lat, lon, address
  return None, None, None

# This is the Haversine Helper Function to calculate the distance in km based on lat and lon
def haversine(coord1, coord2):
  R = 6371.0 # This is the earth's radius in km
  lat1, lon1 = math.radians(coord1[0]), math.radians(coord1[1])
  lat2, lon2 = math.radians(coord2[0]), math.radians(coord2[1])

  dlat = lat2 - lat1
  dlon = lon2 - lon1

  a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
  c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

  return R * c

# This is the MRT Helpder Function to find the nearest MRT in our dictionary based on distance
def get_nearest_mrt(lat, lon):
  min_dist = float('inf')
  for name, coords in mrt_stations.items():
    dist = haversine((lat, lon), coords)
    if dist < min_dist:
      min_dist = dist
  return min_dist

# This loads the model
# This uses st.cache_resource so the model loads only once
@st.cache_resource
def load_model():
  return joblib.load('models/hdb_price_model.pkl')

try:
  model = load_model()
  model_loaded = True
except Exception as e:
  st.error(f"Error loading model: {e}")
  model_loaded = False

# This is the user input
st.header("1. Find the Property")
address_input = st.text_input("Enter the HDB Address or Postal Code (e.g., '310B Punggol Walk' or '822310')")

if address_input.strip():
  with st.spinner("Geocoding via OneMap API..."):
    lat, lon, found_address = get_coordinates(address_input)

  # This will show the user what the search actually found
  if lat and lon:
    st.success(f"Location Found: **{found_address}**")
    st.caption(f"Coordinates: **{lat:.4f}, {lon:.4f}**")

    # This will auto calculate the distance using our two helper functions
    calc_cbd_dist = haversine((lat, lon), cbd_coords)
    calc_mrt_dist = get_nearest_mrt(lat, lon)

    st.info(f"📍 Distance to CBD: **{calc_cbd_dist:.2f} km** | 🚇 Nearest MRT: **{calc_mrt_dist:.2f} km**")

    st.header("2. Property Details")
    col1, col2 = st.columns(2)

    with col1:
      floor_area_sqm = st.number_input("Floor Area (sqm)", min_value=30.0, max_value=200.0, value=90.0, step=1.0)
      mid_storey = st.slider("Storey Level (Mid-point)", min_value=1, max_value=50, value=8)
    
    with col2:
      lease_numeric = st.number_input("Remaining Lease (Years)", min_value=1.0, max_value=99.0, value=75.0, step=1.0)
      time_index = st.number_input("Time Index (Months since start)", min_value=1, max_value=500, value=250, step=1)

    # These are required by the model but I will just use today's date
    year = 2026
    month_val = 3

    # This will create the DataFrame for prediction
    # Also added the auto calculation for cbd, lat, lon, and mrt distance
    input_data = pd.DataFrame({
      'year': [year],
      'month_val': [month_val],
      'time_index': [time_index],
      'mid_storey': [mid_storey],
      'lease_numeric': [lease_numeric],
      'floor_area_sqm': [floor_area_sqm],
      'latitude': [lat],
      'longitude': [lon],
      'mrt_dist_km': [calc_mrt_dist],
      'cbd_dist_km': [calc_cbd_dist]
    })

    # This is the prediction button
    st.markdown("---")
    if st.button("Calculate Value", type="primary"):
      if model_loaded:
        prediction = model.predict(input_data)
        st.success(f"### Estimated Resale Value: SGD ${int(prediction[0]):,}")
        st.info("💡 Insight: Floor area and distance to the CBD are the largest driving factors for this valuation.")
      else:
        st.warning("Model not found. Please ensure it is uploaded correctly in the repository.")
  else:
      st.error("Address not found on OneMap. Please try a different query.")
