## Lab 20:  Setup GitHub for MLOps

*I'm not a github actions expert so I hope this works repeatably.  I've provided reference material at the bottom of this page*

### Discussion topics before we start this section  

This lab assembles all of the pieces needed in github to be ready to deploy an ML model using MLOps principles.  We are going to deploy our text classifier model using github actions.  



## Steps

1. Navigate to your git repo on gh.  If needed, push your changes from your repo to gh as a new remote.  
1. **You will need to work with your data scientist to determine the name of the experiment.** It _might_ be `deep-learning`.  


### Setup Github Actions

1. Click `Actions` in your repo on github
1. Note that it wants to build a file called `./.github/workflows/main.yml`
1. For now, just commit that file.  

### Setup Service Principals and secrets

1. A service principal needs to be generated for authentication and getting access to your Azure subscription. I suggest adding a service principal with contributor rights to the RG where you have deployed your existing Azure Machine Learning workspace. 
1. Login to Azure Portal and navigate to the details pane of your AMLS workspace.  
1. Start CloudShell
1. Run the following after changing the vars:

```bash
# CHANGE ME
SP_NAME='davew-ghaction-svcprn'
SUB_ID='52061d21-01dd-4f9e-aca9-60fff4d67ee2'
RG='MLOpsWorkshop'
SCOPES="/subscriptions/$SUB_ID/resourceGroups/$RG"

az ad sp create-for-rbac --name $SP_NAME \
                         --role contributor \
                         --scopes $SCOPES \
                         --sdk-auth

```

The output should look something like this:

```JSON
{
  "clientId": "767c9788-931d-4552-a76d-1b858c1a3fad",
  "clientSecret": "blahblahblah",
  "subscriptionId": "52061d21-01dd-4f9e-aca9-60fff4d67ee2",
  "tenantId": "72f988bf-86f1-41af-91ab-2d7cd011db47",
  "activeDirectoryEndpointUrl": "https://login.microsoftonline.com",
  "resourceManagerEndpointUrl": "https://management.azure.com/",
  "activeDirectoryGraphResourceId": "https://graph.windows.net/",
  "sqlManagementEndpointUrl": "https://management.core.windows.net:8443/",
  "galleryEndpointUrl": "https://gallery.azure.com/",
  "managementEndpointUrl": "https://management.core.windows.net/"
}
```

Add this JSON as a secret called `AZURE_CREDENTIALS` in your GH repo:

1. click on the Settings tab in your repository
1. then click on Secrets 
1. add the new secret with the name `AZURE_CREDENTIALS` 

### Create a workspace config file

1. Create the file in your repo under [./.cloud/.azure/workspace.json](../.cloud/.azure/workspace.json).  I have created one for you pointed to MY workspace, please change that file and commit and push to gh.  The file follows this format:

```JSON
{
    "name": "<your-workspace-name>",
    "resource_group": "<your-resource-group-name>",
    "create_workspace": true
}
```

At this point, the process of pushing this change to gh should've started our "shell" workflow that we created in the beginning of this lab.  Click the `Actions` option in gh and check that the workflow launched (it probably didn't do anything).  



## What's Next?

In the next lab, we are going to build the github action to "build" the MLOps Pipeline.  This will include:

* whenever a change is committed we will trigger a build
* the build will check out the code then
* then do a bunch of "environment setup"
* then connect to our AMLS workspace
* we will use the latest code to train the model using our compute instance in AMLS (or build one if needed)
* look at the metrics (accuracy in this case) for the new model and if it is better than what we have we will deploy the new model

## Reference Documentation

* [github actions marketplace for AMLS](https://github.com/marketplace/actions/azure-machine-learning-compute-action)
* [MLOps github actions](https://mlops-github.com/actions.html)
