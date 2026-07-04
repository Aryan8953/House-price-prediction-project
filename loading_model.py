import pandas as pd
import joblib
model=joblib.load('model.pkl')

model = joblib.load("house_price_model.pkl")

while True:
    area=float(input("enter area of house in square feet"))
    input_data = pd.DataFrame({
        "Area": [area]
    })

    predicted_price = model.predict(input_data)

    print(f"\n🏠 Predicted House Price: ₹{predicted_price[0]:,.2f}")
    

