import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open("model_pickle", "rb") as file:
    model = pickle.load(file)

# Title
st.title("🏠 House Price Prediction")

st.write("Enter the details below to predict the house price.")

# User Inputs
area = st.number_input("Area (sq ft)", min_value=0.0, step=100.0)
bedrooms = st.number_input("Bedrooms", min_value=1, step=1)
bathrooms = st.number_input("Bathrooms", min_value=1, step=1)

# Predict Button
if st.button("Predict Price"):
    input_data = np.array([[area, bedrooms, bathrooms]])
    prediction = model.predict(input_data)

    st.success(f"Predicted House Price: ₹ {prediction[0]:,.2f}")