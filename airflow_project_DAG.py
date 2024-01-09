from datetime import timedelta, datetime
from airflow import DAG
from airflow.operator.python_operator import PythonOperator 
from airflow.utils.dates import days_ago 
from dataset import run_etl

default_args ={
    'owner':'airflow',
    'start_date': datetime(2024,7,1),
    'retries':1,
    'retyr_delay':timedelta(minutes=1)
}

dag= DAG(
    'project_dag',
    default_args= default_args,
    description = 'Airflow Project DAG'
)

running_etl_fun = PythonOperator(
    task_id = 'etl_task_1',
    python_callable=run_etl,
    dag=dag,
)

running_etl_fun