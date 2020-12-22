# -*- coding: utf-8 -*-
# -----------------------------------------------------------
# Debugging a Dag project
# https://airflow.apache.org/docs/apache-airflow/stable/executor/debug.html
# -----------------------------------------------------------
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.state import State
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
    dag_id='debug_airflow',
    default_args=default_args,
    schedule_interval=None,
    catchup=False
)


def task_one():
    message = 'Running the task one'
    print(message)


def task_two():
    message = 'Running the task two'
    print(message)


def task_three():
    message = 'Running the task tree'
    print(message)


t1 = PythonOperator(
    task_id='t1',
    python_callable=task_one,
    dag=dag
)

t2 = PythonOperator(
    task_id='t2',
    python_callable=task_two,
    dag=dag
)

t3 = PythonOperator(
    task_id='t3',
    python_callable=task_three,
    dag=dag
)

t1 >> t2 >> t3

if __name__ == '__main__':
    dag.clear(dag_run_state=State.NONE)
    dag.run()
