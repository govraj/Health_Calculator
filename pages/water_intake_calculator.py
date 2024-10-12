import streamlit as st

# Title of the app
st.title("Daily Water Intake Calculator")

# Input for body weight
weight = st.number_input("Enter your body weight (in kilograms)", value=0.0)

# Convert body weight to pounds (optional, if you want to use pounds)
weight_in_pounds = weight * 2.20462

# Calculation: Water intake is often recommended as 35 ml of water per kilogram of body weight.
if st.button("Calculate"):
    if weight > 0:
        # Calculate the daily water intake in liters
        water_intake_liters = (weight * 35) / 1000  # 35 ml per kg
        st.success(f"Your recommended daily water intake is: {water_intake_liters:.2f} liters.")
    else:
        st.error("Please enter a valid weight greater than zero.")

# Footer message
st.write("This calculator is based on the general recommendation of 35 ml of water per kg of body weight.")
