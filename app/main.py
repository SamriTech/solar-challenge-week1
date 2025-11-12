import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from utils import load_data

st.set_page_config(page_title="Solar Data Dashboard", layout="wide")

st.title("☀️ Solar Data Comparison Dashboard")

# --- Sidebar ---
st.sidebar.header("Settings")
country = st.sidebar.selectbox("Select Country", ["Benin", "SierraLeone", "Togo"])
metric = st.sidebar.selectbox("Select Metric", ["GHI", "DNI", "DHI"])

# --- Load Data ---
df = load_data(country)

# --- Display Summary ---
st.subheader(f"Summary Statistics for {country}")
st.write(df[[metric]].describe())

# --- Boxplot ---
st.subheader(f"{metric} Distribution")
fig, ax = plt.subplots(figsize=(7, 4))
sns.boxplot(y=df[metric], ax=ax, color="skyblue")
ax.set_ylabel(f"{metric} (W/m²)")
st.pyplot(fig)

# --- Line Plot (Optional) ---
st.subheader(f"{metric} over Time")
fig2, ax2 = plt.subplots(figsize=(8, 4))
ax2.plot(df["Timestamp"], df[metric], color="orange")
ax2.set_xlabel("Time")
ax2.set_ylabel(f"{metric} (W/m²)")
st.pyplot(fig2)

st.success("✅ Dashboard loaded successfully!")
