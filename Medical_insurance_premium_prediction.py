import streamlit as st
import pickle
import numpy as np
import os
st.write("Current Working Directory: ", os.getcwd())

# Load trained model
with open("xgboost_model.pkl", "rb") as file:
    model = pickle.load(file)

# Define the app
st.title("Medical Insurance Premium Prediction")

# User Inputs
age = st.number_input("Age", min_value=18, max_value=100, step=1)
bmi = st.number_input("BMI", min_value=10.0, max_value=50.0, step=0.1)
children = st.number_input("Number of Children", min_value=0, max_value=10, step=1)
sex = st.selectbox("Sex", ["Male", "Female"])
smoker = st.selectbox("Smoker", ["Yes", "No"])
region = st.selectbox("Region", ["Northeast", "Northwest", "Southeast", "Southwest"])

# Convert categorical data
sex = 1 if sex == "Male" else 0
smoker = 1 if smoker == "Yes" else 0
region_dict = {"Northeast": 0, "Northwest": 1, "Southeast": 2, "Southwest": 3}
region = region_dict[region]

# Prediction
if st.button("Predict Premium"):
    features = np.array([[age, sex, bmi, children, smoker, region]])
    prediction = model.predict(features)[0]
    st.success(f"Estimated Insurance Premium: ${prediction:.2f}")
