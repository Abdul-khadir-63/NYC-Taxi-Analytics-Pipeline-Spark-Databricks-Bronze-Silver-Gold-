# ============================================================
# SILVER LAYER — DATA CLEANING & BUSINESS VALIDATION
# ============================================================
# Goal:
# Transform raw Bronze data into a clean, business-trusted dataset.
#
# Silver layer responsibilities:
# - Parse timestamps
# - Engineer duration
# - Identify anomalies
# - Separate valid vs invalid trips
# - Preserve bad data for audit
# ============================================================

from pyspark.sql.functions import col, to_timestamp
import pyspark.sql.functions as F

# ------------------------------------------------------------
# Step 1 — Read Bronze data
# ------------------------------------------------------------
# Bronze contains raw ingested dataset without business validation.
# ------------------------------------------------------------

df = spark.read.parquet(
    "/Volumes/workspace/default/day_20_project/bronze/taxi_raw_data"
)

# ------------------------------------------------------------
# Step 2 — Parse timestamp columns
# ------------------------------------------------------------
# Convert string timestamps into proper Spark timestamp format.
# This ensures time-based calculations are accurate.
# ------------------------------------------------------------

df = df.withColumn(
    "pickup_time",
    to_timestamp(col("tpep_pickup_datetime"), "MM/dd/yyyy hh:mm:ss a")
).withColumn(
    "dropoff_time",
    to_timestamp(col("tpep_dropoff_datetime"), "MM/dd/yyyy hh:mm:ss a")
)

# ------------------------------------------------------------
# Step 3 — Create trip duration (in minutes)
# ------------------------------------------------------------
# Business metric:
# Duration = dropoff - pickup
# ------------------------------------------------------------

df = df.withColumn(
    "trip_duration_minutes",
    (F.unix_timestamp("dropoff_time") -
     F.unix_timestamp("pickup_time")) / 60
)

# ============================================================
# DATA QUALITY ANALYSIS (Before Cleaning)
# ============================================================
# Important rule:
# Never clean blindly.
# Always measure anomalies first.
# ============================================================

# -------------------------------
# Timestamp checks
# -------------------------------

print("Null pickup_time:",
      df.filter(col("pickup_time").isNull()).count())

print("Null dropoff_time:",
      df.filter(col("dropoff_time").isNull()).count())

print("Trips where pickup > dropoff:",
      df.filter(col("pickup_time") > col("dropoff_time")).count())


# -------------------------------
# Duration checks
# -------------------------------

print("Negative duration trips:",
      df.filter(col("trip_duration_minutes") < 0).count())

print("Zero duration trips:",
      df.filter(col("trip_duration_minutes") == 0).count())


# -------------------------------
# Fare anomaly checks
# -------------------------------

df.select(
    F.count(F.when(col("fare_amount") < 0, 1)).alias("Negative fares"),
    F.count(F.when(col("fare_amount") == 0, 1)).alias("Zero fares"),
    F.count(F.when(col("fare_amount") > 1000, 1)).alias("Extreme fares")
).show()


# ============================================================
# SILVER BUSINESS RULE — VALID TRIP LOGIC
# ============================================================
# A trip is considered valid only if:
# - Duration > 0
# - Fare > 0
# - Passenger count > 0
# - Pickup occurs before dropoff
# ============================================================

is_valid = (
    (F.col("trip_duration_minutes") > 0) &
    (F.col("fare_amount") > 0) &
    (F.col("passenger_count") > 0) &
    (F.col("pickup_time") <= F.col("dropoff_time"))
)

# Clean dataset
valid_trips_silver = df.filter(is_valid)

# Anomaly dataset (kept for audit / investigation)
anomaly_trips_silver = df.filter(~is_valid)


# ------------------------------------------------------------
# Validation summary
# ------------------------------------------------------------

total_initial = df.count()
valid_count = valid_trips_silver.count()
anomaly_count = anomaly_trips_silver.count()

print("="*50)
print(f"TOTAL ROWS: {total_initial}")
print(f"VALID ROWS: {valid_count}")
print(f"ANOMALIES:  {anomaly_count}")
print("="*50)


# ============================================================
# Write Silver outputs
# ============================================================

valid_trips_silver.write.mode("overwrite").parquet(
    "/Volumes/workspace/default/day_20_project/silver/clean_valid_trips"
)

anomaly_trips_silver.write.mode("overwrite").parquet(
    "/Volumes/workspace/default/day_20_project/silver/anomalies"
)

print("Silver layer created successfully.")
