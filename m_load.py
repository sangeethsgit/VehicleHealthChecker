import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("Mileage vs Vehicle Load")

df = pd.read_csv(r"D:\CDAC Internship\DOCS\vehicle_dataset_1000.csv")
df.columns = df.columns.str.strip()


fig, ax = plt.subplots()
sns.scatterplot(data=df, x="Vehicle Load (kg)", y="Mileage (kmpl)", ax=ax)
st.pyplot(fig)