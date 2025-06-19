import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import seaborn as sns

df=pd.read_csv(r"D:\CDAC Internship\DOCS\vehicle_dataset_1000-2.csv")
df['Load Bin'] = pd.cut(df['Battery Voltage (V)'], bins=20)

grouped = df.groupby('Load Bin').agg({
    'Battery Voltage (V)': 'mean',
    'Time Until Next Service (days)': 'mean'
})

fig, ax = plt.subplots()
sns.lineplot(
    x='Battery Voltage (V)', 
    y='Time Until Next Service (days)', 
    data=grouped, 
    ax=ax
)

ax.set_xlabel('Average Battery Voltage per Bin (kg)')
ax.set_ylabel('Average Time Until Next Service (days)')
st.pyplot(fig)
