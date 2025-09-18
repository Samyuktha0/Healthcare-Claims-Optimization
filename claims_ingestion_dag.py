from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
import snowflake.connector

def ingest_to_snowflake():
    conn = snowflake.connector.connect(...)
    cursor = conn.cursor()
    cursor.execute("PUT file://claims.csv @%claims_table")
    cursor.execute("COPY INTO claims_table FROM @%claims_table FILE_FORMAT = (TYPE = CSV)")

dag = DAG('claims_ingestion', start_date=datetime(2023, 1, 1), schedule_interval='@daily')
ingest_task = PythonOperator(task_id='ingest', python_callable=ingest_to_snowflake, dag=dag)
