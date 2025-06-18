import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("Time until next service vs Oil Level (L)")

df = pd.read_csv(r"D:\CDAC Internship\DOCS\vehicle_dataset_1000.csv")
df.columns = df.columns.str.strip()


fig, ax = plt.subplots()
sns.scatterplot(data=df, x="Oil Level (L)", y="Time Until Next Service (days)", ax=ax)
st.pyplot(fig)