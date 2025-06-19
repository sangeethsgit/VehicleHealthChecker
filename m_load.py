import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import seaborn as sns

df=pd.read_csv(r"D:\CDAC Internship\DOCS\vehicle_dataset_1000-2.csv")
df['Load Bin'] = pd.cut(df['Vehicle Load (kg)'], bins=20)

grouped = df.groupby('Load Bin').agg({
    'Vehicle Load (kg)': 'mean',
    'Mileage (kmpl)': 'mean'
})

fig, ax = plt.subplots()
sns.lineplot(
    x='Vehicle Load (kg)', 
    y='Mileage (kmpl)', 
    data=grouped, 
    ax=ax
)

ax.set_xlabel('Average Vehicle Load per Bin (kg)')
ax.set_ylabel('Average Mileage (kmpl)')
st.pyplot(fig)
