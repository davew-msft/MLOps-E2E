## Lab 23:  Test Our Pipelines

TODO


### Discussion topics before we start this section  

1. 
2. 

## Steps



    
## Exercise 6: Test Build and Release Pipelines

Duration: 30 minutes

### Task 1: Make Edits to Source Code

1. Navigate to: **Repos -> Files -> scripts -> train.py**.

2. **Edit** `train.py`.

3. Change the **learning rate (lr)** for the optimizer from **0.1** to **0.001**.

4. Change the number of training **epochs** from **1** to **5**.

5. Select **Commit**.

    ![Make edits to train.py by changing the learning rate. Select Commit after editing.](media/44_1.png 'Edit Train.py')
    
6. Provide comment: `Improving model performance: changed learning rate.` and select **Commit**.

    ![Provide commit comment for train.py.](media/45_1.png 'Commit - Comment')
    
### Task 2: Monitor Build Pipeline

1. Navigate to **Pipelines, Builds**. Observe that the CI build is triggered because of the source code change. 

   ![Navigate to Pipelines, Builds.](media/46_1.png 'Pipelines - Builds')
   
2. Select the pipeline run and monitor the pipeline steps. The pipeline will run for 16-18 minutes. Proceed to the next task when the build pipeline successfully completes.
    
   ![Monitor Build Pipeline. It will take around 16-18 minutes to complete.](media/47.png 'Build Pipeline Steps')

### Task 3: Monitor Release Pipeline

1. Navigate to **Pipelines, Releases**. Observe that the Release pipeline is automatically trigger upon successful completion of the build pipeline. Select as shown in the figure to view pipeline logs. 
    
   ![Navigate to Pipelines, Releases and Select as shown in the figure to view pipeline logs.](media/48.png 'Pipelines - Releases')
   
2. The release pipeline will run for about 15 minutes. Proceed to the next task when the release pipeline successfully completes.

### Task 4: Review Release Pipeline Outputs

1. From the pipeline logs view, select **Deploy & Test Webservice** task to view details.

    ![Select Deploy & Test Webservice task to view details.](media/50.png 'Pipeline Logs')
    
2. Observe the **Scoring URI** and **API Key** for the deployed webservice. Please note down both the `Scoring URI` and `API Key` for *Exercise 7*.

    ![View Deploy & Test Webservice task logs and note down the Scoring URI of the deployed webservice.](media/51.png 'Deploy & Test Webservice Task Logs')

3. Log in to Azure Portal. Open your **Resource Group, Workspace, Deployments** section, and observe the deployed webservice: **compliance-classifier-service**.

    ![View deployed webservice in Azure Portal.](media/52.png 'Azure Portal - Workspace, Deployments')
