# https://airflow.apache.org/docs/apache-airflow/stable/start.html

# airflow needs a home, ~/airflow is the default,
# but you can lay foundation somewhere else if you prefer
# (optional)
export AIRFLOW_HOME=~/study/learning-airflow

# initialize the database
airflow db init

# create user
airflow users create \
    --username admin \
    --firstname Peter \
    --lastname Parker \
    --role Admin \
    --email spiderman@superhero.org

# start the web server, default port is 8080
airflow webserver --port 8081 -D

# start the scheduler
airflow scheduler