# Databricks notebook source
# MAGIC %md
# MAGIC Azure ML & Azure Databricks notebooks by Parashar Shah.
# MAGIC 
# MAGIC Modified by Darwin Schweitzer
# MAGIC 
# MAGIC Copyright (c) Microsoft Corporation. All rights reserved.
# MAGIC 
# MAGIC Licensed under the MIT License. 

# COMMAND ----------

# MAGIC %md Please ensure you have run all previous notebooks in sequence before running this.

# COMMAND ----------

# MAGIC %md Please Register Azure Container Instance(ACI) using Azure Portal: https://docs.microsoft.com/en-us/azure/azure-resource-manager/resource-manager-supported-services#portal in your subscription before using the SDK to deploy your ML model to ACI.

# COMMAND ----------

from azureml.core import Workspace
import azureml.core

# Check core SDK version number
print("SDK version:", azureml.core.VERSION)

#'''
ws = Workspace.from_config()
print('Workspace name: ' + ws.name, 
      'Azure region: ' + ws.location, 
      'Subscription id: ' + ws.subscription_id, 
      'Resource group: ' + ws.resource_group, sep = '\n')
#'''

# COMMAND ----------

##NOTE: service deployment always gets the model from the current working dir.
import os

model_name = "BikeBuyer.mml" # OR BikeBuyer_runHistory.mml
model_name_dbfs = os.path.join("/dbfs", model_name)

print("copy model from dbfs to local")
model_local = "file:" + os.getcwd() + "/" + model_name
dbutils.fs.cp(model_name, model_local, True)

# COMMAND ----------

#Register the model
from azureml.core.model import Model
mymodel = Model.register(model_path = model_name, # this points to a local file
                       model_name = model_name, # this is the name the model is registered as, am using same name for both path and name.                 
                       description = "ADB trained model by Darwin",
                       workspace = ws)

print(mymodel.name, mymodel.description, mymodel.version)

# COMMAND ----------

#%%writefile score_sparkml.py
score_sparkml = """

import json

def init():
    try:
        # One-time initialization of PySpark and predictive model
        import pyspark
        from azureml.core.model import Model
        from pyspark.ml import PipelineModel
        
        global trainedModel
        global spark
        
        spark = pyspark.sql.SparkSession.builder.appName("ADB and AML notebook by Darwin").getOrCreate()
        model_name = "{model_name}" #interpolated
        model_path = Model.get_model_path(model_name)
        trainedModel = PipelineModel.load(model_path)
    except Exception as e:
        trainedModel = e
    
def run(input_json):
    if isinstance(trainedModel, Exception):
        return json.dumps({{"trainedModel":str(trainedModel)}})
      
    try:
        sc = spark.sparkContext
        input_list = json.loads(input_json)
        input_rdd = sc.parallelize(input_list)
        input_df = spark.read.json(input_rdd)
    
        # Compute prediction
        prediction = trainedModel.transform(input_df)
        #result = prediction.first().prediction
        predictions = prediction.collect()

        #Get each scored result
        preds = [str(x['prediction']) for x in predictions]
        result = ",".join(preds)
    except Exception as e:
        result = str(e)
    return json.dumps({{"result":result}})
    
""".format(model_name=model_name)

exec(score_sparkml)

with open("score_sparkml.py", "w") as file:
    file.write(score_sparkml)

# COMMAND ----------

from azureml.core.conda_dependencies import CondaDependencies 

myacienv = CondaDependencies.create(conda_packages=['scikit-learn','numpy','pandas'])

with open("mydeployenv.yml","w") as f:
    f.write(myacienv.serialize_to_string())

# COMMAND ----------

#deploy to ACI
from azureml.core.webservice import AciWebservice, Webservice

myaci_config = AciWebservice.deploy_configuration(
    cpu_cores = 1, 
    memory_gb = 1, 
    tags = {'name':'BikeBuyer Databricks Azure ML ACI'}, 
    description = 'This is for ADB and AML example. Azure Databricks & Azure ML SDK demo with ACI by Darwin.')

# COMMAND ----------

# this will take 10-15 minutes to finish

service_name = "bikebuyeraciws"
runtime = "spark-py" 
driver_file = "score_sparkml.py"
my_conda_file = "mydeployenv.yml"

# image creation
from azureml.core.image import ContainerImage
myimage_config = ContainerImage.image_configuration(execution_script = driver_file, 
                                    runtime = runtime, 
                                    conda_file = my_conda_file)

# Webservice creation
myservice = Webservice.deploy_from_model(
  workspace=ws, 
  name=service_name,
  deployment_config = myaci_config,
  models = [mymodel],
  image_config = myimage_config
    )

myservice.wait_for_deployment(show_output=True)

# COMMAND ----------

help(ContainerImage)

# COMMAND ----------

# List images by ws

for i in ContainerImage.list(workspace = ws):
    print('{}(v.{} [{}]) stored at {} with build log {}'.format(i.name, i.version, i.creation_state, i.image_location, i.image_build_log_uri))

# COMMAND ----------

#for using the Web HTTP API 
print(myservice.scoring_uri)

# COMMAND ----------

import json

#get the some sample data
test_data_path = "BikeBuyerTest"
test = spark.read.parquet(test_data_path).limit(5)

test_json = json.dumps(test.toJSON().collect())

print(test_json)

# COMMAND ----------

#using data defined above predict if income is >50K (1) or <=50K (0)
myservice.run(input_data=test_json)

# COMMAND ----------

#comment to not delete the web service
myservice.delete()

# COMMAND ----------

