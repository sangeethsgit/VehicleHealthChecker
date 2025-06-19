import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

st.title(":green[Vehicle Dashboard]")
st.title("Vehicle Health Prediction")
df = pd.read_csv(r"D:\CDAC Internship\DOCS\vehicle_dataset_1000-2.csv")
df.columns = df.columns.str.strip()
X = df[['Oil Level (L)', 'Vehicle Load (kg)', 'Battery Voltage (V)', 'Tyre Condition']]
y = df[['Mileage (kmpl)', 'Engine Health Score', 'Time Until Next Service (days)']]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)

st.header("Vehicle Parameters")
oil_level = st.number_input("Oil Level (L)",min_value=0.0,max_value=10.0)
vehicle_load = st.number_input("Vehicle Load (kg)",min_value=0,max_value=5000)
battery_voltage = st.number_input("Battery Voltage (V)",min_value=0.0,max_value=15.0)
tyre_condition = st.selectbox("Tyre Condition", options=[0, 1], format_func=lambda x: "Bad" if x == 0 else "Good")


if st.button("Predict Health Parameters"):
    inpdat = pd.DataFrame([[oil_level, vehicle_load, battery_voltage, tyre_condition]],
                              columns=['Oil Level (L)', 'Vehicle Load (kg)', 'Battery Voltage (V)', 'Tyre Condition'])
    
    prediction = model.predict(inpdat)[0]
    
    st.subheader("Predicted Results:")
    st.write(f"**Mileage (kmpl):** {prediction[0]:.2f}")
    st.write(f"**Engine Health Score:** {prediction[1]:.2f}")
    st.write(f"**Time Until Next Service (days):** {int(prediction[2])}")
