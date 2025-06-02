from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import sys
import os
from dotenv import load_dotenv


load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', '.env'))

# Adjust this path to the folder containing your `my_app` folder
base_dir = os.getenv("BASE_PATH")

if base_dir and base_dir not in sys.path:
    sys.path.insert(0, base_dir)
print(f"Base directory added to sys.path: {base_dir}")    

from my_app.datasets import gathering_datasets
    
with DAG(
    'ecommerce_sales_data_engineering',
    start_date=datetime(2023, 1, 1),
    schedule_interval='@hourly',
    catchup=True,
    tags=['ecommerce']  # اضافه کردن تگ برای مدیریت بهتر UI
) as dag:

    run_data = PythonOperator(
        task_id='run_data',
        python_callable=gathering_datasets
    )