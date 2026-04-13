import pandas as pd
import logging
from datetime import datetime


def transform(data):
    logging.info("Start transform")

    price = data["bitcoin"]["usd"]
    timestamp = datetime.utcnow()

    df = pd.DataFrame([{
        "timestamp": timestamp,
        "price_usd": price
    }])

    return df
