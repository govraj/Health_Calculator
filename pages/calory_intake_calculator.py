import streamlit as st

# Title of the app
st.title("Calories Intake Calculator")

# Inputs for weight, height, age, and gender
current_weight = st.number_input("Enter your current weight (in kg)", value=0.0)
height = st.number_input("Enter your height (in cm)", value=0.0)
age = st.number_input("Enter your age (in years)", value=0)
gender = st.selectbox("Select your gender", ["Male", "Female"])
activity_level = st.selectbox("Select your activity level", [
    "Sedentary (little or no exercise)", 
    "Lightly active (light exercise/sports 1-3 days/week)", 
    "Moderately active (moderate exercise/sports 3-5 days/week)", 
    "Very active (hard exercise/sports 6-7 days a week)", 
    "Super active (very hard exercise & physical job)"
])

# Input for desired ideal weight
ideal_weight = st.number_input("Enter your ideal weight (in kg)", value=0.0)

# Calculate BMR using the Mifflin-St Jeor Equation
def calculate_bmr(weight, height, age, gender):
    if gender == "Male":
        bmr = 10 * weight + 6.25 * height - 5 * age + 5
    else:
        bmr = 10 * weight + 6.25 * height - 5 * age - 161
    return bmr

# Activity multiplier
activity_multiplier = {
    "Sedentary (little or no exercise)": 1.2,
    "Lightly active (light exercise/sports 1-3 days/week)": 1.375,
    "Moderately active (moderate exercise/sports 3-5 days/week)": 1.55,
    "Very active (hard exercise/sports 6-7 days a week)": 1.725,
    "Super active (very hard exercise & physical job)": 1.9
}

if st.button("Calculate"):
    if current_weight > 0 and height > 0 and age > 0 and ideal_weight > 0:
        # Calculate BMR and TDEE for current weight
        bmr_current = calculate_bmr(current_weight, height, age, gender)
        tdee_current = bmr_current * activity_multiplier[activity_level]
        
        # Calculate BMR and TDEE for ideal weight
        bmr_ideal = calculate_bmr(ideal_weight, height, age, gender)
        tdee_ideal = bmr_ideal * activity_multiplier[activity_level]
        
        # Display results
        st.success(f"To maintain your current weight, you need approximately {tdee_current:.0f} calories per day.")
        st.success(f"To achieve your ideal weight of {ideal_weight} kg, you need approximately {tdee_ideal:.0f} calories per day.")
    else:
        st.error("Please provide all input values correctly.")

# Footer message
st.write("This calculator is based on the Mifflin-St Jeor Equation for BMR and adjusts for activity levels to estimate TDEE.")
