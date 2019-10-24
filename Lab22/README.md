## Lab 22:  Setup and Run a Release Pipeline

TODO


### Discussion topics before we start this section  

1. 
2. 

## Steps

1. Return to Azure DevOps and navigate to **Pipelines, Releases** and select **New pipeline**.

    ![To create new Release Pipeline navigate to Pipelines, Releases and select New pipeline.](media/19.png 'New Release Pipeline')

2. Select **Empty job**. 

    ![Select empty job to start building the release pipeline.](../images/20.png 'Select a template: Empty job')

3. Provide Stage name: `Deploy & Test` and close the dialog.

1. Select **Add an artifact**.

    ![Add a new artifact to the release pipeline.](../images/22.png 'Add an artifact')

2. Select Source type: `Build`, follow the prompts:  

    ![Provide information to add the build artifact.](../images/23.png 'Add a build artifact')
    
2. Open the **Variables** tab.

    ![Open variables tab.](../images/25.png 'Release Pipeline Variables')

3. Add four Pipeline variables as name - value pairs and then select **Save**:

    a. Name: `aks_name` Value: `<use the aks name from your AMLS workspace`
    
    b. Name: `description` Value: `"Compliance Classifier Web Service"` *Note the double quotes around description value*.
    
    c. Name: `service_name` Value: `compliance-classifier-service`

    d. Name: `aks_region` Value: `eastus`

    >**Note**:
    >- Keep the scope for the variables to `Deploy & Test` stage.
    >- The name of the Azure region should be the same one that was used to create Azure Machine Learning workspace earlier on.
    
      ![Add four pipeline variables as name value pairs and save.](../images/26.png 'Add Pipeline Variables')
      
### Setup Agent Pool for Deploy & Test stage
        
1. Open the **Tasks** tab.

    ![Open view stage tasks link.](../images/27.png 'Pipeline Tasks')
    
2. Select **Agent job** and change **Agent pool** to `Azure Pipelines` and change **Agent Specification** to `ubuntu-16.04`.

    ![Change Agent pool to be Hosted Ubuntu 1604.](../images/28_2.png 'Agent Job Setup')
    
### Add Use Python Version task

1. Select **Add a task to Agent job**, search for `Use Python Version`, and select **Add**.

    ![Add Use Python Version task to Agent job.](../images/29.png 'Add Use Python Version Task')

2. Provide **Display name:** `Use Python 3.6` and **Version spec:** `3.6`.

    ![Provide Display name and Version spec for the Use Python version task.](../images/30.png 'Use Python Version Task Dialog')
    
### Add Install Requirements task

1. Select **Add a task to Agent job**, search for `Bash`, and select **Add**.
    
    ![Add Bash task to Agent job.](../images/31.png 'Add Bash Task')

2. Provide **Display name:** `Install Requirements` and select **object browser ...** to provide **Script Path**.

    ![Provide Display name for the Bash task.](../images/32.png 'Bash Task Dialog')

3. Navigate to **Linked artifacts/_mlops-quickstart/devops-for-ai/environment_setup** and select **install_requirements.sh**.

    ![Provide Script Path to the Install Requirements bash file.](../images/33.png 'Select Path Dialog')

4. Expand **Advanced** and select **object browser ...** to provide **Working Directory**.

    ![Expand advanced section to provide Working Directory.](../images/34.png 'Bash Task - Advanced Section')
    
5. Navigate to **Linked artifacts/_mlops-quickstart/devops-for-ai** and select **environment_setup**.

    ![Provide path to the Working Directory.](../images/35.png 'Select Path Dialog')
    
### Add Deploy & Test Webservice task
    
1. Select **Add a task to Agent job**.

    ![Select Add a task to Agent job.](../images/36_1.png 'Add a Task to Agent job')
    
2. Search for `Azure CLI`, and select **Add**

    ![Add Azure CLI task to Agent job.](../images/36_2.png 'Azure CLI Task')

3. Provide the following information for the Azure CLI task:

    a. Display name: `Deploy & Test Webservice`
    
    b. Azure subscription: *This is the service connection*.
    
    c. Script Location: `Inline script`
    
    d. Inline Script: `python aml_service/deploy.py --service_name $(service_name) --aks_name $(aks_name) --aks_region $(aks_region) --description $(description)`
    
      ![Setup the Azure CLI task using the information above.](../images/38.png 'Azure CLI Task Dialog')

4. Expand **Advanced** and provide **Working Directory:** `$(System.DefaultWorkingDirectory)/_mlops-quickstart/devops-for-ai`.

    ![Provide Working Directory for the Azure CLI task.](../images/39.png 'Azure CLI Task - Working Directory')
    

>Please review the code in `aml_service/deploy.py`. This step will read the `eval_info.json` and if the evaluation step recommended to deploy the new trained model, it will deploy the new model to production in an **Azure Kubernetes Service (AKS)** cluster.

### Define Deployment Trigger

1. Navigate to **Pipeline** tab, and select **Pre-deployment conditions** for the `Deploy & Test` stage.

2. Select **After release**.

    ![Setup Pre-deployment conditions for the Deploy & Test stage.](../images/40.png 'Pre-deployment Conditions Dialog')

3. Close the dialog.

### Enable Continuous Deployment Trigger

1. Select **Continuous deployment trigger** for `_mlops-quickstart` artifact.

2. Enable: **Creates a release every time a new build is available**.

    ![Enable Continuous Deployment Trigger for the Release pipeline.](../images/41.png 'Continuous Deployment Trigger Dialog')
    
3. Close the dialog

### Task 10: Save the Release Pipeline

1. Provide name: `Classifier Release Pipeline`.

2. Select: **Save**.

    ![Provide name for the release pipeline and select save.](../images/42.png 'Save')

3. Select: **Ok**.

    ![Select Ok.](../images/43.png 'Save - Ok')


We will test everything in the next lab.  