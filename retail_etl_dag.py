from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from kafka.kafka_producer import publish_sales_events
from kafka.kafka_consumer import consume_sales_events
from etl.transform import transform_sales_data

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'retries': 1,
}

with DAG('retail_etl_pipeline', default_args=default_args, schedule_interval='@daily') as dag:
    publish_task = PythonOperator(
        task_id='publish_sales_events',
        python_callable=publish_sales_events,
        op_kwargs={'file_path': '/path/to/sales.csv'}
    )

    consume_task = PythonOperator(
        task_id='consume_sales_events',
        python_callable=consume_sales_events
    )

    publish_task >> consume_task
