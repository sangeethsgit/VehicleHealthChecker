import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("Mileage vs Tyre Condition")

df = pd.read_csv(r"D:\CDAC Internship\DOCS\vehicle_dataset_1000-2.csv")
df.columns = df.columns.str.strip()


fig, ax = plt.subplots()
sns.histplot(data=df, x="Mileage (kmpl)", hue="Tyre Condition", multiple="stack",ax=ax)
st.pyplot(fig)
