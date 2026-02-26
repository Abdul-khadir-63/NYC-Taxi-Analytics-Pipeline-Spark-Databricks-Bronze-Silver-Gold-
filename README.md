<div align="center">
  <h1>🚕 NYC Taxi Analytics Pipeline</h1>
  <p><b>End-to-End Spark Data Engineering Project on 112M+ Records</b></p>
  <p>
    <img src="https://img.shields.io/badge/Apache%20Spark-PySpark-orange?style=for-the-badge&logo=apachespark">
    <img src="https://img.shields.io/badge/Platform-Databricks-red?style=for-the-badge&logo=databricks">
    <img src="https://img.shields.io/badge/Data-10GB-blue?style=for-the-badge">
    <img src="https://img.shields.io/badge/Architecture-Bronze%20Silver%20Gold-green?style=for-the-badge">
  </p>
</div>

<hr />

<h2>📌 Project Overview</h2>
<p>This project builds a production-style data engineering pipeline using <b>Apache Spark on Databricks</b>. A 10GB NYC Yellow Taxi dataset (112M+ rows) is processed through a structured architecture: <b>Bronze → Silver → Gold</b>. The pipeline simulates real-world ingestion, cleaning, validation, aggregation, and performance optimization.</p>

<hr />

<h2>🗂️ Dataset Information</h2>
<table width="100%">
  <tr><td><b>Attribute</b></td><td><b>Details</b></td></tr>
  <tr><td>Dataset</td><td>NYC Yellow Taxi Trip Records (2018)</td></tr>
  <tr><td>Source</td><td>Kaggle (NYC Taxi & Limousine Commission)</td></tr>
  <tr><td>Rows / Size</td><td>~112,234,626 Rows / ~10GB</td></tr>
  <tr><td>Includes</td><td>Timestamps, Passenger count, Trip distance, Fare breakdown, Payment type</td></tr>
</table>

<hr />

<h2>📥 Dataset & Volume Setup</h2>
<p>Follow these steps to configure Databricks correctly before running the pipeline:</p>

<div style="background-color: #f6f8fa; padding: 15px; border-radius: 8px; border: 1px solid #ddd;">
  <b>1️⃣ Download:</b> Search Kaggle for <code>NYC Yellow Taxi Trip Records 2018</code> and download <code>taxi_2018.csv</code>.<br><br>
  <b>2️⃣ Folder Structure:</b> Navigate to <code>workspace/default/</code> and create <code>NYC_Yellow_Taxi_2018_Project/</code> with subfolders: 
  <code>bronze/taxi_raw_data/</code>, <code>silver/clean_valid_trips/</code>, <code>silver/anomalies/</code>, <code>gold/daily_revenue/</code>, and <code>gold/hourly_demand/</code>.<br><br>
  <b>3️⃣ Upload:</b> Place the CSV at <code>/Volumes/workspace/default/kaggle_files/taxi_2018.csv</code>.
</div>

<hr />

<h2 align="center">🏗️ Project Architecture & Logic</h2>



<h3>🥉 Bronze Layer — Raw Data</h3>
<p><b>Purpose:</b> Store original structured dataset exactly as received in Parquet format.</p>
<ul>
  <li><b>Validation:</b> Row count verification (112M+ rows), Null checks, Negative fare detection.</li>
</ul>
<pre><code>df.write.format("parquet").mode("overwrite").save(BRONZE_OUTPUT_PATH)</code></pre>

<h3>🥈 Silver Layer — Clean & Validated Data</h3>
<p><b>Purpose:</b> Apply business rules and feature engineering. Separates clean data from anomalies.</p>
<ul>
  <li><b>Transformations:</b> Convert string to timestamp, calculate <code>trip_duration_minutes</code>.</li>
  <li><b>Rules:</b> Duration > 0, Fare > 0, Passenger count > 0, Pickup ≤ Dropoff.</li>
</ul>

<h3>🥇 Gold Layer — Business KPIs</h3>
<p><b>Analytics-ready datasets for reporting:</b></p>
<ul>
  <li><b>Daily Revenue:</b> Revenue per day, total trips, and average trip value.</li>
  <li><b>Hourly Demand:</b> Peak travel hours, revenue by hour, and trip distance patterns.</li>
</ul>
<pre><code>df.write.mode("overwrite").partitionBy("pickup_date").parquet(GOLD_PATH)</code></pre>

<hr />

<h2 align="center">🚀 Performance Optimizations Applied</h2>
<div align="center">
  <code>Explicit Schema Definition</code> • <code>Parquet Conversion</code> • <code>Column Pruning</code> • 
  <code>Repartitioning</code> • <code>Shuffle Partition Tuning</code> • <code>Adaptive Execution</code>
</div>

<hr />

<h2>📈 What This Project Demonstrates</h2>
<ul>
  <li>Handling large datasets (100M+ rows).</li>
  <li>Layered data architecture (Medallion).</li>
  <li>Data quality engineering (Anomaly separation).</li>
  <li>Spark performance tuning & Partition strategy design.</li>
</ul>

<hr />

<h2 align="center">🌟 About Me</h2>
<p align="center">
  Hi there! I'm <b>Abdul Khadir</b>. I'm a Diploma Computer Science graduate on a mission to become a <b>Data Engineer</b>!
</p>

<p align="center">
  <a href="#"><img src="https://img.shields.io/badge/GitHub-Profile-black?style=flat&logo=github"></a>
</p>
