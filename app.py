import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title
st.title("E-Challan Dashboard")

# Load data
df = pd.read_csv("echallan_daily_data.csv")

# Convert date column
df["date"] = pd.to_datetime(df["date"])

# ---- KPI Cards ----
total_challan = df["totalChallan"].sum()
total_pending = df["pendingChallan"].sum()
total_disposed = df["disposedChallan"].sum()

col1, col2, col3 = st.columns(3)

col1.metric("Total Challan", total_challan)
col2.metric("Total Pending", total_pending)
col3.metric("Total Disposed", total_disposed)

st.write("---")

# ---- Line Chart ----
st.subheader("Challan Trend Over Time")

fig, ax = plt.subplots()
ax.plot(df["date"], df["totalChallan"])
ax.set_xlabel("Date")
ax.set_ylabel("Total Challan")

st.pyplot(fig)

# ---- Top Days with Highest Challan ----
st.subheader("Top 10 Highest Challan Days")

top_days = df.sort_values("totalChallan", ascending=False).head(10)
st.dataframe(top_days)
