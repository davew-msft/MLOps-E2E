demo:
    Lab11/safe-driver.ipynb
    Lab12/safe-driver-prediction-v2.ipynb
    Lab12/pipelines.ipynb
    Lab12/inferencing.ipynb

HERE:  
redo the old deep learning text example as a new set of labs.  
should all be in jupyter-notebooks folder


measuring model performance and making decsions is Challenge05 in DevOps4DS


Lab 16 maps to Challenge06

good project template:  https://dev.azure.com/DAISolutions/MLOperationalization/_git/MLOpsBasic



alternate mlops workshop
    I have most of this
    https://github.com/microsoft/MCW-ML-Ops/blob/master/Hands-on%20lab/HOL%20step-by-step%20-%20MLOps.md



model deployment to iotedge:  
    https://github.com/nthacker/AML-service-labs/blob/master/lab-6/visual-studio/README.md
    https://github.com/Azure/azureml-examples/blob/main/tutorials/deploy-edge/ase-gpu.ipynb
    https://docs.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

airflow

mask detection on the edge
    https://github.com/retkowsky/MaskDetection

azfunc
    https://docs.microsoft.com/en-us/azure/machine-learning/how-to-deploy-functions

full e2e employee attrition model toward end of prezis/MLops Quick Pitch.pptx and airefarch2.pptx

papermill
    https://github.com/nteract/papermill

interface to adls
    https://github.com/dask/adlfs

gh actions:  
    https://mlops.githubapp.com//
    https://techcommunity.microsoft.com/t5/azure-ai/using-github-actions-amp-azure-machine-learning-for-mlops/ba-p/1419027
    https://github.com/Azure/azureml-examples
    https://github.com/Azure/azureml-template
    https://github.com/machine-learning-apps/ml-template-azure

transfer learning:  https://github.com/maxluk/dogbreeds-webinar

aml notebooks:  https://github.com/Azure/MachineLearningNotebooks/tree/master/how-to-use-azureml


img data labelling?
    https://github.com/balakreshnan/mlops/tree/master/MLAssitDataLabelling


mlops python:  https://github.com/microsoft/MLOpsPython
mlops:  https://github.com/microsoft/MLOps
mlops scripts templates:  
    https://github.com/anagha-microsoft/ncr-mlops-hol-code
    https://github.com/retkowsky/ncr-mlops-hol

cogsvc workshop
https://github.com/Microsoft/MCW-Cognitive-Services-and-Deep-Learning

custom vision
    You can try the Microsoft COCO DataSet - https://cocodataset.org/#home
There are implementations around the same for Azure Custom Vision. One such example below- https://github.com/vladkol/CustomVision.COCO

edge models 
    simplified 
    end-to-end AI object detection on a Raspberry Pi 3 edge
device, starting (almost) “from scratch” to consider each builing blocks of such a solution. This guide is designed
for developers as well as data scientists who wish to easily put their AI models in practice on edge devices without
focusing too much on the deployment.
    see "Bringing Computer Vision models to the Intelligent Edge with Azure IoT Edge - A guide for developers and data scientists.pdf"

dataset labeling:  https://github.com/MercyPrasanna/dataset-labeling/blob/master/dataset-labeling.ipynb


aml acceleration template, do it yourself, this might be a lab instead of my "starter" stuff
https://github.com/microsoft/aml-acceleration-template


datasets with automl and even designer...about midway down
https://github.com/shkumar64/AzureMachineLearningWorkshop

enable model data collection:
https://docs.microsoft.com/en-us/azure/machine-learning/how-to-enable-data-collection

call center analytics, audio
https://github.com/rlagh2/callcenteranalytics with powerbi


vision:  https://github.com/microsoft/computervision-recipes/
video anomaly detection:  https://github.com/microsoft/mlops_videoanomalydetection

https://github.com/lockedata/realtimeAIpipeline

audio language in containers:  https://techcommunity.microsoft.com/t5/azure-ai/automatically-detect-audio-language-with-the-speech-language/ba-p/1694363
https://techcommunity.microsoft.com/t5/azure-ai/accelerate-self-paced-learning-at-the-edge-with-speech/ba-p/1636986

autonomous driver e2e deep learning tutorial 
    https://github.com/Microsoft/AutonomousDrivingCookbook
    https://github.com/microsoft/AutonomousDrivingCookbook/tree/master/AirSimE2EDeepLearning
    seems cool
    "ML-Blueprints-for-Finance.pdf"


dask on amls
    https://github.com/danielsc/azureml-and-dask
SparkML on Databricks is more mature  & faster on large dataset and can deal with very large dataset (>100 GB).
But I don’t like Spark’s set of algorithms with limited  hyper parameters for tunning which may lead to poor prediction performance.
For example for same Randomforest algorithm on unbalanced dataset, you may have much better performance on Sklearn than on Spark ML.
If your customer doesn’t have Spark skill and is very familiar with sklearn, XGBoost…then DaskML may be easier to learn for them.
https://github.com/Azure/azureml-examples/blob/main/tutorials/using-dask

a/b testing using controlled rolloout
    https://docs.microsoft.com/en-us/azure/machine-learning/how-to-deploy-azure-kubernetes-service?tabs=python#deploy-models-to-aks-using-controlled-rollout-preview

event grid with AMLS
    https://docs.microsoft.com/en-us/azure/machine-learning/how-to-use-event-grid#sample-scenarios
# Other Resources

* [AMLS automl](https://github.com/Azure/MachineLearningNotebooks/tree/master/how-to-use-azureml/automated-machine-learning)
* [Lab 43 based on this](https://github.com/Azure/MachineLearningNotebooks/blob/master/how-to-use-azureml/automated-machine-learning/continuous-retraining/auto-ml-continuous-retraining.ipynb)
* Lab 121:  https://docs.microsoft.com/en-us/azure/machine-learning/how-to-use-mlflow-azure-databricks

## skipping for now

another mlops demo/lab/workshop
https://github.com/microsoft/ignite-learning-paths-training-aiml/blob/main/aiml50/README.md
    this is more of a demo
    model is already deployed
    model makes faulty prediction
    we build up the MLOps solution with azdo
    we change a parameter and retrain via the azdo pipeline
    everything gets deployed
    we prove the pipeline works.  

text analytics from cogs to aml to hyperdrive
    https://github.com/microsoft/ignite-learning-paths-training-aiml/blob/main/aiml40/README.md
    I have this started on the Lab301 branch

Lab400 is https://github.com/csiebler/azureml-workshop-2020
    https://github.com/csiebler/azureml-workshop-2020/blob/master/3-mlops/MLOps_with_ML_pipelines.md

Lab401 is https://github.com/csiebler/azureml-workshop-2020/blob/master/3-mlops/MLOps_basic_example.md
right now this doesn't deploy correctly

containers/onnx: this is Lab 302 
https://github.com/microsoft/ignite-learning-paths-training-aiml/blob/main/aiml20/README.md

vision on edge
    Lab 304
    https://github.com/Azure-Samples/azure-intelligent-edge-patterns/tree/master/factory-ai-vision
    https://docs.microsoft.com/en-us/azure/media-services/live-video-analytics-edge/custom-vision-tutorial?pivots=programming-language-csharp
