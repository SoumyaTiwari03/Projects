import streamlit as st
import pandas as pd
import joblib

st.title("Taxi Fare Prediction")

model = joblib.load("best_taxi_model.pkl")

pickup_zone = st.selectbox("Pickup Zone", ["North","South","East","West","Central"])
vehicle_type = st.selectbox("Vehicle Type", ["Sedan","SUV","Mini","Auto"])
passenger_count = st.number_input("Passenger Count", 1, 10, 1)
trip_distance_km = st.number_input("Trip Distance (km)", 0.0, 500.0, 5.0)
trip_duration_min = st.number_input("Trip Duration (min)", 1.0, 1000.0, 15.0)
payment_method = st.selectbox("Payment Method", ["Cash","Card","UPI"])
hour = st.slider("Hour", 0, 23, 12)
day = st.slider("Day", 1, 31, 1)
month = st.slider("Month", 1, 12, 1)
weekday = st.selectbox(
    "Weekday",
    ["Monday", "Tuesday", "Wednesday",
     "Thursday", "Friday", "Saturday", "Sunday"]
)
weekday_map = {
    "Monday": 0,
    "Tuesday": 1,
    "Wednesday": 2,
    "Thursday": 3,
    "Friday": 4,
    "Saturday": 5,
    "Sunday": 6
}


if st.button("Predict Fare"):
    data = pd.DataFrame({
        "pickup_zone":[pickup_zone],
        "vehicle_type":[vehicle_type],
        "passenger_count":[passenger_count],
        "trip_distance_km":[trip_distance_km],
        "trip_duration_min":[trip_duration_min],
        "payment_method":[payment_method],
        "hour":[hour],
        "day":[day],
        "month":[month],
        "weekday": [weekday_map[weekday]]
        
        })
    

    pred = model.predict(data)[0]
    st.success(f"Estimated Fare: ₹{pred:.2f}")
    st.snow()
