import streamlit as st
import numpy as np
import pandas as pd
import pickle

# Load the trained XGBoost model
with open('xgboost_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Streamlit App
def main():
    st.title("Medical Insurance Premium Prediction")
    st.write("Enter the details to predict insurance charges")
    
    # User Inputs
    age = st.number_input("Age", min_value=18, max_value=100, value=30)
    bmi = st.number_input("BMI", min_value=10.0, max_value=50.0, value=25.0)
    children = st.number_input("Number of Children", min_value=0, max_value=10, value=0)
    smoker = st.selectbox("Smoker", ["Yes", "No"])
    sex = st.selectbox("Sex", ["Male", "Female"])
    region = st.selectbox("Region", ["northeast", "northwest", "southeast", "southwest"])
    
    # Preprocessing
    smoker = 1 if smoker == "Yes" else 0
    sex = 1 if sex == "Male" else 0
    
    # Convert input to dataframe
    input_data = pd.DataFrame([[age, sex, bmi, children, smoker]],
                              columns=["age", "sex", "bmi", "children", "smoker"])
    
    # Predict
    if st.button("Predict Premium"):
        prediction = model.predict(input_data)
        st.success(f"Estimated Insurance Premium: ${prediction[0]:,.2f}")

if __name__ == "__main__":
    main()