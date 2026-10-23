# Importando bibliotecas
import requests
from airflow import DAG
from datetime import date, datetime, timedelta
from airflow.operators.python import PythonOperator


# Criando a função para extrair os dados da API
def extrair_dados(endpoint):
    response = requests.get(endpoint, timeout=30)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Erro ao extrair os dados do {endpoint}")
        return None
    
# Caminho dos dados
endpoint_user = "https://dummyjson.com/users/"
endpoint_product = "https://dummyjson.com/products/"

# Argumentos da DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}


# Definições da DAG
with DAG(
    dag_id = 'teste_id',
    default_args = default_args,
    description = "DAG teste em python",
    schedule_interval = '@daily',
    start_date = datetime(2021, 12, 01),
    catchup = False
) as dag:

#Tasks
    t_users = PythonOperator (
    task_id = 't_users',
    python_callable = extrair_dados,
    op_kwargs = {"endpoint": endpoint_user}
)
    t_products = PythonOperator(
    task_id = 't_products',
    python_callable = extrair_dados,
    op_kwargs = {"endpoint": endpoint_product},
)

# Definição da ordem de execução das tarefas
[t_users, t_products]