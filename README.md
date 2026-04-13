# Real-Time Bitcoin Data Pipeline

This project is a real-time data engineering pipeline that fetches live Bitcoin prices, stores them, and visualizes trends through a dashboard.

## 🚀 Features

- Real-time API data ingestion
- Data transformation and processing
- Time-series storage using SQLite
- Incremental data loading
- Logging system
- Data visualization (matplotlib)
- Interactive dashboard (Streamlit)

## 🧱 Architecture

API → Extract → Transform → Load → Database → Dashboard

## ⚙️ How to Run

```bash
pip install -r requirements.txt
python3 pipeline.py
streamlit run dashboard.py
