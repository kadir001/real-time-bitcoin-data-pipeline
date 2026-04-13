import sqlite3
import pandas as pd
import streamlit as st

DB_PATH = "data/processed/prices.db"

st.title("📈 Bitcoin Price Dashboard")

# Data ophalen
conn = sqlite3.connect(DB_PATH)

query = "SELECT * FROM bitcoin_prices"
df = pd.read_sql(query, conn)

conn.close()

# Sorteren
df = df.sort_values("timestamp")

# Toon laatste prijs
latest_price = df["price_usd"].iloc[-1]
st.metric(label="Current Bitcoin Price (USD)", value=latest_price)

# Grafiek
st.line_chart(df.set_index("timestamp")["price_usd"])
