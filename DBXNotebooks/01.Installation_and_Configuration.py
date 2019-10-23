# Databricks notebook source
# MAGIC %md Now we support installing AML SDK as library from GUI. When attaching a library follow this https://docs.databricks.com/user-guide/libraries.html and add the below string as your PyPi package (during private preview). You can select the option to attach the library to all clusters or just one cluster.
# MAGIC 
# MAGIC Provide this full string to install the SDK:
# MAGIC 
# MAGIC azureml-sdk[databricks]

# COMMAND ----------

import azureml.core

# Check core SDK version number - based on build number of preview/master.
print("SDK version:", azureml.core.VERSION)

# COMMAND ----------

subscription_id = "<your-subscription-id>"
resource_group = "<your-existing-resource-group>"
workspace_name = "<a-new-or-existing-workspace; it is unrelated to Databricks workspace>"
workspace_region = "<your-resource group-region>"

# COMMAND ----------

# import the Workspace class and check the azureml SDK version
# exist_ok checks if workspace exists or not.

from azureml.core import Workspace

ws = Workspace.create(name = workspace_name,
                      subscription_id = subscription_id,
                      resource_group = resource_group, 
                      location = workspace_region,
                      exist_ok=True)

ws.get_details()

# COMMAND ----------

ws = Workspace(workspace_name = workspace_name,
               subscription_id = subscription_id,
               resource_group = resource_group)

# persist the subscription id, resource group name, and workspace name in aml_config/config.json.
ws.write_config()

# COMMAND ----------

# MAGIC %sh
# MAGIC cat /databricks/driver/aml_config/config.json

# COMMAND ----------

# import the Workspace class and check the azureml SDK version
from azureml.core import Workspace

ws = Workspace.from_config()
print('Workspace name: ' + ws.name, 
      'Azure region: ' + ws.location, 
      'Subscription id: ' + ws.subscription_id, 
      'Resource group: ' + ws.resource_group, sep = '\n')

# COMMAND ----------

dbutils.notebook.exit("success")

# COMMAND ----------

