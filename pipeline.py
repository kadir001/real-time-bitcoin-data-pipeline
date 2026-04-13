import logging
import os

from src.extract import extract
from src.transform import transform
from src.load import load
from config import LOG_PATH

# Zorg dat logs folder bestaat
os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename=LOG_PATH,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


if __name__ == "__main__":
    try:
        logging.info("Pipeline gestart")

        data = extract()
        df = transform(data)
        load(df)

        print(df.to_string())

        logging.info("Pipeline succesvol afgerond")

    except Exception as e:
        logging.error(f"Fout: {e}")
        raise
