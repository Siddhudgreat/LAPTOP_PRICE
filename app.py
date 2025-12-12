import streamlit as st
import pandas as pd
import pickle

# Load model & encoders
model = pickle.load(open("laptop_model.pkl", "rb"))
encoders = pickle.load(open("encoders.pkl", "rb"))

st.title("💻 Laptop Price Prediction App")

st.write("Enter laptop details to predict the approximate price.")

# Input Fields
brand = st.selectbox("Brand", encoders["brand"].classes_)
processor = st.selectbox("Processor", encoders["processor"].classes_)
ram = st.selectbox("RAM (GB)", [4, 8, 16, 32])
storage = st.selectbox("Storage (GB)", [256, 512, 1024])
gpu = st.selectbox("GPU", encoders["gpu"].classes_)
display = st.selectbox("Display Size (inches)", [13.3, 14.0, 15.6, 16.0])
battery = st.slider("Battery Life (hours)", 3, 12)
weight = st.slider("Weight (kg)", 1.2, 3.0, step=0.1)

# Prepare input
input_data = pd.DataFrame({
    "Brand": [encoders["brand"].transform([brand])[0]],
    "Processor": [encoders["processor"].transform([processor])[0]],
    "RAM(GB)": [ram],
    "Storage(GB)": [storage],
    "GPU": [encoders["gpu"].transform([gpu])[0]],
    "DisplaySize": [display],
    "BatteryLife": [battery],
    "Weight": [weight]
})

# Predict
if st.button("Predict Price"):
    prediction = model.predict(input_data)[0]
    st.success(f"💰 Estimated Laptop Price: ₹ {int(prediction)}")
