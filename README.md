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

---

## 📌 Project Overview

This project builds a production-style data engineering pipeline using **Apache Spark on Databricks**.

A **10GB NYC Yellow Taxi dataset (112M+ rows)** is processed through a structured architecture:

<p align="center"><b>Bronze → Silver → Gold</b></p>

The pipeline simulates real-world ingestion, cleaning, validation, aggregation, and performance optimization.

---

## 🗂 Dataset Information

| Attribute | Details |
|---|---|
| Dataset | NYC Yellow Taxi Trip Records (2018) |
| Source | Kaggle (NYC Taxi & Limousine Commission) |
| File | taxi_2018.csv |
| Size | ~10GB |
| Rows | ~112,234,626 |
| Format | CSV |

### Dataset Includes

- Pickup & dropoff timestamps  
- Passenger count  
- Trip distance  
- Fare breakdown (fare, tax, tip, tolls)  
- Payment type  

---

## ⚙️ How Dataset Was Loaded in Databricks

### Step 1 — Upload dataset to volume


kaggle_file/
taxi_2018.csv


### Step 2 — Read CSV with explicit schema

--python
df = spark.read.csv(
    "/Volumes/workspace/default/kaggle_file/taxi_2018.csv",
    header=True,
    schema=taxi_dataset_schema
)
Step 3 — Save as Parquet (Bronze layer)
df.write.format("parquet") \
    .mode("overwrite") \
    .save("/Volumes/workspace/default/day_20_project/bronze/taxi_raw_data/")

CSV → converted to Parquet for fast analytics.

<h2 align="center">🏗 Project Architecture</h2>
day_20_project/

bronze/
   taxi_raw_data/

silver/
   clean_valid_trips/
   anomalies/

gold/
   daily_revenue/
   hourly_demand/
<h2 align="center">🥉 Bronze Layer — Raw Data</h2>
Purpose

Store original structured dataset

No business logic applied

Convert CSV → Parquet

Validation Performed

Row count verification (112M+ rows)

Null checks

Negative fare detection

Distance validation

Timestamp consistency check

Bronze keeps data exactly as received.

<h2 align="center">🥈 Silver Layer — Clean & Validated Data</h2>
Purpose

Apply business rules

Parse timestamps

Engineer trip duration

Identify anomalies

Separate clean vs invalid trips

Transformations

Convert string → timestamp

Calculate trip_duration_minutes

Validation Rules

Duration > 0

Fare > 0

Passenger count > 0

Pickup ≤ Dropoff

Outputs
clean_valid_trips/
anomalies/

Simulates real-world data quality enforcement.

<h2 align="center">🥇 Gold Layer — Business KPIs</h2>

Analytics-ready datasets for dashboards and reporting.

📊 Daily Revenue KPI

Business Questions

Revenue per day

Total trips per day

Average trip value

Aggregations

SUM(total_amount)

COUNT(*)

AVG(total_amount)

Stored at:

gold/daily_revenue/
⏰ Hourly Demand Intelligence

Business Questions

Peak travel hours

Revenue by hour

Average fare trends

Trip distance patterns

Aggregations

Trip count

Total revenue

Average fare

Average trip distance

Stored at:

gold/hourly_demand/
<h2 align="center">🚀 Performance Optimizations Applied</h2>

Explicit schema definition

Parquet conversion

Column pruning

Repartition before groupBy

Shuffle partition tuning

Explain plan analysis

Adaptive execution awareness

<h2 align="center">📈 What This Project Demonstrates</h2>

Handling large datasets (100M+ rows)

Layered data architecture

Data quality engineering

Business KPI modeling

Spark performance tuning

Partition strategy design

Production ETL mindset

<h2 align="center">🛠 Technologies Used</h2>

Apache Spark (PySpark)

Databricks

Parquet

Distributed processing

Data engineering best practices

<h2 align="center">🎯 Key Learnings</h2>

Shuffle operations must be controlled

Repartition strategy impacts performance

Always measure anomalies before cleaning

Separate raw, clean, and business layers

Build analytics tables, not just transformations

<h2 align="center">📌 Future Improvements</h2>

Incremental processing

Partitioned writes for Gold tables

Workflow orchestration (Airflow / Databricks Jobs)

Data quality framework integration

Small file compaction

Monitoring & alerting

<h1 align="center">🌟 About Me </h1>
Hi there! I'm **Abdul Khadir**, I'm an Deploma computer Science Pass out Student on a mission to Became a Data Engineer!
