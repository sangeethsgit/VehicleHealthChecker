import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("Engine Health Score vs Vehicle Load")

df = pd.read_csv(r"D:\CDAC Internship\DOCS\vehicle_dataset_1000.csv")
df.columns = df.columns.str.strip()


fig, ax = plt.subplots()
sns.scatterplot(data=df, x="Vehicle Load (kg)", y="Engine Health Score", ax=ax)
st.pyplot(fig)