import streamlit as st
import pandas as pd
import pickle

# Load Pipeline Model
model = pickle.load(open("models/linear_model.pkl", "rb"))

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
    ["yes", "no"]
)

guestroom = st.selectbox(
    "Guest Room",
    ["yes", "no"]
)

basement = st.selectbox(
    "Basement",
    ["yes", "no"]
)

hotwaterheating = st.selectbox(
    "Hot Water Heating",
    ["yes", "no"]
)

airconditioning = st.selectbox(
    "Air Conditioning",
    ["yes", "no"]
)

prefarea = st.selectbox(
    "Preferred Area",
    ["yes", "no"]
)

furnishingstatus = st.selectbox(
    "Furnishing Status",
    [
        "furnished",
        "semi-furnished",
        "unfurnished"
    ]
)

if st.button("Predict Price"):

    if area <= 0:
        st.error("Area must be greater than zero")

    else:

        if area < 1000:
            st.warning(
                "Area entered is very small"
            )

        data = pd.DataFrame({
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

        prediction = model.predict(data)[0]

        st.success(
            "Prediction Generated Successfully"
        )

        st.metric(
            "Estimated House Price",
            f"{prediction:,.2f}"
        )

        st.balloons()
        st.snow()