# Databricks notebook source
# MAGIC %md
# MAGIC Azure ML & Azure Databricks notebooks by Parashar Shah.
# MAGIC 
# MAGIC Modified by Darwin Schweitzer.
# MAGIC 
# MAGIC Copyright (c) Microsoft Corporation. All rights reserved.
# MAGIC 
# MAGIC Licensed under the MIT License. 

# COMMAND ----------

# MAGIC %md Please ensure you have run all previous notebooks in sequence before running this.

# COMMAND ----------

# MAGIC %md # Data Ingestion

# COMMAND ----------

# Download data-scientist-model.csv from GitHub. This file has 4875 rows.
basedataurl = "https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/BikeBuyer/OriginalDataScientistWork/data"
datafile = "data-scientist-model.csv"
datafile_dbfs = os.path.join("/dbfs", datafile)

if os.path.isfile(datafile_dbfs):
    print("found {} at {}".format(datafile, datafile_dbfs))
else:
    print("downloading {} to {}".format(datafile, datafile_dbfs))
    urllib.request.urlretrieve(os.path.join(basedataurl, datafile), datafile_dbfs)

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

# MAGIC %md # Data Preparation

# COMMAND ----------

# Choose feature columns and the label column.
label = "BikeBuyer"
xvals_all = set(data_all.columns) - {label}

#dbutils.widgets.remove("xvars_multiselect")
dbutils.widgets.removeAll()

dbutils.widgets.multiselect('xvars_multiselect', 'MaritalStatus', xvals_all)
xvars_multiselect = dbutils.widgets.get("xvars_multiselect")
xvars = xvars_multiselect.split(",")

print("label = {}".format(label))
print("features = {}".format(xvars))

data = data_all.select([*xvars, label])

# Split data into train and test.
train, test = data.randomSplit([0.75, 0.25], seed=123)

print("train ({}, {})".format(train.count(), len(train.columns)))
print("test ({}, {})".format(test.count(), len(test.columns)))

# COMMAND ----------

# MAGIC %md #Data Persistence

# COMMAND ----------

# Write the train and test data sets to intermediate storage
train_data_path = "BikeBuyerTrain"
test_data_path = "BikeBuyerTest"

train_data_path_dbfs = os.path.join("/dbfs", "BikeBuyerTrain")
test_data_path_dbfs = os.path.join("/dbfs", "BikeBuyerTest")

train.write.mode('overwrite').parquet(train_data_path)
test.write.mode('overwrite').parquet(test_data_path)
print("train and test datasets saved to {} and {}".format(train_data_path_dbfs, test_data_path_dbfs))

# COMMAND ----------

dbutils.notebook.exit("success")