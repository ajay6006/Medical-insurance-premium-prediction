# 🏥 Medical Insurance Premium Prediction using Machine Learning  

## 🌐 Live Demo  
🔗 **Try the Web App Here:** [Medical Insurance Premium Prediction](https://medical-insurance-premium-prediction-aj.streamlit.app/)  

## 📌 Project Overview  
This project aims to build a machine learning model to predict a person's medical insurance premium based on various factors like age, BMI, smoking status, and region. By leveraging machine learning techniques, we enhance the accuracy of premium estimation, helping insurers and individuals make informed financial decisions.  

## 🔍 Problem Statement  
The goal is to develop a predictive model that estimates medical insurance costs based on user-provided input data. The dataset includes the following features:  

- **Independent Variables:** Age, Sex, BMI, Number of Children, Smoker (Yes/No), Region  
- **Target Variable:** Insurance Charges (Premium Cost)  

## 🛠️ Tools & Technologies Used  
- **Programming Language:** Python  
- **Libraries:** Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn  
- **Machine Learning Models:** Linear Regression, Decision Tree, Random Forest, XGBoost  
- **Deployment:** Streamlit  

## 🔄 Project Workflow  
1. **Data Collection & Preprocessing**  
   - Loaded the dataset and checked for missing values and inconsistencies  
   - Performed exploratory data analysis (EDA) using statistical measures and visualizations  
   - Encoded categorical features using One-Hot Encoding  

2. **Model Training & Evaluation**  
   - Split the dataset into training and testing sets  
   - Trained multiple ML models: Linear Regression, Decision Tree, Random Forest, and XGBoost  
   - Evaluated models using **R² score** and **Mean Absolute Error (MAE)**  
   - Achieved the best performance using **XGBoost (R² Score: 87%, MAE: 2464.63)**  

3. **Deployment**  
   - Saved the trained model using Pickle  
   - Built an interactive web app using Streamlit for real-time premium prediction  

## 📈 Conclusion  
- XGBoost outperformed other models, achieving an **R² score of 87%** and **MAE of 2464.63**.  
- The model effectively predicts insurance premiums based on user inputs.  
- The Streamlit-based deployment makes it accessible and easy to use.  
