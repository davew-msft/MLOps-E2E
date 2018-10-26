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

# MAGIC %md Please ensure you have run all previous notebooks in sequence before running this. This notebook uses image from ACI notebook for deploying to AKS.

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

# List images by ws

from azureml.core.image import ContainerImage
for i in ContainerImage.list(workspace = ws):
    print('{}(v.{} [{}]) stored at {} with build log {}'.format(i.name, i.version, i.creation_state, i.image_location, i.image_build_log_uri))

# COMMAND ----------

from azureml.core.image import Image
myimage = Image(workspace=ws, id="bikebuyeraciws:1")

# COMMAND ----------

#create AKS compute
#it may take 20-25 minutes to create a new cluster

from azureml.core.compute import AksCompute, ComputeTarget

# Use the default configuration (can also provide parameters to customize)
prov_config = AksCompute.provisioning_configuration()

aks_name = 'bb-aks-clus1' 

# Create the cluster
aks_target = ComputeTarget.create(workspace = ws, 
                                  name = aks_name, 
                                  provisioning_configuration = prov_config)

aks_target.wait_for_completion(show_output = True)

print(aks_target.provisioning_state)
print(aks_target.provisioning_errors)

# COMMAND ----------

from azureml.core.webservice import Webservice
help( Webservice.deploy_from_image)

# COMMAND ----------

from azureml.core.webservice import Webservice, AksWebservice
from azureml.core.image import ContainerImage

#Set the web service configuration (using default here)
aks_config = AksWebservice.deploy_configuration()

#unique service name
service_name ='bb-aks-service'

# Webservice creation using single command, there is a variant to use image directly as well.
aks_service = Webservice.deploy_from_image(
  workspace=ws, 
  name=service_name,
  deployment_config = aks_config,
  image = myimage,
  deployment_target = aks_target
    )

aks_service.wait_for_deployment(show_output=True)

# COMMAND ----------

#for using the Web HTTP API 
print(aks_service.scoring_uri)
print(aks_service.get_keys())

# COMMAND ----------

import json

#get the some sample data
test_data_path = "BikeBuyerTest"
test = spark.read.parquet(test_data_path).limit(5)

test_json = json.dumps(test.toJSON().collect())

print(test_json)

# COMMAND ----------

#using data defined above predict if customer will buy a bike Yes (1) or No (0)
aks_service.run(input_data=test_json)

# COMMAND ----------

#comment to not delete the web service
aks_service.delete()
#image.delete()
#model.delete()
#aks_target.delete()

# COMMAND ----------

