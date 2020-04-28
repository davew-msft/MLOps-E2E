import argparse
import azureml.core
from azureml.core import Workspace, Experiment, Run, Datastore
from azureml.data.azure_storage_datastore import AzureBlobDatastore
from azureml.core.compute import AmlCompute
from azureml.core.compute import ComputeTarget
from azureml.core.runconfig import RunConfiguration
from azureml.core.conda_dependencies import CondaDependencies
from azureml.core.runconfig import DEFAULT_CPU_IMAGE
from azureml.data.data_reference import DataReference
from azureml.pipeline.core import Pipeline, PipelineData
from azureml.pipeline.steps import PythonScriptStep
from azureml.core.authentication import AzureCliAuthentication

print("In piplines_master.py")
print("Pipeline SDK-specific imports completed")
# Check core SDK version number
print("Azure ML SDK version:", azureml.core.VERSION)

parser = argparse.ArgumentParser("pipelines_master")
parser.add_argument("--aml_compute_target", type=str, help="compute target name", dest="aml_compute_target", required=True)
parser.add_argument("--model_name", type=str, help="model name", dest="model_name", required=True)
parser.add_argument("--build_number", type=str, help="build number", dest="build_number", required=True)
parser.add_argument("--image_name", type=str, help="image name", dest="image_name", required=True)
parser.add_argument("--path", type=str, help="path", dest="path", required=True)
args = parser.parse_args()

print("Argument 1: %s" % args.aml_compute_target)
print("Argument 2: %s" % args.model_name)
print("Argument 3: %s" % args.build_number)
print("Argument 4: %s" % args.image_name)
print("Argument 5: %s" % args.path)

print('creating AzureCliAuthentication...')
cli_auth = AzureCliAuthentication()
print('done creating AzureCliAuthentication!')

print('get workspace...')
ws = Workspace.from_config(path=args.path, auth=cli_auth)
print('done getting workspace!')

print("looking for existing compute target.")
aml_compute = AmlCompute(ws, args.aml_compute_target)
print("found existing compute target.")

# Create a new runconfig object
run_amlcompute = RunConfiguration()

# Use the cpu_cluster you created above. 
run_amlcompute.target = args.aml_compute_target

# Enable Docker
run_amlcompute.environment.docker.enabled = True

# Set Docker base image to the default CPU-based image
run_amlcompute.environment.docker.base_image = DEFAULT_CPU_IMAGE

# Use conda_dependencies.yml to create a conda environment in the Docker image for execution
run_amlcompute.environment.python.user_managed_dependencies = False

# Auto-prepare the Docker image when used for execution (if it is not already prepared)
run_amlcompute.auto_prepare_environment = True

# Specify CondaDependencies obj, add necessary packages
run_amlcompute.environment.python.conda_dependencies = CondaDependencies.create(pip_packages=[
    'numpy',
    'pandas',
    'tensorflow==2.0.0',
    'keras==2.3.1',
    'azureml-sdk',
    'azureml-dataprep[pandas]'
])

scripts_folder = 'scripts'
def_blob_store = ws.get_default_datastore()

train_output = PipelineData('train_output', datastore=def_blob_store)
print("train_output PipelineData object created")

trainStep = PythonScriptStep(
    name="train",
    script_name="train.py", 
    arguments=["--model_name", args.model_name,
              "--build_number", args.build_number],
    compute_target=aml_compute,
    runconfig=run_amlcompute,
    source_directory=scripts_folder,
    allow_reuse=False
)
print("trainStep created")

evaluate_output = PipelineData('evaluate_output', datastore=def_blob_store)

evaluateStep = PythonScriptStep(
    name="evaluate",
    script_name="evaluate.py", 
    arguments=["--model_name", args.model_name,  
               "--image_name", args.image_name, 
               "--output", evaluate_output],
    outputs=[evaluate_output],
    compute_target=aml_compute,
    runconfig=run_amlcompute,
    source_directory=scripts_folder,
    allow_reuse=False
)
print("evaluateStep created")

evaluateStep.run_after(trainStep)
steps = [evaluateStep]

pipeline = Pipeline(workspace=ws, steps=steps)
print ("Pipeline is built")

pipeline.validate()
print("Simple validation complete")

run = Run.get_context()
experiment_name = run.experiment.name

pipeline_run = Experiment(ws, experiment_name).submit(pipeline)
print("Pipeline is submitted for execution")

pipeline_run.wait_for_completion(show_output=True, timeout_seconds=43200)

print("Downloading evaluation results...")
# access the evaluate_output
data = pipeline_run.find_step_run('evaluate')[0].get_output_data('evaluate_output')
# download the predictions to local path
data.download('.', show_progress=True)

import json
# load the eval info json
with open(os.path.join('./', data.path_on_datastore, 'eval_info.json')) as f:
    eval_info = json.load(f)
print("Printing evaluation results...")
print(eval_info)

print("Saving evaluation results for release pipeline...")
output_dir = os.path.join(args.path, 'outputs')
os.makedirs(output_dir, exist_ok=True)
filepath = os.path.join(output_dir, 'eval_info.json')

with open(filepath, "w") as f:
    json.dump(eval_info, f)
    print('eval_info.json saved!')
