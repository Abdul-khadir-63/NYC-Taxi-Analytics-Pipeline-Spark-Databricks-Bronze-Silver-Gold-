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
<h2 align="center">📥 Dataset & Volume Setup</h2>

<p align="center">
  <em>The dataset is not included in this repository because it is ~10GB. Follow the steps below to configure Databricks correctly.</em>
</p>

<div style="margin-bottom: 25px;">
  <h3>1️⃣ Download Dataset</h3>
  <p>Download the <strong>NYC Yellow Taxi 2018</strong> dataset from Kaggle:</p>
  <ul>
    <li><strong>Search:</strong> NYC Yellow Taxi Trip Records 2018</li>
    <li><strong>File Name:</strong> <code>taxi_2018.csv</code></li>
  </ul>
</div>

<div style="margin-bottom: 25px;">
  <h3>2️⃣ Create Project Folder Structure</h3>
  <p>In Databricks, navigate to <code>Data > Volumes > workspace/default/</code> and create the following directory hierarchy:</p>
  <pre style="background-color: #f6f8fa; padding: 15px; border-radius: 8px; border: 1px dotted #0366d6; color: #24292e;">
NYC_Yellow_Taxi_2018_Project/
├── bronze/
│   └── taxi_raw_data/
├── silver/
│   ├── clean_valid_trips/
│   └── anomalies/
└── gold/
    ├── daily_revenue/
    └── hourly_demand/</pre>
</div>

<div style="margin-bottom: 25px;">
  <h3>3️⃣ Upload Dataset</h3>
  <p>Create a dedicated ingestion folder and upload your raw file:</p>
  <ul>
    <li><strong>Folder:</strong> <code>workspace/default/kaggle_files/</code></li>
    <li><strong>File:</strong> <code>taxi_2018.csv</code></li>
    <li><strong>Final Path:</strong> <code>/Volumes/workspace/default/kaggle_files/taxi_2018.csv</code></li>
  </ul>
</div>

<div style="margin-bottom: 25px;">
  <h3>4️⃣ Update Paths in Code</h3>
  <p>Ensure the following paths are configured in your Python scripts:</p>
  <div style="background-color: #fdf6e3; padding: 10px; border-radius: 5px; border-left: 5px solid #b58900;">
    <code style="color: #d33682;">INPUT_PATH</code> = "/Volumes/workspace/default/kaggle_files/taxi_2018.csv"<br>
    <code style="color: #d33682;">BRONZE_OUTPUT_PATH</code> = "/Volumes/workspace/default/NYC_Yellow_Taxi_2018_Project/bronze/taxi_raw_data/"
  </div>
</div>

<div style="margin-bottom: 25px;">
  <h3>5️⃣ Run the Pipeline</h3>
  <p>Run the scripts in the following sequential order:</p>
  <ol>
    <li><code>bronze.py</code></li>
    <li><code>silver.py</code></li>
    <li><code>gold.py</code></li>
  </ol>
</div>

<hr />

<div style="background-color: #fffbdd; border: 1px solid #d2991d; padding: 15px; border-radius: 8px;">
  <strong>⚠️ Important Notes:</strong>
  <ul>
    <li>Dataset contains <strong>112M+ rows</strong>.</li>
    <li>First execution may take time; ensure Spark cluster is active.</li>
    <li>Adjust volume paths if your workspace naming differs.</li>
  </ul>
</div>

## ⚙️ How Dataset Was Loaded in Databricks

### Step 1 — Upload dataset to volume


kaggle_file/
taxi_2018.csv


### Step 2 — Read CSV with explicit schema

<b> python </b><br> 
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
NYC_Project/

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

<h2 align="center">👨‍💻 Author</h2> <p align="center"> Spark Data Engineering practice project focused on large-scale processing, pipeline architecture, and Spark optimization. </p> 
