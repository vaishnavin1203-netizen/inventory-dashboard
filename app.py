import streamlit as st
import pandas as pd

df = pd.read_csv("b2b_inventory_dataset.csv")

st.title("📊 B2B Inventory Dashboard")

# KPIs
total_sales = df["Sales"].sum()
current_stock = df["Stock_Level"].sum()
low_stock_items = df[df["Stock_Level"] < df["Reorder_Level"]].shape[0]
forecast_demand = round(df["Sales"].mean(), 2)

st.subheader("Key Performance Indicators")
st.write("Total Sales:", total_sales)
st.write("Current Stock:", current_stock)
st.write("Low Stock Items:", low_stock_items)
st.write("Forecast Demand:", forecast_demand)

# Sales Trend
st.subheader("Sales Trend")
df["Date"] = pd.to_datetime(df["Date"], errors='coerce')
sales_trend = df.groupby("Date")["Sales"].sum()
st.line_chart(sales_trend)

# Stock by Category
st.subheader("Stock Levels by Category")
stock_category = df.groupby("Category")["Stock_Level"].sum()
st.bar_chart(stock_category)

# Region-wise Sales
st.subheader("Region-wise Sales")
region_sales = df.groupby("Region")["Sales"].sum()
st.bar_chart(region_sales)