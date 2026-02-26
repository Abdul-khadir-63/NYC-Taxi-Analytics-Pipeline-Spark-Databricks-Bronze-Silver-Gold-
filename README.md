<h1 align="center">🚕 NYC Taxi Analytics Pipeline</h1>

<p align="center">
End-to-End Spark Data Engineering Project on 112M+ Records
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Apache%20Spark-PySpark-orange">
  <img src="https://img.shields.io/badge/Platform-Databricks-red">
  <img src="https://img.shields.io/badge/Data-10GB-blue">
  <img src="https://img.shields.io/badge/Architecture-Bronze%20Silver%20Gold-green">
</p>
📌 Project Overview

This project builds a complete production-style data engineering pipeline using Apache Spark on Databricks.

A 10GB NYC Yellow Taxi dataset (112M+ rows) is processed through a structured:

Bronze → Silver → Gold architecture

The pipeline simulates real-world ingestion, cleaning, validation, aggregation, and performance optimization.

🗂 Dataset Information

Dataset Name: NYC Yellow Taxi Trip Records (2018)
Source: Kaggle (Original data from NYC Taxi & Limousine Commission)
File Used: taxi_2018.csv
Size: ~10GB
Total Rows: ~112,234,626
Format: CSV

Dataset Includes

Pickup & dropoff timestamps

Passenger count

Trip distance

Fare breakdown (fare, tax, tip, tolls)

Payment type

⚙️ How Dataset Was Loaded in Databricks
1️⃣ Upload dataset to Databricks Volume
kaggle_file/
   taxi_2018.csv
2️⃣ Read CSV with Explicit Schema
df = spark.read.csv(
    "/Volumes/workspace/default/kaggle_file/taxi_2018.csv",
    header=True,
    schema=taxi_dataset_schema
)
3️⃣ Save as Parquet (Bronze Layer)
df.write.format("parquet") \
    .mode("overwrite") \
    .save("/Volumes/workspace/default/day_20_project/bronze/taxi_raw_data/")

CSV is converted into columnar Parquet format for better performance.

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
Purpose

Store original structured dataset

No business logic modifications

Convert CSV → Parquet

Validation Performed

Row count verification (112M+ rows)

Null checks

Negative fare detection

Distance validation

Timestamp consistency check

Bronze keeps data exactly as received.

🥈 Silver Layer — Clean & Validated Data
Purpose

Apply business rules

Parse timestamps

Engineer trip duration

Identify anomalies

Separate clean vs invalid trips

Transformations

Convert string → timestamp

Calculate trip_duration_minutes

Apply business validation rules:

Duration > 0

Fare > 0

Passenger count > 0

Pickup ≤ Dropoff

Outputs
clean_valid_trips/
anomalies/

This layer simulates real-world data quality enforcement.

🥇 Gold Layer — Business KPIs

Gold contains analytics-ready tables for reporting and dashboards.

📊 Daily Revenue KPI
Business Questions

How much revenue per day?

Total trips per day?

Average trip value per day?

Aggregations

SUM(total_amount)

COUNT(*)

AVG(total_amount)

Stored at:

gold/daily_revenue/
⏰ Hourly Demand Intelligence
Business Questions

Peak travel hours?

Revenue by hour?

Average fare per hour?

Trip distance trends?

Aggregations

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

Business KPI modeling

Spark performance tuning

Partition strategy design

Production-style ETL mindset

🛠 Technologies Used

Apache Spark (PySpark)

Databricks

Parquet

Distributed data processing

Data engineering best practices

🎯 Key Learnings

Shuffle operations are expensive and must be controlled

Repartition strategy directly impacts performance

Always measure anomalies before cleaning

Separate raw, clean, and business layers

Build analytics-ready tables, not just transformations

📌 Future Improvements

Incremental processing instead of overwrite

Partitioned writes for large Gold tables

Workflow orchestration (Airflow / Databricks Jobs)

Data quality framework integration

Small file compaction

Monitoring and alerting

👨‍💻 Author

Spark Data Engineering practice project focused on large-scale processing, pipeline architecture, and Spark optimization.
