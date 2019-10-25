## Lab 23:  Test Our Pipelines

Now that we have the build and release pipelines configured, let's test them.  


### Discussion topics before we start this section  

1. epochs and learning rate
2. 

## Steps

### Make Edits to Source Code

1. **Edit** `scripts/train.py`.  This is very close to the version we created in AzNotebooks.  

3. Change the **learning rate (lr)** for the optimizer from **0.1** to **0.001**.

4. Change the number of training **epochs** from **1** to **5**.

5. Select **Commit**.

    ![Make edits to train.py by changing the learning rate. Select Commit after editing.](../images/44_1.png 'Edit Train.py')
    
6. Provide comment: `Improving model performance: changed learning rate.` and select **Commit**.

    ![Provide commit comment for train.py.](../images/45_1.png 'Commit - Comment')
    
### Task 2: Monitor Build Pipeline

1. Navigate to **Pipelines, Builds**. Observe that the CI build is triggered because of the source code change. 

2. Select the pipeline run and monitor the pipeline steps. The pipeline will run for 20 minutes. Proceed to the next task when the build pipeline successfully completes.
    

### Task 3: Monitor Release Pipeline

1. Navigate to **Pipelines, Releases**. Observe that the Release pipeline is automatically triggered upon successful completion of the build pipeline. Select as shown in the figure to view pipeline logs. 
    
   ![Navigate to Pipelines, Releases and Select as shown in the figure to view pipeline logs.](../images/48.png 'Pipelines - Releases')
   
2. The release pipeline will run for about 15 minutes. Proceed to the next task when the release pipeline successfully completes.

### Task 4: Review Release Pipeline Outputs

1. From the pipeline logs view, select **Deploy & Test Webservice** task to view details.

    ![Select Deploy & Test Webservice task to view details.](../images/50.png 'Pipeline Logs')
    
2. Observe the **Scoring URI** and **API Key** for the deployed webservice. Please note down both the `Scoring URI` and `API Key`.

Examples:

|Name|Value|Example|
|----|-----|--------|
|Scoring URI||http://40.121.22.12:80/api/v1/service/compliance-classifier-service/score |
|API Key||0eukNRewJss1wBU23ddSAnWGfXN7qk7M|

![View Deploy & Test Webservice task logs and note down the Scoring URI of the deployed webservice.](../images/51.png 'Deploy & Test Webservice Task Logs')

3. In AMLS go to your deployed webservice.  You can see the values there as well.  

    ![View deployed webservice in Azure Portal.](../images/52.png 'Azure Portal - Workspace, Deployments')




## Testing the deployed solution

In this exercise, you verify that the first release of the application works.

### Task 1: Test the Deployment

1. Browse to your Azure Notebooks project and navigate to `Test Deployment.ipynb`. This is the notebook you will step through executing in this lab.

 
