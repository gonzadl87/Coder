
from datetime import datetime, timedelta
from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator


default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'cripto_exchange_dag',
    default_args=default_args,
    schedule=timedelta(days=1),  # Programa la ejecución del DAG
)

run_script = DockerOperator(
    task_id='run_script',
    image='script_cripto_exchanges',  
    dag=dag,
)

run_script

