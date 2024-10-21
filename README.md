# Telia_analysis

This project is a data engineering pipeline built with Apache Airflow and Apache Spark. It processes telecommunication data from multiple sources (GSM, LTE, UMTS, and site data) using Spark jobs orchestrated by Airflow
.
Project Structure

Telia_spark/
├── dags/                  # Airflow DAG files
├── data/                  # Raw data files
│   ├── gsm/
│   ├── lte/
│   ├── site/
│   └── umts/
├── jobs/                  # Spark job scripts
│   └── python/
├── logs/                  # Airflow logs
│   ├── dag_processor_manager/
│   └── scheduler/
└── venv/                  # Python virtual environment


Prerequisites

git clone https://github.com/saqib4975/Telia_analysis.git
cd Telia_spark

Docker
Docker Compose

Build and start the Docker containers

Usage
Airflow

Access the Airflow web interface at http://localhost:8081.
Log in with the credentials set in your docker-compose.yml file.
DAGs are automatically loaded from the dags/ directory.


