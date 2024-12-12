from pyspark.sql import SparkSession
from pyspark.sql.functions import col, json_tuple
import time

# Create a SparkSession
spark = SparkSession.builder \
    .appName("KafkaSparkConsumer") \
    .config("spark.jars.packages", "org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.2") \
    .getOrCreate()

# Define Kafka parameters
kafka_bootstrap_servers = 'localhost:9092'
topic = 'media_titles'

# Read data from Kafka
df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", kafka_bootstrap_servers) \
    .option("subscribe", topic) \
    .option("startingOffsets", "earliest") \
    .option("failOnDataLoss", "false") \
    .load()

# Convert the binary value column to string
df = df.selectExpr("CAST(key AS STRING)", "CAST(value AS STRING)")

# Define the schema of the JSON data
schema = "id STRING, show_id STRING, type STRING, title STRING, director STRING, cast STRING, country STRING, date_added STRING, release_year STRING, rating STRING, duration STRING, listed_in STRING, description STRING, source STRING, total_views INT, user_reviews STRING, user_rating INT"

# Parse the JSON data using json_tuple
df = df.select(
    col("key"),
    json_tuple(col("value"), "id", "show_id", "type", "title", "director", "cast", "country", "date_added", "release_year", "rating", "duration", "listed_in", "description", "source", "total_views", "user_reviews", "user_rating").alias(
        "id", "show_id", "type", "title", "director", "cast", "country", "date_added", "release_year", "rating", "duration", "listed_in", "description", "source", "total_views", "user_reviews", "user_rating"
    )
)


# Start the streaming query and process in micro-batches
def process_micro_batches(df):
    # Define a query to write to a memory sink for periodic processing
    query = df.writeStream \
        .outputMode("append") \
        .format("memory") \
        .queryName("media_titles_temp") \
        .start()

    # Process data in micro-batches
    try:
        while True:
            # Sleep for a while to allow some data to accumulate
            time.sleep(10)
            
            # Read the data from the in-memory table
            micro_batch_df = spark.table("media_titles_temp")
            
            # Print the data to the console
            micro_batch_df.show(truncate=False)

    except KeyboardInterrupt:
        # Stop the streaming query gracefully
        query.stop()

# Start processing
process_micro_batches(df)
