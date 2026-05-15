🥗 Diet Recommendation System using Machine Learning
📌 Project Overview

This project is a Machine Learning-based Diet Recommendation System that suggests suitable diet plans based on a user's health and lifestyle information.

The application predicts personalized diet categories such as:

Balanced Diet
Diabetic Diet
Heart Healthy Diet
High Protein Diet
Low Carb Diet

A Streamlit web application was developed for real-time diet recommendation.

❓ Problem Statement

Maintaining a healthy diet is important for overall well-being. Different people require different diet plans based on:

Age
BMI
Sugar Level
Cholesterol
Activity Level
Fitness Goal

The goal of this project is to build a Machine Learning model that recommends an appropriate diet plan based on user health data.

📂 Dataset Features

The dataset contains the following features:

Age
Gender
Height_cm
Weight_kg
BMI
Activity_Level
Sugar_Level
Cholesterol
Goal
Diet
🛠 Technologies Used
Python
NumPy
Pandas
Scikit-learn
Streamlit
Pickle
⚙️ Data Preprocessing

Categorical features were encoded into numerical values.

Gender Encoding
gender_map = {
    "Male": 1,
    "Female": 0
}
Activity Level Encoding
activity_map = {
    "Low": 0,
    "Medium": 1,
    "High": 2
}
Goal Encoding
goal_map = {
    "Weight Loss": 0,
    "Weight Gain": 1,
    "Maintain": 2
}
🤖 Machine Learning Model Used
Logistic Regression

The model was trained to classify users into different diet categories.

📊 Output Diet Categories
diet_map = {
    0: "Balanced",
    1: "Diabetic",
    2: "Heart Healthy",
    3: "High Protein",
    4: "Low Carb"
}
🧠 Feature Scaling

StandardScaler was used to scale numerical input features before model training.

from sklearn.preprocessing import StandardScaler
📈 Model Performance
Train Accuracy: 82.3%
Test Accuracy: 82%

The model showed stable performance without major overfitting.

🔄 Project Workflow
Dataset Reading
       ↓
Data Cleaning
       ↓
Encoding Categorical Features
       ↓
Feature Scaling
       ↓
Train Test Split
       ↓
Model Training
       ↓
Prediction
       ↓
Diet Recommendation
       ↓
Streamlit Deployment
🌐 Streamlit Web Application

The Streamlit app allows users to:

Enter health details
Select activity level
Select fitness goal
Predict recommended diet plan instantly
🍽 Diet Recommendations
Balanced Diet
Rice/Roti
Vegetables
Fruits
Dal
Curd
Diabetic Diet
Low sugar foods
Whole grains
Green vegetables
Avoid sweets
Heart Healthy Diet
Oats
Fruits
Nuts
Low oil foods
High Protein Diet
Eggs
Paneer
Chicken
Sprouts
Low Carb Diet
Vegetables
Paneer
Eggs
Reduce rice and sugar
💾 Pickle Files Used
diet_recommended_prediction_model.pkl
scaler.pkl
📁 Project Structure
Diet-Recommendation-System/
│
├── app.py
├── diet_recommended_prediction_model.pkl
├── scaler.pkl
├── requirements.txt
├── README.md
▶️ Installation
pip install -r requirements.txt
▶️ Run Streamlit App
streamlit run app.py
🚀 Future Improvements
Deep Learning Models
More Diet Categories
Real-time Health Monitoring
API Integration
Personalized Meal Plans
👩‍💻 Author
Likhitha Bellamkonda
