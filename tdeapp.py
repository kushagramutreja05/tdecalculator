import streamlit as st

# Function to calculate BMR and TDE
def calculate_tdee(age, weight, height, gender, activity_level):
    if gender == 'Male':
        bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    else:
        bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
    tde = bmr * activity_level
    return bmr, tde

# Streamlit form for user input
st.title("TDEE Calculator")

age = st.number_input("Age", min_value=1, max_value=120, step=1)
weight = st.number_input("Weight (kg)", min_value=1.0, step=0.1)
height = st.number_input("Height (cm)", min_value=1.0, step=0.1)
gender = st.selectbox("Gender", ["Male", "Female"])
activity_level = st.selectbox("Activity Level", [
    ("Sedentary (little or no exercise)", 1.2),
    ("Lightly Active (light exercise/sports 1-3 days/week)", 1.37),
    ("Moderately Active (moderate exercise/sports 3-5 days/week)", 1.55),
    ("Very Active (hard exercise/sports 6-7 days a week)", 1.725),
    ("Extra Active (very hard exercise/physical job or 2x training)", 1.9)
])

# Calculate TDE when the button is pressed
if st.button("Calculate TDEE"):
    bmr, tde = calculate_tdee(age, weight, height, gender, activity_level[1])
    st.write(f"Basal Metabolic Rate (BMR): {bmr:.2f} kcal")
    st.write(f"Total Daily Energy Expenditure (TDEE): {tde:.2f} kcal")
