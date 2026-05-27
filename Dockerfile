FROM astrocrpublic.azurecr.io/runtime:3.2-4

# Copy churn project files for the ML pipeline
COPY churn/ /usr/local/airflow/include/churn/
