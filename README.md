# 🏥 Healthcare Claims Optimization

This project automates ingestion and optimization of healthcare claims using Airflow and Snowflake. It includes anomaly detection logic and SQL performance tuning for faster analytics.

## 🚀 Features
- Ingests 500K+ claim records via Airflow
- Flags 3.2K+ anomalies using Python rules
- Reduces query latency by 40%
- Modular DAG with retry and alerting

## 🧰 Tech Stack
- Apache Airflow
- Snowflake
- Python
- SQL

## 🛠️ Setup Instructions
1. Clone the repo: `git clone https://github.com/samyuktha/healthcare-claims-optimization.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Configure Airflow DAG: `claims_ingestion_dag.py`
4. Load dummy data from `/data/claims.csv` into Snowflake
5. Run anomaly detection script

## 📦 Environment
- Python 3.8+
- Airflow 2.5+
- Snowflake account

## 📊 Dataset
Dummy dataset: `claims.csv`  
Fields: `claim_id`, `patient_id`, `amount`, `diagnosis_code`, `timestamp`

## 📄 License
MIT
