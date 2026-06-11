import streamlit as st
import pandas as pd
import pickle
from streamlit_extras.let_it_rain import rain


model = pickle.load(
    open(
        "insurance_model.pkl",
        "rb"
    )
)

st.title("Insurance Charges Prediction")

age = st.number_input(
    "Age",
    min_value=18,
    max_value=100,
    step = 25
)

sex = st.selectbox(
    "Gender",
    ["male", "female"]
)

bmi = st.number_input(
    "BMI",
    value=25.0
)

children = st.number_input(
    "Number of Children",
    min_value=0,
    max_value=10,
    step=0
)

smoker = st.selectbox(
    "Smoker",
    ["yes", "no"]
)

region = st.selectbox(
    "Region",
    [
        "southwest",
        "southeast",
        "northwest",
        "northeast"
    ]
)
if st.button("Predict Charges"):

    if bmi <= 0:
        st.error("BMI must be greater than 0")

    else:

        if smoker == "yes":
            st.warning(
                "Smoking can significantly increase insurance charges"
            )

        data = pd.DataFrame({
            "age": [age],
            "sex": [sex],
            "bmi": [bmi],
            "children": [children],
            "smoker": [smoker],
            "region": [region]
        })

        prediction = model.predict(data)[0]

        st.success("Prediction Generated Successfully!")

        st.metric(
            "Estimated Insurance Charges",
            f"${prediction:,.2f}"
        )

        # Rain Money
        rain(
            emoji="💰",
            font_size=40,
            falling_speed=10,
            animation_length="3"
        )