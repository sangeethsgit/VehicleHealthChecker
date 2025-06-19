import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("Engine Health Score vs Tyre Condition")

df = pd.read_csv(r"D:\CDAC Internship\DOCS\vehicle_dataset_1000-2.csv")
df.columns = df.columns.str.strip()


fig, ax = plt.subplots()
sns.histplot(data=df, x="Engine Health Score", hue="Tyre Condition", multiple="stack",ax=ax)
st.pyplot(fig)