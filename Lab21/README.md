## Lab 21:  Setup and Run a Build Pipeline

In this lab we build the build pipeline for our ML model. This lab is lengthy and sometimes frustrating due to connectivity issues.  These are "one-time" issues.  


### Discussion topics before we start this section  

1. Review the yaml for a build pipeline
2. Service Connections errors

## Steps

1. From left navigation select **Pipelines** .  Our pipeline already shows up because we have our template yml file.  It probably also has a failure run because you just updated the variables.  That's ok.  

4. Review the YAML file.  

1. Change EVERY `azureSubscription` variable to your subscription.

>Question:  Is there a better way to do this?  

The build pipeline has four key steps:
    
* Attach folder to workspace and experiment. This command creates the `.azureml` subdirectory that contains a `config.json` file that is used to communicate with your Azure Machine Learning workspace. All subsequent steps rely on the `config.json` file to instantiate the workspace object.
    
* Create the AML Compute target to run your master pipeline for model training and model evaluation.
    
* Run the master pipeline. The master pipeline has two steps: 

  * (1) Train the machine learning model, and 
  * (2) Evaluate the trained machine learning model. 
  
  The evaluation step evaluates if the new model performance is better than the currently deployed model. If the new model performance is improved, the evaluate step will create a new Image for deployment. The results of the evaluation step will be saved in a file called `eval_info.json` that will be made available for the release pipeline. You can review the code for the master pipeline and its steps in `aml_service/pipelines_master.py`,  `scripts/train.py`, and `scripts/evaluate.py`.
    
* Publish the build artifacts. The `snapshot of the repository`, `config.json`, and `eval_info.json` files are published as build artifacts and thus can be made available for the release pipeline.

1.  Select **Save and Run** to start running the build pipeline.  

2. Monitor the build run. The build pipeline, for the first run, will take around 15-20 minutes to run.


### Review Build Artifacts

1. The build will publish an artifact named `devops-for-ai`. Select **Artifacts, devops-for-ai** to review the artifact contents.

    ![Select Artifacts, devops-for-ai to review the artifact contents.](../images/16.png 'Build Artifacts')

2. Select **outputs, eval_info.json** and then select **Download**. The `eval_info.json` is the output from the *model evaluation* step and the information from the evaluation step will be later used in the release pipeline to deploy the model. Select **Close** to close the dialog.

    ![Download output from the model evaluation step.](../images/17.png 'Download JSON file')

3. Open the `eval_info.json` in a json viewer or a text editor and observe the information. The json output contains information such as if the model passed the evaluation step (`deploy_model`: *true or false*), and the name and id of the created image (`image_name` and `image_id`) to deploy.

    ![Review information in the eval_info json file.](../images/18.png 'Eval Info JSON File')

### Review Build Outputs

1. Observe the registered model: `compliance-classifier` in AMLS.  This is likely version 3 (1 was from Jupyter and 2 was the manual model upload).  

    ![Review registered model in Azure Portal.](../images/53.png 'Registered Models in Azure Portal')

2. Observe the deployment image created during the build pipeline: `compliance-classifier-image`.

    ![Review deployment image in Azure Portal.](../images/54.png 'Images in Azure Portal')