import argparse
import os, json, sys
import azureml.core
from azureml.core import Workspace
from azureml.core import Experiment
from azureml.core.model import Model
import azureml.core
from azureml.core import Run
from azureml.core.webservice import AciWebservice, Webservice

from azureml.core.conda_dependencies import CondaDependencies 
from azureml.core.image import ContainerImage
from azureml.core import Image

print("In evaluate.py")

parser = argparse.ArgumentParser("evaluate")

parser.add_argument("--model_name", type=str, help="model name", dest="model_name", required=True)
parser.add_argument("--image_name", type=str, help="image name", dest="image_name", required=True)
parser.add_argument("--output", type=str, help="eval output directory", dest="output", required=True)

args = parser.parse_args()

print("Argument 1: %s" % args.model_name)
print("Argument 2: %s" % args.image_name)
print("Argument 3: %s" % args.output)

run = Run.get_context()
ws = run.experiment.workspace

print('Workspace configuration succeeded')

model_list = Model.list(ws, name = args.model_name)
latest_model = sorted(model_list, reverse=True, key = lambda x: x.created_time)[0]

latest_model_id = latest_model.id
latest_model_name = latest_model.name
latest_model_version = latest_model.version
latest_model_path = latest_model.get_model_path(latest_model_name, _workspace=ws)

print('Latest model id: ', latest_model_id)
print('Latest model name: ', latest_model_name)
print('Latest model version: ', latest_model_version)
print('Latest model path: ', latest_model_path)

latest_model_run_id = latest_model.tags.get("run_id")
print('Latest model run id: ', latest_model_run_id)

latest_model_run = Run(run.experiment, run_id = latest_model_run_id)

latest_model_accuracy = latest_model_run.get_metrics().get("acc")
print('Latest model accuracy: ', latest_model_accuracy)

ws_list = Webservice.list(ws, model_name = latest_model_name)
print('webservice list')
print(ws_list)

deploy_model = False
current_model = None

if(len(ws_list) > 0):
    webservice = ws_list[0]
    try:
        image_id = webservice.tags['image_id']
        image = Image(ws, id = image_id)
        current_model = image.models[0]
        print('Found current deployed model!')
    except:
        deploy_model = True
        print('Image id tag not found!')
else:
    deploy_model = True
    print('No deployed webservice for model: ', latest_model_name)

current_model_accuracy = -1 # undefined
if current_model != None:
    current_model_run = Run(run.experiment, run_id = current_model.tags.get("run_id"))
    current_model_accuracy = current_model_run.get_metrics().get("acc")
    print('accuracies')
    print(latest_model_accuracy, current_model_accuracy)
    if latest_model_accuracy > current_model_accuracy:
        deploy_model = True
        print('Current model performs better and will be deployed!')
    else:
        print('Current model does NOT perform better and thus will NOT be deployed!')

eval_info = {}
eval_info["model_name"] = latest_model_name
eval_info["model_version"] = latest_model_version
eval_info["model_path"] = latest_model_path
eval_info["model_acc"] = latest_model_accuracy
eval_info["deployed_model_acc"] = current_model_accuracy
eval_info["deploy_model"] = deploy_model
eval_info["image_name"] = args.image_name
eval_info["image_id"] = ""

os.makedirs(args.output, exist_ok=True)
eval_filepath = os.path.join(args.output, 'eval_info.json')

if deploy_model == False:
    with open(eval_filepath, "w") as f:
        json.dump(eval_info, f)
        print('eval_info.json saved')
    print('Model did not meet the accuracy criteria and will not be deployed!')
    print('Exiting')
    sys.exit(0)

# Continue to package Model and create image
print('Model accuracy has met the criteria!')
print('Proceeding to package model and create the image...')

print('Updating scoring file with the correct model name')
with open('score.py') as f:
    data = f.read()
with open('score_fixed.py', "w") as f:
    f.write(data.replace('MODEL-NAME', args.model_name)) #replace the placeholder MODEL-NAME
    print('score_fixed.py saved')

# create a Conda dependencies environment file
print("Creating conda dependencies file locally...")
conda_packages = ['numpy']
pip_packages = ['tensorflow==2.0.0', 'keras==2.3.1', 'azureml-sdk', 'azureml-monitoring']
mycondaenv = CondaDependencies.create(conda_packages=conda_packages, pip_packages=pip_packages)

conda_file = 'scoring_dependencies.yml'
with open(conda_file, 'w') as f:
    f.write(mycondaenv.serialize_to_string())

# create container image configuration
print("Creating container image configuration...")
image_config = ContainerImage.image_configuration(execution_script = 'score_fixed.py', 
                                                  runtime = 'python', conda_file = conda_file)

print("Creating image...")
image = Image.create(name=args.image_name, models=[latest_model], image_config=image_config, workspace=ws)

# wait for image creation to finish
image.wait_for_creation(show_output=True)

eval_info["image_id"] = image.id

with open(eval_filepath, "w") as f:
    json.dump(eval_info, f)
    print('eval_info.json saved')







