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

<h1 align="center">🏗️ Project Architecture & Pipeline Design</h1>



<div style="background-color: #f6f8fa; padding: 20px; border-radius: 10px; border: 1px solid #ddd; margin-bottom: 30px;">
  <h3 style="margin-top: 0;">📁 Directory Structure</h3>
  <pre style="font-family: 'Courier New', monospace; color: #24292e;">
NYC_Project/
├── bronze/
│   └── taxi_raw_data/
├── silver/
│   ├── clean_valid_trips/
│   └── anomalies/
└── gold/
    ├── daily_revenue/
    └── hourly_demand/</pre>
</div>

<div style="display: flex; flex-direction: column; gap: 20px;">

  <div style="border: 1px solid #cd7f32; border-left: 10px solid #cd7f32; padding: 20px; border-radius: 8px; background-color: #fffaf5;">
    <h3 style="color: #cd7f32; margin-top: 0;">🥉 Bronze Layer — Raw Data</h3>
    <p><strong>Purpose:</strong> Store original structured dataset with no business logic applied. Convert CSV → Parquet.</p>
    <strong>Validation Performed:</strong>
    <ul>
      <li>Row count verification (112M+ rows)</li>
      <li>Null checks & Negative fare detection</li>
      <li>Distance validation & Timestamp consistency check</li>
    </ul>
    <em>Result: Bronze keeps data exactly as received.</em>
  </div>

  <div style="border: 1px solid #c0c0c0; border-left: 10px solid #c0c0c0; padding: 20px; border-radius: 8px; background-color: #fcfcfc;">
    <h3 style="color: #7d7d7d; margin-top: 0;">🥈 Silver Layer — Clean & Validated Data</h3>
    <p><strong>Purpose:</strong> Apply business rules, engineer duration, and separate clean vs. invalid trips.</p>
    <strong>Transformations & Rules:</strong>
    <ul>
      <li>Convert string ➔ timestamp | Calculate <code>trip_duration_minutes</code></li>
      <li>Validation: Duration > 0, Fare > 0, Passenger count > 0, Pickup ≤ Dropoff</li>
    </ul>
    <strong>Outputs:</strong> <code>clean_valid_trips/</code>, <code>anomalies/</code>
  </div>

  <div style="border: 1px solid #ffd700; border-left: 10px solid #ffd700; padding: 20px; border-radius: 8px; background-color: #fffef0;">
    <h3 style="color: #b8860b; margin-top: 0;">🥇 Gold Layer — Business KPIs</h3>
    <p>Analytics-ready datasets for dashboards and reporting.</p>
    
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px;">
      <div>
        <strong>📊 Daily Revenue KPI</strong>
        <ul>
          <li>Revenue/Trips per day</li>
          <li>Aggs: SUM, COUNT, AVG</li>
        </ul>
      </div>
      <div>
        <strong>⏰ Hourly Demand Intelligence</strong>
        <ul>
          <li>Peak hours & revenue trends</li>
          <li>Avg fare & distance patterns</li>
        </ul>
      </div>
    </div>
  </div>

</div>

<hr />

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-top: 20px;">
  <div style="padding: 15px; border: 1px solid #ddd; border-radius: 8px;">
    <h4>🚀 Performance Optimizations</h4>
    <small>Explicit schema, Parquet conversion, Column pruning, Repartition before groupBy, Shuffle partition tuning, Explain plan analysis, Adaptive execution.</small>
  </div>
  <div style="padding: 15px; border: 1px solid #ddd; border-radius: 8px;">
    <h4>🛠️ Technologies Used</h4>
    <small>Apache Spark (PySpark), Databricks, Parquet, Distributed Processing, Data Engineering Best Practices.</small>
  </div>
</div>

<hr />

<h3 align="center">📈 Project Impact & Insights</h3>
<table width="100%" style="border-collapse: collapse;">
  <tr style="background-color: #f2f2f2;">
    <th style="padding: 10px; border: 1px solid #ddd;">What This Project Demonstrates</th>
    <th style="padding: 10px; border: 1px solid #ddd;">🎯 Key Learnings</th>
  </tr>
  <tr>
    <td style="padding: 10px; border: 1px solid #ddd; vertical-align: top;">
      • Handling 100M+ rows<br>• Layered Medallion architecture<br>• Data quality engineering<br>• Partition strategy design
    </td>
    <td style="padding: 10px; border: 1px solid #ddd; vertical-align: top;">
      • Control shuffle operations<br>• Measure anomalies before cleaning<br>• Separate raw, clean, and business layers
    </td>
  </tr>
</table>

<hr />

<div style="padding: 15px; background-color: #eefbff; border-radius: 8px; border: 1px dashed #0077b6;">
  <h4>📌 Future Improvements</h4>
  <p style="font-size: 0.9em;">
    Incremental processing • Partitioned writes for Gold • Workflow orchestration (Airflow/Jobs) • Data quality framework • Small file compaction • Monitoring & alerting.
  </p>
</div>

<p align="center" style="margin-top: 20px;">
  <strong>👨‍💻 Author:</strong> Spark Data Engineering practice project focused on large-scale processing and Spark optimization.
</p>
