from airflow import DAG
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 1),
    'email': ['your_email@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'simple_spark_etl_dag',
    default_args=default_args,
    description='Simple DAG for PySpark ETL job',
    schedule='@daily',
    catchup=False,
)

spark_etl_task = SparkSubmitOperator(
    task_id='spark_etl_job',
    application='/jobs/python/Data_analysis.py',
    conn_id='spark_default',
    dag=dag,
)