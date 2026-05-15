import pickle
file_path = "model_diet.pkl"
with open(file_path, "rb") as file:
    model = pickle.load(file)
print(model)
print(type(model))
import numpy as np
import pandas as pd
import streamlit as st
import pickle

# load model
model = pickle.load(open("model_diet.pkl", "rb"))
Scaler =pickle.load(open("scaler_diet.pkl", "rb"))
st.markdown("""
<style>

label {
    color: black !important;
    font-size: 18px !important;
    font-weight: bold !important;
}

.stApp {
    background-color: #F0F8FF;
    border: 5px solid #1E90FF;
    border-radius: 20px;
    padding: 20px;
}

</style>
""", unsafe_allow_html=True)
col1, col2 = st.columns([3,1])

with col1:
    st.markdown(
        "<h1 style='color:#458376;'>Diet Plan Recommendation App</h1>",
        unsafe_allow_html=True
    )

with col2:
    st.image("img.png", width=120)
# user inputs
# user inputs

age = st.number_input("Age", min_value=1, max_value=100)

height = st.number_input("Height (cm)", min_value=50, max_value=250)

weight = st.number_input("Weight (kg)", min_value=10, max_value=200)

gender = st.selectbox("Gender", ["Male", "Female"])

bmi = st.number_input("BMI", min_value=5.0, max_value=60.0)

activity = st.selectbox(
    "Activity Level",
    ["Low", "Medium", "High"]
)

sugar_level = st.number_input("Sugar Level", min_value=50, max_value=300)

cholestrol = st.number_input("Cholesterol", min_value=50, max_value=400)

goal = st.selectbox(
    "Goal",
    ["Weight Loss", "Weight Gain", "Maintain"]
)

# encoding manually
gender_value = 1 if gender == "Male" else 0

activity_map = {
    "Low": 0,
    "Medium": 1,
    "High": 2
}

goal_map = {
    "Weight Loss": 0,
    "Weight Gain": 1,
    "Maintain": 2
}

activity_value = activity_map[activity]
goal_value = goal_map[goal]

# output mapping
diet_map = {
    0: "Balanced",
    1: "Diabetic",
    2: "Heart Healthy",
    3: "High Protein",
    4: "Low Carb"
}
diet_plans = {
    "Balanced": "Eat rice/roti, dal, vegetables, fruits, curd, and enough water.",
    "Diabetic": "Eat low sugar foods, whole grains, green vegetables, dal, and avoid sweets/soft drinks.",
    "Heart Healthy": "Eat oats, fruits, vegetables, nuts, low-oil food, and avoid fried foods.",
    "High Protein": "Eat eggs/paneer/chicken, dal, sprouts, Greek yogurt, nuts, and milk.",
    "Low Carb": "Eat more vegetables, paneer/eggs/chicken, nuts, and reduce rice, bread, and sweets."
}

# prediction
if st.button("Recommend Diet"):
    input_data = np.array([[
        age,
        gender_value,
        height,
        weight,
        bmi,
        activity_value,
        sugar_level,
        cholestrol,
        goal_value
    ]])

    input_data = Scaler.transform(input_data)

    prediction = model.predict(input_data)

    diet_name = diet_map[prediction[0]]

    st.markdown(
        f"<h2 style='color:green;'>Recommended Diet: {diet_name}</h2>",
        unsafe_allow_html=True
    )

    st.write("Diet Plan:")
    st.info(diet_plans[diet_name])