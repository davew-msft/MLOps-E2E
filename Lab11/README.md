## Lab 11:  Let's look at a Classifier

In this lab a data scientist uses DL in Azure Notebooks to train a keras model against our parts descriptions.  We use AMLS to help with the training, logging, and deployment of the model.  

This exercise is geared to a data scientist.  


### Discussion topics before we start this section  

1. Keras vs pytorch?  
2. difference between running AzNotebooks on free tier and training on remote compute
1. %%writefile


## Steps

1. Deploy a GPU compute cluster (3 nodes, NC series is fine) as a `Machine Learning Compute` compute resource.  Name it `gpucluster`. 
1. Open Jupyter (from the Compute instance in AMLS) and navigate to `jupyter-notebooks/Deep Learning with Text.ipynb`. This is the notebook you will step through executing in this lab.
  * if you want to build your own model using your own datasets then consider starting with `jupyter-notebooks-starter` folder.  
1. Follow the instructions within the notebook to complete the lab.
1. In Azure Notebooks navigate to the `models` folder (under `jupyter-notebooks`) and download the **model.h5** file to your local disk. We will use the downloaded model file in the next exercise. *Note that if the downloaded file name is changed to `utf-8''model.h5`, then rename the file back to `model.h5`*.

    >**Note**: The **model.h5** file is generated during the execution of the notebook at the previous step (step 2). When running the notebook, make sure the execution is successful and the file is correctly created.

