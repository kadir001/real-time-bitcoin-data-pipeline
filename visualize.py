import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

DB_PATH = "data/processed/prices.db"

# Data ophalen
conn = sqlite3.connect(DB_PATH)

query = "SELECT * FROM bitcoin_prices"
df = pd.read_sql(query, conn)

conn.close()

# Sorteren op tijd
df = df.sort_values("timestamp")

# Plot
plt.figure()
plt.plot(df["timestamp"], df["price_usd"])

plt.xlabel("Time")
plt.ylabel("Bitcoin Price (USD)")
plt.title("Bitcoin Price Over Time")

plt.xticks(rotation=45)
plt.tight_layout()

plt.show()
