# Streaming Data Pipeline with Apache Kafka, Spark, and Airflow

This repository contains the implementation of a streaming data pipeline that extracts data from popular streaming platforms (Netflix, Hulu, Amazon Prime, Disney+), processes it in real-time, and visualizes the results on a live dashboard. The pipeline leverages modern data engineering tools like Apache Kafka, Apache Spark, Apache Airflow, and a real-time database.

## Features

- **Data Extraction**: Parallel extraction of data from multiple streaming platforms.
- **Real-Time Processing**: Processing the data using Apache Spark Streaming.
- **Workflow Management**: Scheduling and managing data producers with Apache Airflow.
- **Streaming Data Visualization**: Visualizing processed data on a live dashboard.
- **Database Integration**: Storing processed data into a database table.

## Architecture

1. **Data Producers**: Extract data from streaming platforms and send it to Kafka topics.
2. **Apache Kafka**: Acts as the messaging queue for data streams.
3. **Apache Airflow**: Manages and schedules data producers to run in parallel.
4. **Apache Spark**: Processes data in real time from Kafka topics.
5. **Database**: Stores processed data for querying and visualization.
6. **Dashboard**: Displays real-time streaming data insights.

## Prerequisites

- **Docker**: To containerize the services.
- **Apache Kafka**: For data streaming.
- **Apache Spark**: For data processing.
- **Apache Airflow**: For workflow orchestration.
- **Database**: Any compatible database (e.g., PostgreSQL, MySQL, or MongoDB).
- **Dashboard Tool**: E.g., Grafana or a custom-built dashboard.

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/streaming-data-pipeline.git
   cd streaming-data-pipeline
   ```

2. Start the services using Docker Compose:
   ```bash
   docker-compose up
   ```

3. Configure Apache Airflow:
   - Access the Airflow UI at `http://localhost:8080`.
   - Import the provided DAGs to manage data producers.

4. Access Kafka:
   - Kafka is available at `localhost:9092`.
   - Use Kafka topics to monitor incoming data.

5. Configure the database:
   - Ensure the database is running and accessible.
     

## Workflow

1. Airflow triggers data producers to extract data from streaming platforms.
2. Data is published to Kafka topics.
3. Spark processes data in real-time and streams the results into the database.
4. The dashboard visualizes the processed data in real-time.

## Folder Structure

```plaintext
.
├── GraduationProjectDag/                 # Airflow DAGs
├── kafka_spark_consumer/                # Kafka configuration and scripts
├── sparkNotebook/                # Spark streaming application
├── movies dashboard/            # Dashboard setup and configuration
├── Producers/             # Database Platforms
├── Pipeline.png/         # Data Pipeline
└── README.md             # Project documentation
```

## Contributing

Contributions are welcome! Feel free to fork this repository and submit pull requests for improvements or new features.


## Acknowledgments

- [Apache Kafka](https://kafka.apache.org/)
- [Apache Spark](https://spark.apache.org/)
- [Apache Airflow](https://airflow.apache.org/)

## Contact

For questions or support, contact [mariammahmod035@gmail.com].

Happy streaming!




