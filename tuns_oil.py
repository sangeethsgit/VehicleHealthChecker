import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import seaborn as sns

df=pd.read_csv(r"D:\CDAC Internship\DOCS\vehicle_dataset_1000-2.csv")
df['Load Bin'] = pd.cut(df['Oil Level (L)'], bins=20)

grouped = df.groupby('Load Bin').agg({
    'Oil Level (L)': 'mean',
    'Time Until Next Service (days)': 'mean'
})

fig, ax = plt.subplots()
sns.lineplot(
    x='Oil Level (L)', 
    y='Time Until Next Service (days)', 
    data=grouped, 
    ax=ax
)

ax.set_xlabel('Average Oil Level per Bin (kg)')
ax.set_ylabel('Average Time Until Next Service (days)')
st.pyplot(fig)
