# Batch Scoring Deep Learning Models With Azure Machine Learning

## Overview
As described in the associated page on the [Azure Reference Architecture center](https://docs.microsoft.com/en-us/azure/architecture/reference-architectures/ai/batch-scoring-deep-learning), in this repository, we use the scenario of applying style transfer onto a video (collection of images). This architecture can be generalized for any batch scoring with deep learning scenario. An alternative solution using Azure Kubernetes Service can be found [here](https://github.com/Azure/Batch-Scoring-Deep-Learning-Models-With-AKS).

## Design
![Reference Architecture Diagram](https://happypathspublic.blob.core.windows.net/assets/batch_scoring_for_dl/batchscoringdl-aml-architecture-diagram.jpg)

The above architecture works as follows:
1. Upload a video file to storage.
2. The video file will trigger Logic App to send a request to the AML pipeline published endpoint.
3. The pipeline will then process the video, apply style transfer with MPI, and postprocess the video.
4. The output will be saved back to blob storage once the pipeline is completed.

### What is Neural Style Transfer 

| Style image: | Input/content video: | Output video: | 
|--------|--------|---------|
| <img src="https://happypathspublic.blob.core.windows.net/assets/batch_scoring_for_dl/style_image.jpg" width="300"> | [<img src="https://happypathspublic.blob.core.windows.net/assets/batch_scoring_for_dl/input_video_image_0.jpg" width="300" height="300">](https://happypathspublic.blob.core.windows.net/assets/batch_scoring_for_dl/input_video.mp4 "Input Video") *click to view video* | [<img src="https://happypathspublic.blob.core.windows.net/assets/batch_scoring_for_dl/output_video_image_0.jpg" width="300" height="300">](https://happypathspublic.blob.core.windows.net/assets/batch_scoring_for_dl/output_video.mp4 "Output Video") *click to view* |


## Setup

```bash

## navigate to wherever you clone your dev repos
git clone https://github.com/Azure/Batch-Scoring-Deep-Learning-Models-With-AML batch-score

cd batch-score

## this will create a conda environment called __batchscoringdl_aml__
conda env create -f environment.yml
conda activate batchscoringdl_aml

## login to Azure
az login
```


## Steps
Run throught the following notebooks:
1. [Test the scripts](notebooks/01_local_testing.ipynb)
2. [Setup AML](notebooks/02_setup_aml.ipynb).
3. [Develop & publish AML pipeline](notebooks/03_develop_pipeline.ipynb)
4. [Deploy Logic Apps](notebooks/04_deploy_logic_apps.ipynb)
5. [Clean up](notebooks/05_clean_up.ipynb)

## Clean up
To clean up your working directory, you can run the `clean_up.sh` script that comes with this repo. This will remove all temporary directories that were generated as well as any configuration (such as Dockerfiles) that were created during the tutorials. This script will _not_ remove the `.env` file. 

To clean up your Azure resources, you can simply delete the resource group that all your resources were deployed into. This can be done in the `az group delete --name <name-of-your-resource-group>`. 

All the step above are covered in the final [notebook](notebooks/05_clean_up.ipynb).

