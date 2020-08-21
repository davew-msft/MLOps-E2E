# Automated Machine Learning

automl builds ML models for you by automating model and hyperparameter selection. Bring a labelled dataset that you want to build a model for, automated ML will give you a high quality machine learning model that you can use for predictions.

If you are new to Data Science, automated ML will help you get jumpstarted by simplifying machine learning model building. It abstracts you from needing to perform model selection, hyperparameter selection, and in one step creates a high quality trained model for you to use.

If you are an experienced data scientist, automated ML will help increase your productivity by intelligently performing the model and hyperparameter selection for your training and generates high quality models much quicker than manually specifying several combinations of the parameters and running training jobs. Automated ML provides visibility and access to all the training jobs and the performance characteristics of the models to help you further tune the pipeline if you desire.

automl with AMLS can be setup and run using

* the azure portal/ml workspace (GUI experience):  we use this method for this lab
* Jupyter notebooks in a AMLS compute target
  * [Here are some examples for various use cases](https://github.com/Azure/MachineLearningNotebooks/tree/master/how-to-use-azureml/automated-machine-learning)
* any other python environment where we can call the AMLS APIs
* databricks

## Using Automated Machine Learning

1. Go to your AMLS workspace and select Automated Machine Learning under the authoring section.

1. Enter your experiment name, then select a compute from the list of your existing computes or [create a new compute](https://docs.microsoft.com/en-us/azure/machine-learning/service/how-to-create-portal-experiments#create-an-experiment). 

1. Select a the IBM-Employee-Attrition dataset that you had created in Lab40.

1. Preview data and keep all columns selected for training.

1. Select the training job type: **Classification**
1. Select target column: **Attrition**

1. Open “**Advanced settings**”, set the 'Primary metric' to 'AUC_weighted' and training job time to 15 minutes (for the workshop).

1. Hit "**Start**" and wait for the training job to start. You’ll be able to see the models which are created during the run, click on any of the models to open the detailed view of that model, where you can analyze the [graphs and metrics](https://docs.microsoft.com/en-us/azure/machine-learning/service/how-to-understand-automated-ml).

1. Once the run is completed, click **deploy the best model** to create a deployed endpoint from the model.


## Reference Topics

* To learn more about automated ML, see documentation [here](https://docs.microsoft.com/en-us/azure/machine-learning/service/concept-automated-ml).
* [automl sample notebooks](https://github.com/Azure/MachineLearningNotebooks/tree/master/how-to-use-azureml/automated-machine-learning)

## Optional Tasks

* Once your model has been deployed, follow these [instructions](https://docs.microsoft.com/en-us/power-bi/service-machine-learning-integration) to consume the model from Power BI.