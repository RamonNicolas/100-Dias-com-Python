from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2020, 9, 25),
    "catchup": False,
    "email": ["airflow@airflow.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minute=5),
}
dag = DAG("tutorial", default_args=default_args, schedule_interval=timedelta(1))

t1 = BashOperator(task_id="print_date", bash_command="date", dag=dag)
t2 = BashOperator(task_id="sleep", bash_command="sleep 5", retries=3, dag=dag)

templated_command = """
        {% for i in range(5) %}
            echo "{{ds}}"
            echo "{{ macros.ds_add(ds,7) }}"
            echo "{{ params.myparam }}"
        {% endfor %}

"""
t3 = BashOperator(
    task_id="templated",
    bash_command=templated_command,
    params={"my_param": "Parameter I passed IN"},
    dag=dag,
)


def print_mensagem_ramon():
    print("Fala DEVERS")


t4 = PythonOperator(
    task_id="live_python",
    python_callable=print_mensagem_ramon,
    dag=dag,
)

# t2.set_upstream(t1)
# t3.set_upstream(t1)

t1 >> [t2, t3] >> t4
