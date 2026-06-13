import streamlit as st
import pandas as pd
import pickle
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model_path = os.path.join(
    BASE_DIR,
    "linear_regression_model.pkl"
)

with open(model_path, "rb") as f:
    model = pickle.load(f)

    scaler_path = os.path.join(
    BASE_DIR,
    "scaler.pkl"
)

with open(scaler_path, "rb") as f:
    scaler = pickle.load(f)

    
st.title("House Price Prediction")

area = st.number_input(
    "Area",
    min_value=100,
    value=1000
)

bedrooms = st.slider(
    "Bedrooms",
    1,
    10,
    3
)

bathrooms = st.slider(
    "Bathrooms",
    1,
    10,
    2
)

stories = st.slider(
    "Stories",
    1,
    5,
    2
)

parking = st.slider(
    "Parking Spaces",
    0,
    5,
    1
)

mainroad = st.selectbox(
    "Main Road Access",
    ["Available", "Not Available"]
)

guestroom = st.selectbox(
    "Guest Room",
    ["Available", "Not Available"]
)

basement = st.selectbox(
    "Basement",
    ["Available", "Not Available"]
)

hotwaterheating = st.selectbox(
    "Hot Water Heating",
    ["Available", "Not Available"]
)

airconditioning = st.selectbox(
    "Air Conditioning",
    ["Available", "Not Available"]
)

prefarea = st.selectbox(
    "Preferred Area",
    ["Available", "Not Available"]
)

furnishingstatus = st.selectbox(
    "Furnishing Status",
    [
        "Furnished",
        "Semi-Furnished",
        "Unfurnished"
    ]
)

if st.button("Predict Price"):

    if area <= 0:
        st.error("Please enter a valid area")

    else:

        if area < 1000:
            st.warning(
                "Area is unusually small"
            )

        mainroad = 1 if mainroad == "Available" else 0
        guestroom = 1 if guestroom == "Available" else 0
        basement = 1 if basement == "Available" else 0
        hotwaterheating = 1 if hotwaterheating == "Available" else 0
        airconditioning = 1 if airconditioning == "Available" else 0
        prefarea = 1 if prefarea == "Available" else 0

        furnishing_map = {
            "Furnished": 0,
            "Semi-Furnished": 1,
            "Unfurnished": 2
        }

        furnishingstatus = furnishing_map[
            furnishingstatus
        ]

        features = pd.DataFrame({
            "area": [area],
            "bedrooms": [bedrooms],
            "bathrooms": [bathrooms],
            "stories": [stories],
            "mainroad": [mainroad],
            "guestroom": [guestroom],
            "basement": [basement],
            "hotwaterheating": [hotwaterheating],
            "airconditioning": [airconditioning],
            "parking": [parking],
            "prefarea": [prefarea],
            "furnishingstatus": [furnishingstatus]
        })

        prediction = model.predict(
            features
        )[0]

        st.success(
            "Prediction Generated Successfully"
        )

        st.metric(
            "Estimated House Price",
            f"₹ {prediction:,.0f}"
        )

        st.balloons()