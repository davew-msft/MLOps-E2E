# Databricks notebook source
# MAGIC %md # Data Ingestion

# COMMAND ----------

# Download adworks-bike-purchases.csv from GitHub. This file has 9133 rows.
import os
import urllib

basedataurl = "https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/BikeBuyer/LoyaltyCardBuyers"
datafile = "adworks-bike-purchases.csv"
datafile_dbfs = os.path.join("/dbfs", datafile)

if os.path.isfile(datafile_dbfs):
    print("found {} at {}".format(datafile, datafile_dbfs))
else:
    print("downloading {} to {}".format(datafile, datafile_dbfs))
    urllib.request.urlretrieve(os.path.join(basedataurl, datafile), datafile_dbfs)

# COMMAND ----------

# MAGIC %sh
# MAGIC cat /dbfs/adworks-bike-purchases.csv

# COMMAND ----------

# Create a Spark dataframe out of the csv file.
data_all = sqlContext.read.format('csv').options(header='true', inferSchema='true', ignoreLeadingWhiteSpace='true', ignoreTrailingWhiteSpace='true').load(datafile)
print("({}, {})".format(data_all.count(), len(data_all.columns)))
data_all.printSchema()

# COMMAND ----------

data_all.head(5)

# COMMAND ----------

display(data_all.limit(5))

# COMMAND ----------

