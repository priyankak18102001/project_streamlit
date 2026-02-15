import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

st.set_page_config(page_title="E-Challan Dashboard", layout="wide")

st.title("E-Challan Dashboard")

# Load data safely
file_path = os.path.join(os.path.dirname(__file__), "echallan_daily_data.csv")
df = pd.read_csv(file_path)
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
st.subheader("Challan Trend (Line Chart)")
st.line_chart(df.set_index("date")[["totalChallan"]])

# ---- Bar Chart ----
st.subheader("Pending vs Disposed (Bar Chart)")
bar_data = df[["pendingChallan", "disposedChallan"]].sum()
st.bar_chart(bar_data)

# ---- Area Chart ----
st.subheader("Challan Area Chart")
st.area_chart(df.set_index("date")[["totalChallan"]])

# ---- Pie Chart ----
st.subheader("Pending vs Disposed (Pie Chart)")

pie_values = [
    df["pendingChallan"].sum(),
    df["disposedChallan"].sum()
]

labels = ["Pending", "Disposed"]

fig, ax = plt.subplots()
ax.pie(pie_values, labels=labels, autopct="%1.1f%%")
ax.axis("equal")

st.pyplot(fig)

st.subheader("Monthly Challan Trend")

df["month"] = df["date"].dt.to_period("M").astype(str)
monthly_data = df.groupby("month")["totalChallan"].sum()

st.bar_chart(monthly_data)

st.subheader("Top 10 Highest Challan Days")

top_days = df.sort_values("totalChallan", ascending=False).head(10)
st.bar_chart(top_days.set_index("date")["totalChallan"])

st.subheader("Challan Distribution")

import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.hist(df["totalChallan"], bins=20)
ax.set_xlabel("Challan Count")
ax.set_ylabel("Frequency")

st.pyplot(fig)

st.subheader("Cumulative Challan Growth")

df["cumulative"] = df["totalChallan"].cumsum()
st.line_chart(df.set_index("date")["cumulative"])

st.subheader("Pending vs Disposed Trend")

st.line_chart(df.set_index("date")[["pendingChallan","disposedChallan"]])


# ---- Data Table ----
st.subheader("Dataset Preview")
st.dataframe(df)
