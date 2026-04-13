import requests
import logging
from config import API_URL


def extract():
    logging.info("Start extract (API call)")

    response = requests.get(API_URL)

    if response.status_code != 200:
        raise Exception("API request failed")

    data = response.json()

    logging.info(f"API response: {data}")

    return data
