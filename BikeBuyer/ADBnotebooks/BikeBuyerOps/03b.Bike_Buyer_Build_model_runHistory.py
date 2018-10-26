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

import azureml.core

# Check core SDK version number
print("SDK version:", azureml.core.VERSION)

# COMMAND ----------

# import the Workspace class and check the azureml SDK version
from azureml.core import Workspace

ws = Workspace.from_config()
print('Workspace name: ' + ws.name, 
      'Azure region: ' + ws.location, 
      'Subscription id: ' + ws.subscription_id, 
      'Resource group: ' + ws.resource_group, sep = '\n')

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
        si_xvars.append(StringIndexer(inputCol=key, outputCol=tmpCol, handleInvalid="skip"))
        ohe_xvars.append(OneHotEncoder(inputCol=tmpCol, outputCol=featureCol))
    else:
        featureCols.append(key)

# string-index the label column into a column named "label"
si_label = StringIndexer(inputCol=label, outputCol='label')

# assemble the encoded feature columns in to a column named "features"
assembler = VectorAssembler(inputCols=featureCols, outputCol="features")

# COMMAND ----------

from azureml.core.run import Run
from azureml.core.experiment import Experiment
import numpy as np
import os
import shutil

model_name = "BikeBuyer_runHistory.mml"
model_dbfs = os.path.join("/dbfs", model_name)
run_history_name = 'spark-ml-notebook'

# start a training run by defining an experiment
myexperiment = Experiment(ws, "BikeBuyer_Experiment")
root_run = myexperiment.start_logging()

# Regularization Rates
regs = np.arange(0.0, 1.0, 0.2)

# try a bunch of alpha values in a Linear Regression (Ridge) model
for reg in regs:
    print("Regularization rate: {}".format(reg))
    # create a bunch of child runs
    with root_run.child_run("reg-" + str(reg)) as run:
        # create a new Logistic Regression model.
        lr = LogisticRegression(regParam=reg)
        
        # put together the pipeline
        pipe = Pipeline(stages=[*si_xvars, *ohe_xvars, si_label, assembler, lr])

        # train the model
        model_pipeline = pipe.fit(train)
        
        # make prediction
        pred = model_pipeline.transform(test)
        
        # evaluate. note only 2 metrics are supported out of the box by Spark ML.
        bce = BinaryClassificationEvaluator(rawPredictionCol='rawPrediction')
        au_roc = bce.setMetricName('areaUnderROC').evaluate(pred)
        au_prc = bce.setMetricName('areaUnderPR').evaluate(pred)

        print("Area under ROC: {}".format(au_roc))
        print("Area Under PR: {}".format(au_prc))
      
        # log reg, au_roc, au_prc and feature names in run history
        run.log("reg", reg)
        run.log("au_roc", au_roc)
        run.log("au_prc", au_prc)
        run.log_list("columns", train.columns)

        # save model
        model_pipeline.write().overwrite().save(model_name)
        
        # upload the serialized model into run history record
        mdl, ext = model_name.split(".")
        model_zip = mdl + ".zip"
        shutil.make_archive(mdl, 'zip', model_dbfs)
        run.upload_file("outputs/" + model_name, model_zip)        
        #run.upload_file("outputs/" + model_name, path_or_stream = model_dbfs) #cannot deal with folders

        # now delete the serialized model from local folder since it is already uploaded to run history 
        shutil.rmtree(model_dbfs)
        os.remove(model_zip)
        
# Declare run completed
root_run.complete()
root_run_id = root_run.id
print ("run id:", root_run.id)

# COMMAND ----------

#Load all run metrics from run history into a dictionary object.
child_runs = {}
child_run_metrics = {}

for r in root_run.get_children():
    child_runs[r.id] = r
    child_run_metrics[r.id] = r.get_metrics()

# COMMAND ----------

best_run_id = max(child_run_metrics, key = lambda k: child_run_metrics[k]['au_roc'])
best_run = child_runs[best_run_id]
print('Best run is:', best_run_id)
print('Metrics:', child_run_metrics[best_run_id])

# COMMAND ----------

best_reg = child_run_metrics[best_run_id]['reg']
max_auc = child_run_metrics[best_run_id]['au_roc']

reg_auc = np.array([(child_run_metrics[k]['reg'], child_run_metrics[k]['au_roc']) for k in child_run_metrics.keys()])
reg_auc_sorted = reg_auc[reg_auc[:,0].argsort()]

import pandas as pd
df = pd.DataFrame(reg_auc_sorted)
spdf = spark.createDataFrame(df)
display(spdf)

# COMMAND ----------

#Download the model from the best run to a local folder
best_model_file_name = "best_model.zip"
best_run.download_file(name = 'outputs/' + model_name, output_file_path = best_model_file_name)

# COMMAND ----------

# MAGIC %md #Model Evaluation

# COMMAND ----------

##unzip the model to dbfs (as load() seems to require that) and load it.
if os.path.isfile(model_dbfs) or os.path.isdir(model_dbfs):
    shutil.rmtree(model_dbfs)
shutil.unpack_archive(best_model_file_name, model_dbfs)

model_pipeline_best = PipelineModel.load(model_name)

# COMMAND ----------

# make prediction
pred = model_pipeline_best.transform(test)
output = pred[['MaritalStatus','Age','Gender','Region','Education','YearlyIncome','NumberCarsOwned','TotalChildren','NumberChildrenAtHome','HouseOwnerFlag','CommuteDistance','BikeBuyer']]
display(output.limit(5))

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
model_pipeline_best.write().overwrite().save(model_name)
print("saved model to {}".format(model_dbfs))

# COMMAND ----------

# MAGIC %sh
# MAGIC 
# MAGIC ls -la /dbfs/BikeBuyer_runHistory.mml/*

# COMMAND ----------

dbutils.notebook.exit("success")

# COMMAND ----------

