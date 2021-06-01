## Lab 13:  Pipelines and Inference Deployment

You just transformed the experimental notebook into a Python script that can be managed and run independently of the notebook environment. You used the script to train the model, then you used code in the notebook to register the model that the script produced.

 Your team would like to have the training, registration, and future steps such as evaluation be easily reproduced and increase the speed and scale of those steps being executed. To achieve this objective, you'll encapsulate both model training and model registration as steps in an Azure ML pipeline which utilizes provisioned on-demand scalable Azure compute targets. The Azure compute target optimizes the time spent running training with a full set of data and can scale down to no cost when the job is done.

In order to improve their insurance application approval software, the team would also like a real-time prediction of the likelihood that a driver will file a claim. To accomplish this objective, you'll deploy the registered model as a real-time inferencing service using the provided model scoring script.


### Discussion topics before we start this section  

* [What are AMLS pipelines?](https://docs.microsoft.com/azure/machine-learning/concept-ml-pipelines)
* [Create and run machine learning pipelines with Azure Machine Learning SDK](https://docs.microsoft.com/azure/machine-learning/how-to-create-your-first-pipeline)
* [Troubleshooting machine learning pipelines](https://docs.microsoft.com/azure/machine-learning/how-to-debug-pipelines)


### Steps
1. Consider building an Azure ML compute target on which to run the pipeline and its steps.  If you do this now it will save time during the lab.  Any small cluster will do.  
    * To avoid automatic scale down of Azure ML managed compute the training compute option **Idle seconds before scale down** has been set to 1800. This can save time between pipeline runs if you are frequently debugging AML pipelines.  **Or set the minimum nodes to 1.**  
1. Navigate to [Lab12/pipelines.ipynb](./pipelines.ipynb). 
    * upload this notebook to your JupyterLab and run through the cells



## Helpful Hints


## Resources

* [Documentation - What are compute targets in Azure Machine Learning?](https://docs.microsoft.com/azure/machine-learning/concept-compute-target)
* [Create Azure Machine Learning datasets](https://docs.microsoft.com/en-us/azure/machine-learning/how-to-create-register-datasets)
* [Tutorial: Convert ML experiments to production Python code](https://docs.microsoft.com/en-gb/azure/machine-learning/tutorial-convert-ml-experiment-to-production)