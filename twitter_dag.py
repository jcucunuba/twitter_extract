from datetime import datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.util.dates import days_ago
from datetime import timedelta
from twitter_etl import run_twitter_etl 

default_arg = {
    'owner': 'airflow',
    'depens_on_past': False,
    'start_date': datetime(2020, 11, 8),
    'email': ['{inset_your_email}'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retries_delay': timedelta(minutes=1)
}

dag = DAG(
    'twitter_dag',
    default_arg = default_arg,
    descrition = 'My Fisrt Dag, etl code'
)

run_etl = PythonOperator(
    task_id = 'coomplete_twtter_etl',
    python_callable = run_twitter_etl,
    dag = dag
)

run_etl

## Al final hay que cambiar la ruta con la ruta del bucket en S3 -- Actualmente esta en local.