# ============================================================
# GOLD LAYER — BUSINESS KPI TABLES
# ============================================================
# Goal:
# Transform Silver clean dataset into analytics-ready tables.
#
# Gold layer responsibilities:
# - Create business KPIs
# - Aggregate at reporting level
# - Optimize partitioning for analytics
# - Provide dashboard-ready datasets
# ============================================================

import pyspark.sql.functions as F

# ------------------------------------------------------------
# Step 1 — Read clean Silver dataset
# ------------------------------------------------------------

df = spark.read.parquet(
    "/Volumes/workspace/default/day_20_project/silver/clean_valid_trips"
)

# ------------------------------------------------------------
# Step 2 — Select only required columns
# ------------------------------------------------------------
# Gold tables should contain only business-relevant fields.
# Avoid carrying unnecessary raw attributes.
# ------------------------------------------------------------

df = df.select(
    "passenger_count",
    "trip_distance",
    "pickup_time",
    "payment_type",
    "total_amount"
)

# ------------------------------------------------------------
# Step 3 — Engineer reporting dimensions
# ------------------------------------------------------------

df = df.withColumn("pickup_date", F.to_date("pickup_time"))
df = df.withColumn("pickup_hour", F.hour("pickup_time"))

# ============================================================
# GOLD TABLE 1 — DAILY REVENUE KPI
# ============================================================
# Business Questions:
# - How much revenue is generated per day?
# - How many trips occur daily?
# - What is the average trip value?
# ============================================================

# Repartition by grouping column for efficient aggregation
df_daily = df.repartition("pickup_date")

daily_revenue_gold = df_daily.groupBy("pickup_date").agg(
    F.sum("total_amount").alias("total_revenue"),
    F.count("*").alias("total_trips"),
    F.avg("total_amount").alias("avg_trip_value")
).orderBy("pickup_date")

# Write Gold daily revenue table
daily_revenue_gold.write \
    .mode("overwrite") \
    .partitionBy("pickup_date") \
    .parquet("/Volumes/workspace/default/day_20_project/gold/daily_revenue")

print("Gold table created: daily_revenue")


# ============================================================
# GOLD TABLE 2 — HOURLY DEMAND INTELLIGENCE
# ============================================================
# Business Questions:
# - Which hours have highest demand?
# - What is revenue distribution across hours?
# - Are peak hours linked to higher fares?
# ============================================================

df_hourly = df.repartition("pickup_hour")

hourly_demand_gold = df_hourly.groupBy("pickup_hour").agg(
    F.count("*").alias("trip_count"),
    F.sum("total_amount").alias("total_revenue"),
    F.avg("total_amount").alias("avg_fare_per_trip"),
    F.avg("trip_distance").alias("avg_trip_distance")
).orderBy("pickup_hour")

hourly_demand_gold.write \
    .mode("overwrite") \
    .parquet("/Volumes/workspace/default/day_20_project/gold/hourly_demand")

print("Gold table created: hourly_demand")
