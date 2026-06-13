import os
import pickle
import streamlit as st
import numpy as np

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model_path = os.path.join(
    BASE_DIR,
    "model.pkl"
)

with open(model_path, "rb") as f:
    model = pickle.load(f)
    

st.title("Student Performance Prediction")
writing_score = st.number_input(
    "Enter Writing Score",
    min_value=0,
    max_value=100
)
if st.button("Predict Reading Score"):

    if writing_score == 0:
        st.warning("Please enter a valid writing score.")
    else:

        prediction = model.predict(
            np.array([[writing_score]])
        )

        st.success(
            f"Predicted Reading Score: {prediction[0]}"
        )

        st.balloons()
        