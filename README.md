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
The dataset contains over <strong>112 million taxi trip records</strong> (approximately 10GB). The objective of this project is to simulate how a production data team would ingest raw data, clean it, validate it, transform it, and prepare business-ready datasets for reporting and analytics.
</p>

<p align="center"><strong>Bronze → Silver → Gold Architecture</strong></p>

<p>
This layered approach ensures data reliability, traceability, performance optimization, and business usability.
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
<li>Detailed fare breakdown (fare, tax, tip, tolls, surcharge)</li>
<li>Payment type information</li>
</ul>

<hr>

<h2 align="center">📥 Dataset & Volume Setup</h2>

<p align="center">
<em>The dataset is not included in this repository due to its size. Follow these steps to configure Databricks correctly.</em>
</p>

<h3>1️⃣ Download Dataset</h3>
<p>
Download the dataset from Kaggle by searching:
<strong>NYC Yellow Taxi Trip Records 2018</strong>
</p>
<p>Download the file: <code>taxi_2018.csv</code></p>

<h3>2️⃣ Create Volume Folder Structure</h3>
<p>In Databricks go to: <strong>Data → Volumes → workspace/default/</strong></p>

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

<p>This structure ensures clean separation between raw, validated, and business-ready data.</p>

<h3>3️⃣ Upload Dataset</h3>
<p>Upload <code>taxi_2018.csv</code> into:</p>

<pre>
/Volumes/workspace/default/kaggle_files/taxi_2018.csv
</pre>

<h3>4️⃣ Update Paths in Code</h3>

<pre>
INPUT_PATH = "/Volumes/workspace/default/kaggle_files/taxi_2018.csv"
BRONZE_OUTPUT_PATH = "/Volumes/workspace/default/NYC_Yellow_Taxi_2018_Project/bronze/taxi_raw_data/"
</pre>

<h3>5️⃣ Run Pipeline in Order</h3>

<ol>
<li>bronze.py</li>
<li>silver.py</li>
<li>gold.py</li>
</ol>

<hr>

<h1 align="center">🏗️ Project Architecture & Pipeline Design</h1>

<h3>🥉 Bronze Layer — Raw Data</h3>

<p><strong>Purpose:</strong></p>
<ul>
<li>Store raw ingested data</li>
<li>Convert CSV to optimized Parquet format</li>
<li>No business logic modifications</li>
</ul>

<p><strong>Validation Checks Performed:</strong></p>
<ul>
<li>Row count verification</li>
<li>Null value analysis</li>
<li>Negative fare detection</li>
<li>Trip distance validation</li>
<li>Timestamp consistency checks</li>
</ul>

<p>Bronze acts as a reliable raw data backup layer.</p>

<hr>

<h3>🥈 Silver Layer — Clean & Validated Data</h3>

<p><strong>Purpose:</strong></p>
<ul>
<li>Clean the data</li>
<li>Apply business rules</li>
<li>Generate derived columns</li>
<li>Separate valid and invalid trips</li>
</ul>

<p><strong>Key Transformations:</strong></p>
<ul>
<li>Convert string timestamps to proper timestamp format</li>
<li>Calculate <code>trip_duration_minutes</code></li>
<li>Apply validation rules:
    <ul>
        <li>Duration must be greater than 0</li>
        <li>Fare must be positive</li>
        <li>Passenger count must be positive</li>
        <li>Pickup time must be before dropoff time</li>
    </ul>
</li>
</ul>

<p>Output is divided into:</p>
<ul>
<li><code>clean_valid_trips</code></li>
<li><code>anomalies</code></li>
</ul>

<hr>

<h3>🥇 Gold Layer — Business KPIs</h3>

<p>This layer creates analytics-ready datasets used for dashboards and reporting.</p>

<h4>📊 Daily Revenue KPI</h4>
<ul>
<li>Total revenue per day</li>
<li>Total trips per day</li>
<li>Average trip value per day</li>
</ul>

<h4>⏰ Hourly Demand Intelligence</h4>
<ul>
<li>Peak travel hours</li>
<li>Revenue trends by hour</li>
<li>Average fare patterns</li>
<li>Trip distance trends</li>
</ul>

<hr>

<h3 align="center">🚀 Performance Optimizations</h3>

<ul>
<li>Explicit schema definition to avoid inference overhead</li>
<li>Parquet columnar storage format</li>
<li>Column pruning</li>
<li>Repartitioning before aggregation</li>
<li>Shuffle partition tuning</li>
<li>Query plan analysis using explain()</li>
<li>Adaptive execution awareness</li>
</ul>

<hr>

<h3 align="center">📈 What This Project Demonstrates</h3>

<ul>
<li>Handling 100M+ rows efficiently</li>
<li>Production-style medallion architecture</li>
<li>Data validation and anomaly detection</li>
<li>Business KPI design</li>
<li>Spark optimization strategies</li>
<li>Partition strategy thinking</li>
</ul>

<hr>

<h3 align="center">🎯 Key Learnings</h3>

<ul>
<li>Shuffle operations are expensive and must be controlled</li>
<li>Partition strategy impacts performance significantly</li>
<li>Always measure anomalies before removing data</li>
<li>Separate raw, clean, and business layers properly</li>
<li>Build analytics-ready datasets, not just transformations</li>
</ul>

<hr>

<h3 align="center">📌 Future Improvements</h3>

<ul>
<li>Incremental processing instead of overwrite mode</li>
<li>Delta Lake integration</li>
<li>Workflow orchestration</li>
<li>Automated data quality monitoring</li>
<li>Small file optimization</li>
<li>Performance benchmarking reports</li>
</ul>

<hr>

<p align="center">
<strong>👨‍💻 Author:</strong> Spark Data Engineering practice project focused on large-scale processing, pipeline design, and Spark optimization.
</p>
