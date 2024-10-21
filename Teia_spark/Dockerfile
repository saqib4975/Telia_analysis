FROM apache/airflow:2.9.3-python3.11

# Switch to root to install system packages
USER root

# Install necessary packages
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    gcc \
    python3-dev \
    default-jdk \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set the JAVA_HOME environment variable (adjusting path for default-jdk)
ENV JAVA_HOME /usr/lib/jvm/java-17-openjdk-amd64

# Switch back to the airflow user
USER airflow

# Install necessary Python packages
RUN pip install --no-cache-dir \
    apache-airflow-providers-apache-spark==4.1.5 \
    pyspark==3.4.1 \
    apache-airflow-providers-openlineage==1.8.0 \
    apache-airflow-providers-docker==3.7.5

RUN pip install apache-airflow-providers-openlineage==1.8.0

#spark connect
#RUN pip install --no-cache-dir pip install apache-airflow-providers-docker


#
#RUN pip install \
#    apache-airflow-providers-apache-spark \
#    pyspark \
#    apache-airflow-providers-openlineage>=1.8.0

#FROM apache/airflow:2.7.1-python3.11
#
#USER root
#
## Update package lists and install required packages
#RUN apt-get update && \
#    apt-get install -y --no-install-recommends \
#    gcc \
#    python3-dev \
#    default-jdk && \
#    apt-get clean && \
#    rm -rf /var/lib/apt/lists/*
#
## Set JAVA_HOME environment variable
#ENV JAVA_HOME /usr/lib/jvm/java-11-openjdk-amd64
#
#USER airflow
#
## Install additional Airflow providers and packages
#RUN pip install \
#    apache-airflow-providers-apache-spark \
#    pyspark \
#    apache-airflow-providers-openlineage>=1.8.0