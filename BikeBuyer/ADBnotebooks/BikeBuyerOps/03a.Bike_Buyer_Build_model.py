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

# MAGIC %md #Model Building

# COMMAND ----------

import os
import pprint
import numpy as np

from pyspark.ml import Pipeline, PipelineModel
from pyspark.ml.feature import OneHotEncoder, StringIndexer, VectorAssembler
from pyspark.ml.classification import LogisticRegression
from pyspark.ml.evaluation import BinaryClassificationEvaluator
from pyspark.ml.tuning import CrossValidator, ParamGridBuilder

# COMMAND ----------

#get the train and test datasets
train_data_path = "BikeBuyerTrain"
test_data_path = "BikeBuyerTest"

train = spark.read.parquet(train_data_path)
test = spark.read.parquet(test_data_path)

print("train: ({}, {})".format(train.count(), len(train.columns)))
print("test: ({}, {})".format(test.count(), len(test.columns)))

train.printSchema()

# COMMAND ----------

# MAGIC %md #Define ML Pipeline

# COMMAND ----------

label = "BikeBuyer"

reg = 0.1
print("Regularization Rate is {}.".format(reg))

# create a new Logistic Regression model.
lr = LogisticRegression(regParam=reg)

dtypes = dict(train.dtypes)
dtypes.pop(label)

si_xvars = []
ohe_xvars = []
featureCols = []
for idx,key in enumerate(dtypes):
    if dtypes[key] == "string":
        featureCol = "-".join([key, "encoded"])
        featureCols.append(featureCol)
        
        tmpCol = "-".join([key, "tmp"])
        # string-index and one-hot encode the string column
        #https://spark.apache.org/docs/2.3.0/api/java/org/apache/spark/ml/feature/StringIndexer.html
        #handleInvalid: Param for how to handle invalid data (unseen labels or NULL values). 
        #Options are 'skip' (filter out rows with invalid data), 'error' (throw an error), 
        #or 'keep' (put invalid data in a special additional bucket, at index numLabels). Default: "error"
        si_xvars.append(StringIndexer(inputCol=key, outputCol=tmpCol, handleInvalid="skip")) #, handleInvalid="keep"
        ohe_xvars.append(OneHotEncoder(inputCol=tmpCol, outputCol=featureCol))
    else:
        featureCols.append(key)

# string-index the label column into a column named "label"
si_label = StringIndexer(inputCol=label, outputCol='label')

# assemble the encoded feature columns in to a column named "features"
assembler = VectorAssembler(inputCols=featureCols, outputCol="features")

# put together the pipeline
pipe = Pipeline(stages=[*si_xvars, *ohe_xvars, si_label, assembler, lr])

# train the model
model = pipe.fit(train)
print(model)

# COMMAND ----------

# MAGIC %md #Tune ML Pipeline

# COMMAND ----------

regs = np.arange(0.0, 1.0, 0.2)

paramGrid = ParamGridBuilder().addGrid(lr.regParam, regs).build()
cv = CrossValidator(estimator=pipe, evaluator=BinaryClassificationEvaluator(), estimatorParamMaps=paramGrid)

# COMMAND ----------

cvModel = cv.fit(train)

# COMMAND ----------

model = cvModel.bestModel

# COMMAND ----------

# MAGIC %md #Model Evaluation

# COMMAND ----------

# make prediction
pred = model.transform(test)
output = pred[['MaritalStatus','Age','Gender','Region','Education','YearlyIncome','NumberCarsOwned','TotalChildren','NumberChildrenAtHome','HouseOwnerFlag','CommuteDistance','BikeBuyer']]
display(output.limit(25))

# COMMAND ----------

# evaluate. note only 2 metrics are supported out of the box by Spark ML.
bce = BinaryClassificationEvaluator(rawPredictionCol='rawPrediction')
au_roc = bce.setMetricName('areaUnderROC').evaluate(pred)
au_prc = bce.setMetricName('areaUnderPR').evaluate(pred)

print("Area under ROC: {}".format(au_roc))
print("Area Under PR: {}".format(au_prc))

# COMMAND ----------

# MAGIC %md #Model Persistence

# COMMAND ----------

##NOTE: by default the model is saved to and loaded from /dbfs/ instead of cwd!
model_name = "BikeBuyer.mml"
model_dbfs = os.path.join("/dbfs", model_name)

model.write().overwrite().save(model_name)
print("saved model to {}".format(model_dbfs))

# COMMAND ----------

# MAGIC %sh
# MAGIC 
# MAGIC ls -la /dbfs/BikeBuyer.mml/*

# COMMAND ----------

dbutils.notebook.exit("success")