import sqlite3
import logging
from config import DB_PATH


def load(df):
    logging.info("Start load")

    conn = sqlite3.connect(DB_PATH)

    df.to_sql("bitcoin_prices", conn, if_exists="append", index=False)

    conn.close()

    logging.info("Data opgeslagen")
