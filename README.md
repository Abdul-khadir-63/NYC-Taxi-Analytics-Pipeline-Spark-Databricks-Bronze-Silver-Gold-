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

<hr>

<h2 align="center">📌 Project Overview</h2>

<p>
This project demonstrates how to build a real-world data engineering pipeline using <strong>Apache Spark (PySpark)</strong> on <strong>Databricks</strong>.
</p>

<p>
The dataset contains over <strong>112 million taxi trip records</strong> (~10GB). The goal is to simulate how production data teams ingest raw data, validate it, clean it, transform it, and deliver analytics-ready datasets for business reporting.
</p>

<p align="center"><strong>Bronze → Silver → Gold Architecture</strong></p>

<p>
This layered approach improves data reliability, performance, traceability, and business usability.
</p>

<hr>

<h2 align="center">🗂 Dataset Information</h2>

<table width="100%" style="border-collapse: collapse;">
<tr style="background-color:#f2f2f2;">
<th style="padding:10px; border:1px solid #ddd;">Attribute</th>
<th style="padding:10px; border:1px solid #ddd;">Details</th>
</tr>
<tr>
<td style="padding:10px; border:1px solid #ddd;">Dataset</td>
<td style="padding:10px; border:1px solid #ddd;">NYC Yellow Taxi Trip Records (2018)</td>
</tr>
<tr>
<td style="padding:10px; border:1px solid #ddd;">Source</td>
<td style="padding:10px; border:1px solid #ddd;">Kaggle (NYC Taxi & Limousine Commission)</td>
</tr>
<tr>
<td style="padding:10px; border:1px solid #ddd;">File</td>
<td style="padding:10px; border:1px solid #ddd;">taxi_2018.csv</td>
</tr>
<tr>
<td style="padding:10px; border:1px solid #ddd;">Size</td>
<td style="padding:10px; border:1px solid #ddd;">~10GB</td>
</tr>
<tr>
<td style="padding:10px; border:1px solid #ddd;">Rows</td>
<td style="padding:10px; border:1px solid #ddd;">~112,234,626</td>
</tr>
</table>

<p><strong>The dataset includes:</strong></p>
<ul>
<li>Pickup and dropoff timestamps</li>
<li>Passenger count</li>
<li>Trip distance</li>
<li>Fare breakdown (fare, tax, tip, tolls, surcharge)</li>
<li>Payment type</li>
</ul>

<hr>

<h2 align="center">📊 Data Scale</h2>

<ul>
<li>Input dataset: ~10GB CSV</li>
<li>Total records processed: 112M+</li>
<li>Execution engine: Databricks Photon</li>
<li>Processing model: Distributed Spark execution</li>
</ul>

<hr>

<h2 align="center">📥 Dataset & Volume Setup</h2>

<p align="center">
<em>The dataset is not included in this repository due to its size. Follow these steps to configure Databricks.</em>
</p>

<h3>1️⃣ Download Dataset</h3>
<p>Search and download from Kaggle: <strong>NYC Yellow Taxi Trip Records 2018</strong></p>
<p>File: <code>taxi_2018.csv</code></p>

<h3>2️⃣ Create Volume Folder Structure</h3>

<pre>
NYC_Yellow_Taxi_2018_Project/
├── bronze/
│   └── taxi_raw_data/
├── silver/
│   ├── clean_valid_trips/
│   └── anomalies/
└── gold/
    ├── daily_revenue/
    └── hourly_demand/
</pre>

<h3>3️⃣ Upload Dataset</h3>

<pre>
/Volumes/workspace/default/kaggle_files/taxi_2018.csv
</pre>

<h3>4️⃣ Update Paths in Scripts</h3>

<pre>
INPUT_PATH = "/Volumes/workspace/default/kaggle_files/taxi_2018.csv"
BRONZE_OUTPUT_PATH = "/Volumes/workspace/default/NYC_Yellow_Taxi_2018_Project/bronze/taxi_raw_data/"
</pre>

<hr>

<h3 align="center">🧪 How to Run This Project</h3>

<ol>
<li>Clone this repository</li>
<li>Download dataset from Kaggle</li>
<li>Upload CSV to Databricks volume</li>
<li>Create Bronze, Silver, Gold folders</li>
<li>Update paths in scripts</li>
<li>Run scripts in order:</li>
</ol>

<pre>
1. bronze.py
2. silver.py
3. gold.py
</pre>

<p align="center">
  <img src="docs/Data%20flow%20Diagram.png" alt="NYC Taxi Data Flow Diagram" width="850">
</p>

<hr>

<h1 align="center">🏗️ Project Architecture & Pipeline Design</h1>

<h3>🥉 Bronze Layer — Raw Data</h3>

<ul>
<li>Stores raw ingested dataset</li>
<li>CSV converted into Parquet</li>
<li>No business transformation applied</li>
<li>Row count, null checks, data validation performed</li>
</ul>

<hr>

<h3>🥈 Silver Layer — Clean & Validated Data</h3>

<ul>
<li>Timestamp conversion</li>
<li>Trip duration calculation</li>
<li>Business rule validation</li>
<li>Valid and anomaly datasets separated</li>
</ul>

<hr>

<h3>🥇 Gold Layer — Business KPIs</h3>

<ul>
<li>Daily revenue metrics</li>
<li>Total trips per day</li>
<li>Average trip value</li>
<li>Hourly demand analysis</li>
<li>Revenue trends and trip patterns</li>
</ul>

<hr>

<h3 align="center">🚀 Performance Optimizations</h3>

<ul>
<li>Explicit schema definition</li>
<li>Parquet columnar storage</li>
<li>Column pruning</li>
<li>Repartition before aggregation</li>
<li>Shuffle partition tuning</li>
<li>Query plan analysis using explain()</li>
<li>Adaptive execution awareness</li>
</ul>

<hr>

<h3 align="center">📈 What This Project Demonstrates</h3>

<ul>
<li>Handling large-scale datasets (100M+ rows)</li>
<li>Production-style medallion architecture</li>
<li>Data quality engineering</li>
<li>Business KPI modeling</li>
<li>Spark optimization strategies</li>
</ul>

<hr>

<h3 align="center">🎯 Key Learnings</h3>

<ul>
<li>Shuffle operations are expensive</li>
<li>Partition strategy impacts performance</li>
<li>Always analyze anomalies before cleaning</li>
<li>Separate raw, clean, and business data layers</li>
<li>Design analytics-ready datasets</li>
</ul>

<hr>

<h3 align="center">📌 Future Improvements</h3>

<ul>
<li>Incremental pipeline processing</li>
<li>Delta Lake integration</li>
<li>Workflow orchestration</li>
<li>Automated data quality checks</li>
<li>Small file compaction</li>
<li>Monitoring and alerting</li>
</ul>

<hr>

<h1 align="center">👨‍💻 About Me</h1>

<p align="center">
<strong>Abdul Khadir</strong><br>
Diploma in Computer Science graduate<br>
Currently focused on becoming a Data Engineer and building large-scale Spark projects.
</p>
