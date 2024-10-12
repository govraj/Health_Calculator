import streamlit as st

# Title of the app
st.title("Daily Protein Intake Calculator")

# Input for current weight
current_weight = st.number_input("Enter your current weight (in kilograms)", value=0.0)

# Input for ideal weight
ideal_weight = st.number_input("Enter your ideal weight (in kilograms)", value=0.0)

# Select activity level
activity_level = st.selectbox("Select your activity level", [
    "Sedentary (little or no exercise)", 
    "Lightly active (light exercise/sports 1-3 days/week)", 
    "Moderately active (moderate exercise/sports 3-5 days/week)", 
    "Very active (hard exercise/sports 6-7 days/week)", 
    "Super active (intense exercise or physical job)"
])

# Protein intake per kg based on activity level
activity_multiplier = {
    "Sedentary (little or no exercise)": 0.8,  # grams of protein per kg
    "Lightly active (light exercise/sports 1-3 days/week)": 1.0,
    "Moderately active (moderate exercise/sports 3-5 days/week)": 1.3,
    "Very active (hard exercise/sports 6-7 days/week)": 1.6,
    "Super active (intense exercise or physical job)": 1.8
}

# Calculate protein intake for current and ideal weight
if st.button("Calculate"):
    if current_weight > 0 and ideal_weight > 0:
        # Protein intake for current weight
        current_protein_intake = current_weight * activity_multiplier[activity_level]
        st.success(f"Your recommended daily protein intake for your current weight is: {current_protein_intake:.1f} grams.")
        
        # Protein intake for ideal weight
        ideal_protein_intake = ideal_weight * activity_multiplier[activity_level]
        st.success(f"Your recommended daily protein intake for your ideal weight is: {ideal_protein_intake:.1f} grams.")
    else:
        st.error("Please enter valid values for both your current and ideal weight.")

# Footer message
st.write("This calculator is based on general recommendations for protein intake per kg of body weight.")
