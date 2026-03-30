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

# Continue the Helper Function from here tomorrow

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
st.header("Property Details")

col1, col2 = st.columns(2)

with col1:
  floor_area_sqm = st.number_input("Floor Area (sqm)", min_value=30.0, max_value=200.0, value=90.0, step=1.0)
  mid_storey = st.slider("Storey Level (Mid-point)", min_value=1, max_value=50, value=8)
  lease_numeric = st.number_input("Remaining Lease (Years)", min_value=1.0, max_value=99.0, value=75.0, step=1.0)

with col2:
  cbd_dist_km = st.number_input("Distance to CBD (km)", min_value=0.0, max_value=30.0, value=5.5, step=0.1)
  mrt_dist_km = st.number_input("Nearest MRT (km)", min_value=0.0, max_value=10.0, value=0.8, step=0.1)
  time_index = st.number_input("Time Index (e.g. 2026)", min_value=1, max_value=500, value=250, step=1)

# This will ensure that year, lat, long, and month_val have default values if needed by the model
year = 2026
latitude = 1.3521
longitude = 103.8198
month_val = 3

# This will create the DataFrame for prediction
input_data = pd.DataFrame({
  'floor_area_sqm': [floor_area_sqm],
  'cbd_dist_km': [cbd_dist_km],
  'mid_storey': [mid_storey],
  'time_index': [time_index],
  'lease_numeric': [lease_numeric],
  'year': [year],
  'latitude': [latitude],
  'longitude': [longitude],
  'mrt_dist_km': [mrt_dist_km],
  'month_val': [month_val]
})

# This is the prediction button
st.markdown("---")
if st.button("Calculate Value", type="primary"):
  if st.model_loaded:
    # This will re-order to match the model's expectation
    prediction = model.predict(input_data)
    st.success(f"### Estimated Resale Value: SGD ${int(prediction[0]):,}")
    st.info("💡 Insight: Floor area and distance to the CBD are the largest driving factors for this valuation.")
  else:
    st.warning("Model not found. Please ensure it is uploaded correctly in the repository.")
