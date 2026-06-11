import streamlit as st
import pickle
import numpy as np

with open("model.pkl", "rb") as f:
    model=pickle.load(f)
# model = pickle.load(open("model.pkl", "rb"))
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
        