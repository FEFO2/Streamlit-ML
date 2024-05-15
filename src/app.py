
# Import libraries
import streamlit as st
import pandas as pd
import pickle

# Import model
with open('../models/tree_classifier_criterion-entropy_maxdepth-15_minsamleaf-1_minsamsplit-2_RS-42.sav', 'rb') as file:
    model = pickle.load(file)

# Write title and subtitle
st.title('Are you overweight?')
st.write('1 out of 3 US citizens currently have obsesity. Find out if you have it too:')
# Insert Values
Height_val = st.number_input("Enter your height (cms):", min_value=1, step=1)
Weight_val = st.number_input("Enter your weight (kgs):", min_value=1.0, step=0.1)

if st.button("predict"):
    row = [[Height_val,
           Weight_val]]
    result = model.predict(row)
    # Map the result
    if result == 0: category = "Underweight"
    elif result == 1: category = "Normal weight"
    elif result == 2: category = "Overweight"
    elif result == 3: category = "Obese"
    else: category = "Unknown"
    
    # Show the result
    st.write('Your result is', category,'. Remember to eat fruits, vegetables and to avoid drinking too much soda.')
    st.write('Thank you. Stay healthy!')