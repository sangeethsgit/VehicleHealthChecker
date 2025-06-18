import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("Engine Health Score vs Oil Level")

df = pd.read_csv(r"D:\CDAC Internship\DOCS\vehicle_dataset_1000.csv")
df.columns = df.columns.str.strip()


fig, ax = plt.subplots()
sns.scatterplot(data=df, x="Oil Level (L)", y="Engine Health Score", ax=ax)
st.pyplot(fig)