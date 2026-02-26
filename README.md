<div align="center">
  <h1>🚕 NYC Taxi Analytics Pipeline</h1>
  <p><strong>End-to-End Spark Data Engineering on 112M+ Records</strong></p>
  
  <p>
    <img src="https://img.shields.io/badge/Apache%20Spark-PySpark-orange?style=for-the-badge&logo=apachespark">
    <img src="https://img.shields.io/badge/Platform-Databricks-red?style=for-the-badge&logo=databricks">
    <img src="https://img.shields.io/badge/Data_Size-10GB-blue?style=for-the-badge">
    <img src="https://img.shields.io/badge/Architecture-Bronze%20Silver%20Gold-green?style=for-the-badge">
  </p>
</div>

<hr />

<h2 align="center">📥 Dataset & Volume Setup</h2>
<p align="center">The dataset is not included in this repository because it is ~10GB. Follow these steps to configure Databricks.</p>

<div style="margin: 20px; padding: 20px; border: 1px solid #ddd; border-radius: 10px; background-color: #f9f9f9;">
  <strong>1️⃣ Download Dataset:</strong> NYC Yellow Taxi 2018 from Kaggle (<code>taxi_2018.csv</code>).<br><br>
  <strong>2️⃣ Create Folder Structure:</strong> Navigate to <code>workspace/default/</code> and create:
  <pre style="background-color: #f0f0f0; padding: 10px; margin: 10px 0; border-radius: 5px;">
NYC_Yellow_Taxi_2018_Project/
├── bronze/         # taxi_raw_data/
├── silver/         # clean_valid_trips/ | anomalies/
└── gold/           # daily_revenue/ | hourly_demand/</pre>
  <strong>3️⃣ Upload Data:</strong> Store at <code>/Volumes/workspace/default/kaggle_files/taxi_2018.csv</code>
</div>

<hr />

<h2 align="center">🏗️ Medallion Architecture</h2>



<div style="display: flex; flex-direction: column; gap: 10px; margin: 20px;">
  <div style="border-left: 8px solid #cd7f32; padding: 15px; background: #fffaf5;">
    <strong style="color: #cd7f32;">🥉 BRONZE: Raw Data</strong><br>
    Convert CSV to Parquet. Row count verification (112M+ rows). Null and negative fare detection.
  </div>
  <div style="border-left: 8px solid #c0c0c0; padding: 15px; background: #fcfcfc;">
    <strong style="color: #7d7d7d;">🥈 SILVER: Clean & Validated</strong><br>
    Apply business rules: Duration > 0, Fare > 0. Separated anomalies from clean trips.
  </div>
  <div style="border-left: 8px solid #ffd700; padding: 15px; background: #fffef0;">
    <strong style="color: #b8860b;">🥇 GOLD: Business KPIs</strong><br>
    Daily Revenue (Sum/Avg) and Hourly Demand. High-speed reads via <code>partitionBy("pickup_date")</code>.
  </div>
</div>

<hr />

<h2 align="center">🚀 Performance Optimizations</h2>



<table style="width: 100%; border-collapse: collapse; margin: 20px 0;">
  <tr style="background-color: #003366; color: white;">
    <th style="padding: 10px; border: 1px solid #ddd;">Technique</th>
    <th style="padding: 10px; border: 1px solid #ddd;">Implementation</th>
  </tr>
  <tr>
    <td style="padding: 10px; border: 1px solid #ddd;"><b>Explicit Schema</b></td>
    <td style="padding: 10px; border: 1px solid #ddd;">Defined <code>StructType</code> to avoid expensive CSV scanning.</td>
  </tr>
  <tr>
    <td style="padding: 10px; border: 1px solid #ddd;"><b>Partition Pruning</b></td>
    <td style="padding: 10px; border: 1px solid #ddd;">Organized files by date to skip 99% of data during queries.</td>
  </tr>
  <tr>
    <td style="padding: 10px; border: 1px solid #ddd;"><b>Shuffle Tuning</b></td>
    <td style="padding: 10px; border: 1px solid #ddd;">Managed 200 partitions to prevent memory spill in 111M rows.</td>
  </tr>
</table>

<hr />

<h2 align="center">💰 Daily Revenue Summary</h2>
<div style="border: 2px solid #28a745; border-radius: 12px; margin: 20px; overflow: hidden;">
  <div style="background-color: #28a745; color: white; padding: 10px; text-align: center;">
    <strong>Gold Layer BI Report</strong>
  </div>
  <div style="padding: 20px; text-align: center; background: white;">
    <p><strong>Total Trips:</strong> 111,234,626 Processed</p>
    <p><strong>KPIs:</strong> Total Revenue, Trip Count, Avg Trip Value</p>
    <code>Query Logic: groupBy("pickup_date").agg(sum("total_amount"))</code>
  </div>
</div>

<hr />

<div align="center">
  <h2>🌟 About Me</h2>
  <p>
    <strong>Abdul Khadir</strong><br>
    Diploma in Computer Science | Aspiring Data Engineer<br>
    <em>Building high-performance data architectures for the modern world.</em>
  </p>
</div>
