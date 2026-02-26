# NYC-Taxi-Analytics-Pipeline-Spark-Databricks-Bronze-Silver-Gold-
End-to-end data engineering project built with PySpark and Databricks using the Bronze–Silver–Gold architecture. This project processes a large NYC taxi dataset (~112M rows, ~10GB) and transforms raw data into clean, analytics-ready datasets for business insights.

🚕 NYC Taxi Analytics Pipeline (Spark | Databricks)
📌 Project Overview

This project builds an end-to-end data engineering pipeline using Apache Spark on Databricks.

We process a 10GB NYC Yellow Taxi dataset (112M+ rows) and transform it through a structured:

Bronze → Silver → Gold architecture

The goal is to simulate a real production-style data pipeline, including ingestion, cleaning, validation, aggregation, and performance optimization.

🗂 Dataset Information

Dataset Name: NYC Yellow Taxi Trip Records (2018)

Source: Kaggle (Original data from NYC Taxi & Limousine Commission)

File Used: taxi_2018.csv

Size: ~10GB

Total Rows: ~112,234,626

Format: CSV

Dataset Contains:

Pickup & dropoff timestamps

Passenger count

Trip distance

Fare breakdown (fare, tax, tip, tolls, etc.)

Payment type

⚙️ How Dataset Was Loaded in Databricks
1️⃣ Upload Dataset to Databricks

The dataset was uploaded into Databricks volume:

kaggle_file/
   taxi_2018.csv
2️⃣ Read CSV with Explicit Schema

We defined a structured schema to avoid schema inference issues and improve performance:

df = spark.read.csv(
    "/Volumes/workspace/default/kaggle_file/taxi_2018.csv",
    header=True,
    schema=taxi_dataset_schema
)
3️⃣ Save as Parquet (Bronze Layer)
df.write.format("parquet") \
    .mode("overwrite") \
    .save("/Volumes/workspace/default/day_20_project/bronze/taxi_raw_data/")

This converts raw CSV into columnar Parquet format for efficient analytics.

🏗 Project Architecture
day_20_project/

bronze/
   taxi_raw_data/

silver/
   clean_valid_trips/
   anomalies/

gold/
   daily_revenue/
   hourly_demand/
🥉 Bronze Layer — Raw Data
Purpose:

Store original structured dataset

No business logic changes

Convert CSV → Parquet

Validation Performed:

Row count verification (112M+ rows)

Null checks

Negative fare detection

Distance validation

Timestamp format consistency

Bronze layer keeps data exactly as received.

🥈 Silver Layer — Clean & Validated Data
Purpose:

Apply business rules

Parse timestamps

Engineer trip duration

Identify anomalies

Separate clean vs invalid trips

Transformations:

Convert string → timestamp

Calculate trip_duration_minutes

Validate business logic:

Duration > 0

Fare > 0

Passenger count > 0

Pickup ≤ Dropoff

Outputs:

clean_valid_trips/

anomalies/

This layer simulates real-world data quality enforcement.

🥇 Gold Layer — Business KPIs

Gold layer contains analytics-ready tables for reporting and dashboards.

📊 1️⃣ Daily Revenue KPI

Business Questions:

How much revenue per day?

Total trips per day?

Average trip value?

Aggregations:

Sum of total_amount

Count of trips

Average trip value

Stored at:

gold/daily_revenue/
⏰ 2️⃣ Hourly Demand Intelligence

Business Questions:

Peak travel hours?

Revenue by hour?

Average fare per hour?

Trip distance patterns?

Aggregations:

Trip count

Total revenue

Average fare

Average trip distance

Stored at:

gold/hourly_demand/
🚀 Performance Optimizations Applied

Explicit schema definition

Parquet conversion

Column pruning

Repartition before groupBy

Shuffle partition tuning

Explain plan analysis

Adaptive execution awareness

📈 What This Project Demonstrates

Handling large datasets (100M+ rows)

Layered data architecture

Data quality engineering

Business KPI design

Spark performance tuning

Partition strategy thinking

Real-world ETL mindset

🛠 Technologies Used

Apache Spark (PySpark)

Databricks

Parquet

Distributed Data Processing

Data Engineering Best Practices

🎯 Key Learnings

Shuffle is expensive — must be controlled.

Repartition strategy affects performance.

Always measure anomalies before cleaning.

Separate raw, clean, and business layers.

Build analytics tables, not just transformations.

📌 Future Improvements

Incremental processing instead of overwrite

Partitioned writes for large Gold tables

Job orchestration (Airflow / Workflows)

Data quality framework integration

Small file compaction

Monitoring & alerting

👨‍💻 Author

Spark Data Engineering Practice Project
Built for learning advanced Spark pipeline design and optimization.
