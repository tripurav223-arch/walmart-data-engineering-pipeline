from pathlib import Path

from datetime import datetime

from airflow.sdk import DAG
from airflow.providers.standard.operators.bash import BashOperator

# Location of your Walmart dbt project
PROJECT_DIR = str(Path(__file__).resolve().parents[1])

# dbt executable in your existing virtual environment
DBT_EXECUTABLE = str(Path(PROJECT_DIR).parent / ".venv-dbt" / "bin" / "dbt")

# Define the Airflow workflow
with DAG(
    dag_id="walmart_dbt_pipeline",
    start_date=datetime(2026, 10, 1),
    schedule=None,
    catchup=False,
    tags=["walmart", "dbt", "data-engineering"],
) as dag:

    # Step 1: Run Silver transformations
    run_silver = BashOperator(
        task_id="run_silver",
        bash_command=f'"{DBT_EXECUTABLE}" run --select path:models/silver',
        cwd=PROJECT_DIR,
    )

    # Step 2: Build Gold reporting table
    run_gold = BashOperator(
        task_id="run_gold",
        bash_command=f'"{DBT_EXECUTABLE}" run --select fct_order_sales',
        cwd=PROJECT_DIR,
    )

    # Step 3: Run data quality tests
    run_tests = BashOperator(
        task_id="run_dbt_tests",
        bash_command=f'"{DBT_EXECUTABLE}" test',
        cwd=PROJECT_DIR,
    )

    # Execute tasks in order
    run_silver >> run_gold >> run_tests
