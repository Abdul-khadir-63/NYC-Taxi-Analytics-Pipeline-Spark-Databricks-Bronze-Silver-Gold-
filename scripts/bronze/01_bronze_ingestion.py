# ============================================================
# BRONZE LAYER — RAW DATA INGESTION
# ============================================================
# Goal:
# Load the original taxi dataset exactly as received and store it
# safely in parquet format without modifying business logic.
#
# Bronze layer always contains:
# - raw structure
# - original business values
# - minimal transformations
# ============================================================

from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DoubleType, TimestampType

# ------------------------------------------------------------
# Step 1 — Define explicit schema
# ------------------------------------------------------------
# Why:
# - Prevent Spark from guessing column types
# - Avoid inconsistent parsing
# - Ensure stable ingestion pipeline
# - Improve performance during load
# ------------------------------------------------------------

taxi__dataset_schema = StructType([
    StructField("VendorID", IntegerType(), True),
    StructField("tpep_pickup_datetime", StringType(), True),   # kept string for controlled parsing later
    StructField("tpep_dropoff_datetime", StringType(), True),
    StructField("passenger_count", IntegerType(), True),
    StructField("trip_distance", DoubleType(), True),
    StructField("RatecodeID", IntegerType(), True),
    StructField("store_and_fwd_flag", StringType(), True),
    StructField("PULocationID", IntegerType(), True),
    StructField("DOLocationID", IntegerType(), True),
    StructField("payment_type", IntegerType(), True),
    StructField("fare_amount", DoubleType(), True),
    StructField("extra", DoubleType(), True),
    StructField("mta_tax", DoubleType(), True),
    StructField("tip_amount", DoubleType(), True),
    StructField("tolls_amount", DoubleType(), True),
    StructField("improvement_surcharge", DoubleType(), True),
    StructField("total_amount", DoubleType(), True)
])

# ------------------------------------------------------------
# Step 2 — Load CSV dataset
# ------------------------------------------------------------
# - Source: Kaggle taxi dataset (~10GB)
# - Schema applied during ingestion
# - No cleaning at this stage
# ------------------------------------------------------------

df = spark.read.csv(
    "/Volumes/workspace/default/kaggle_files/taxi_2018.csv",
    header=True,
    schema=taxi__dataset_schema
)

# ------------------------------------------------------------
# Step 3 — Store Bronze dataset in parquet format
# ------------------------------------------------------------
# Why parquet:
# - columnar storage
# - faster reads
# - compression
# - analytics friendly
#
# Bronze storage rule:
# - never modify business logic
# - only store raw structured data
# ------------------------------------------------------------

df.write.format("parquet") \
    .mode("overwrite") \
    .save("/Volumes/workspace/default/day_20_project/bronze/taxi_raw_data")

print("Bronze layer created: Raw taxi dataset stored in parquet format.")


# ============================================================
# BRONZE VALIDATION — INITIAL DATA QUALITY CHECKS
# ============================================================
# Goal:
# Verify ingestion success and understand raw data behavior
# before building Silver cleaning logic.
# ============================================================

from pyspark.sql.functions import col, count, when, length
import pyspark.sql.functions as F

# ------------------------------------------------------------
# CHECK 1 — Dataset volume validation
# ------------------------------------------------------------
# Ensures:
# - complete file loaded
# - no partial ingestion
# ------------------------------------------------------------

total_rows = df.count()
print(f"Total rows ingested into Bronze: {total_rows}")


# ------------------------------------------------------------
# CHECK 2 — Null value inspection
# ------------------------------------------------------------
# Purpose:
# - identify missing financial values
# - decide future cleaning rules
# ------------------------------------------------------------

print("Null value inspection for key business columns")

sel_col = df.select(
    "VendorID",
    "tpep_dropoff_datetime",
    "trip_distance",
    "fare_amount",
    "total_amount"
)

sel_col.select([
    count(when(col(c).isNull(), c)).alias(c)
    for c in sel_col.columns
]).show()


# ------------------------------------------------------------
# CHECK 3 — Financial anomaly detection
# ------------------------------------------------------------
# Negative fares may represent:
# - refunds
# - corrections
# - system errors
#
# Bronze keeps them unchanged.
# Cleaning happens in Silver.
# ------------------------------------------------------------

print("Sample rows with negative fare amounts")
df.select("fare_amount").filter(col("fare_amount") < 0).show(5)


# ------------------------------------------------------------
# CHECK 4 — Trip distance validation
# ------------------------------------------------------------
# Expectation:
# - no negative distances
# - zero distance may indicate cancellations
# ------------------------------------------------------------

print("Checking negative trip distances")
df.select("trip_distance").filter(col("trip_distance") < 0).show()


# ------------------------------------------------------------
# CHECK 5 — Passenger count validation
# ------------------------------------------------------------
# Zero passengers may indicate:
# - driver movement
# - cancelled rides
# ------------------------------------------------------------

print("Checking negative passenger counts")
df.select("passenger_count").filter(col("passenger_count") < 0).show()


# ------------------------------------------------------------
# CHECK 6 — Datetime format consistency
# ------------------------------------------------------------
# Purpose:
# - verify ingestion quality
# - confirm consistent timestamp pattern
# - prepare for parsing in Silver
# ------------------------------------------------------------

valid_date_count = df.filter(
    length(col("tpep_dropoff_datetime")) == 22
).count()

print(f"Rows with consistent datetime format: {valid_date_count}")

#            ========================================-------------- Note ---------------------------------------------====================


# ============================================================
# DATASET INFORMATION
# ============================================================
# Dataset: NYC Yellow Taxi Trip Records (2018)
# Source: Kaggle (Original data from NYC Taxi & Limousine Commission)
# Size: ~10GB
# Total Records: ~112 million rows
#
# Description:
# This dataset contains trip-level data including:
# - pickup and dropoff timestamps
# - passenger count
# - trip distance
# - payment type
# - fare breakdown
#
# This project builds a Bronze → Silver → Gold analytics pipeline
# using this dataset.
# ============================================================
