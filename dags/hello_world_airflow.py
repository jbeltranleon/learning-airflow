# -*- coding: utf-8 -*-
# -----------------------------------------------------------
# Hello World on Airflow
# https://airflow.apache.org/docs/apache-airflow/stable/executor/debug.html
# -----------------------------------------------------------
from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'fredy',
    'start_date': datetime(2020, 12, 21),
    'retries': 1,
    'depends_on_past': False,
    'retry_delay': timedelta(seconds=60)
}

# Our DAG will only run manually, that's why we don't set schedule_interval
dag = DAG(
    dag_id='hello_world',
    default_args=default_args,
    schedule_interval=None,
    catchup=False
)

t1 = BashOperator(
    task_id='hello_world_task',
    bash_command="echo 'Hello World'",
    dag=dag
)
