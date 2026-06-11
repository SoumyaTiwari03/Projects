import streamlit as st
import pandas as pd
import pickle

model = pickle.load(
    open("walmart_sales_model.pkl", "rb")
)

st.title("Walmart Sales Prediction")

store = st.number_input(
    "Store Number",
    min_value=1,
    value=1
)

holiday = st.selectbox(
    "Holiday Week",
    [0, 1]
)

temperature = st.number_input(
    "Temperature",
    value=70.0
)

fuel_price = st.number_input(
    "Fuel Price",
    value=3.0
)

cpi = st.number_input(
    "CPI",
    value=200.0
)

unemployment = st.number_input(
    "Unemployment Rate",
    value=7.0
)

year = st.selectbox(
    "Year",
    [2010, 2011, 2012]
)

if st.button("Predict Sales"):

    if fuel_price <= 0:
        st.error(
            "Fuel Price must be greater than 0"
        )

    elif unemployment > 15:
        st.warning(
            "Very high unemployment entered"
        )

    else:

        data = pd.DataFrame({
            "Store": [store],
            "Holiday_Flag": [holiday],
            "Temperature": [temperature],
            "Fuel_Price": [fuel_price],
            "CPI": [cpi],
            "Unemployment": [unemployment],
            "Year": [year]
        })

        prediction = model.predict(data)[0]

        st.success(
            "Prediction Generated Successfully!"
        )

        st.metric(
            "Predicted Weekly Sales",
            f"{prediction:,.2f}"
        )

        st.snow()