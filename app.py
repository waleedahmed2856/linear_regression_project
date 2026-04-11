import streamlit as st
from parameters import load_artifacts, load_locations, get_estimated_price

load_artifacts()

st.title("House Price Predictor")

location = st.selectbox("Select Location", load_locations())

area = st.number_input("Area (sq ft)", min_value=300)
bhk = st.number_input("BHK", min_value=1, max_value=10)
bath = st.number_input("Bathrooms", min_value=1, max_value=10)

if st.button("Predict Price"):
    price = get_estimated_price(location, area, bhk, bath)
    st.success(f"Estimated Price: {price}")