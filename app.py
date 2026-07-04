import streamlit as st
import pandas as pd
import joblib

st.title("🏠 House Price Prediction")

try:
    
    model = joblib.load("house_price_model.pkl")

   
    df = pd.read_csv("house_price.csv")

    st.success("Model Loaded Successfully!")

   
    area = st.number_input(
        "Enter House Area (sq ft)",
        min_value=100.0,
        step=50.0
    )

    if st.button("Predict Price"):

        input_data = pd.DataFrame({
            "Area": [area]
        })

        prediction = model.predict(input_data)

        st.success(f"Predicted House Price: ₹{prediction[0]:,.2f}")

except FileNotFoundError:
    st.error("Model or Dataset file not found.")

except Exception as e:
    st.error(f"Error: {e}")