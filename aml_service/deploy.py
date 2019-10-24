import argparse
import azureml.core
from azureml.core import Workspace, Experiment, Run
from azureml.core.compute import AksCompute, ComputeTarget
from azureml.core.webservice import Webservice, AksWebservice
from azureml.core import Image
from azureml.core.authentication import AzureCliAuthentication
import json
import os, sys

print("In deploy.py")
print("Azure Python SDK version: ", azureml.core.VERSION)

print('Opening eval_info.json...')
eval_filepath = os.path.join('./outputs', 'eval_info.json')

try:
    with open(eval_filepath) as f:
        eval_info = json.load(f)
        print('eval_info.json loaded')
        print(eval_info)
except:
    print("Cannot open: ", eval_filepath)
    print("Exiting...")
    sys.exit(0)

model_name = eval_info["model_name"]
model_version = eval_info["model_version"]
model_path = eval_info["model_path"]
model_acc = eval_info["model_acc"]
deployed_model_acc = eval_info["deployed_model_acc"]
deploy_model = eval_info["deploy_model"]
image_name = eval_info["image_name"]
image_id = eval_info["image_id"]

if deploy_model == False:
    print('Model metric did not meet the metric threshold criteria and will not be deployed!')
    print('Exiting')
    sys.exit(0)

print('Moving forward with deployment...')

parser = argparse.ArgumentParser("deploy")
parser.add_argument("--service_name", type=str, help="service name", dest="service_name", required=True)
parser.add_argument("--aks_name", type=str, help="aks name", dest="aks_name", required=True)
parser.add_argument("--aks_region", type=str, help="aks region", dest="aks_region", required=True)
parser.add_argument("--description", type=str, help="description", dest="description", required=True)
args = parser.parse_args()

print("Argument 1: %s" % args.service_name)
print("Argument 2: %s" % args.aks_name)
print("Argument 3: %s" % args.aks_region)
print("Argument 4: %s" % args.description)

print('creating AzureCliAuthentication...')
cli_auth = AzureCliAuthentication()
print('done creating AzureCliAuthentication!')

print('get workspace...')
ws = Workspace.from_config(auth=cli_auth)
print('done getting workspace!')

image = Image(ws, id = image_id)
print(image)

aks_name = args.aks_name 
aks_region = args.aks_region
aks_service_name = args.service_name

try:
    service = Webservice(name=aks_service_name, workspace=ws)
    print("Deleting AKS service {}".format(aks_service_name))
    service.delete()
except:
    print("No existing webservice found: ", aks_service_name)

compute_list = ws.compute_targets
aks_target = None
if aks_name in compute_list:
    aks_target = compute_list[aks_name]
    
if aks_target == None:
    print("No AKS found. Creating new Aks: {} and AKS Webservice: {}".format(aks_name, aks_service_name))
    prov_config = AksCompute.provisioning_configuration(location=aks_region)
    # Create the cluster
    aks_target = ComputeTarget.create(workspace=ws, name=aks_name, provisioning_configuration=prov_config)
    aks_target.wait_for_completion(show_output=True)
    print(aks_target.provisioning_state)
    print(aks_target.provisioning_errors)
    
print("Creating new webservice")
# Create the web service configuration (using defaults)
aks_config = AksWebservice.deploy_configuration(description = args.description, 
                                                tags = {'name': aks_name, 'image_id': image.id})
service = Webservice.deploy_from_image(
    workspace=ws,
    name=aks_service_name,
    image=image,
    deployment_config=aks_config,
    deployment_target=aks_target
)
service.wait_for_deployment(show_output=True)
print(service.state)

api_key, _ = service.get_keys()
print("Deployed AKS Webservice: {} \nWebservice Uri: {} \nWebservice API Key: {}".
      format(service.name, service.scoring_uri, api_key))

aks_webservice = {}
aks_webservice["aks_service_name"] = service.name
aks_webservice["aks_service_url"] = service.scoring_uri
aks_webservice["aks_service_api_key"] = api_key
print("AKS Webservice Info")
print(aks_webservice)

print("Saving aks_webservice.json...")
aks_webservice_filepath = os.path.join('./outputs', 'aks_webservice.json')
with open(aks_webservice_filepath, "w") as f:
    json.dump(aks_webservice, f)
print("Done saving aks_webservice.json!")

# Single test data
test_data = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 2, 5, 6, 4, 3, 1, 34]]
# Call the webservice to make predictions on the test data
prediction = service.run(json.dumps(test_data))
print('Test data prediction: ', prediction)

