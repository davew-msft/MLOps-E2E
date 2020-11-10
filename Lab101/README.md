## Containerizing a TF Model

In this lab we want to containerize a TF model that we will improve upon in subsequent labs.  This is an MNIST classifier.  Source code is `./src/main.py`.  This file can be run, if desired on your laptop now.  You may need to install pip packages. 

If we run this with Docker directly we actually shouldn't need to install pip packages since those are declared in the dockerfile.  See `./src/Dockerfile`.

Here we are using the base tf image from their [docker hub](https://hub.docker.com/r/tensorflow/tensorflow/tags/).  Different tags are needed depending on if we have GPUs available or not.  And note we also have a `Dockerfile.gpu` if you have gpus available.  

The Dockerfile is also copying our main.py into the container and then setting the entry point script for the container.  

Let's build the image.  I use WSL2 and Docker Desktop for Windows, you may need to adjust the instructions for your use case.  

```bash
#change this to your docker hub username, we will push to docker hub later.  If you'd rather use ACR, feel free to adjust the instructions accordingly
DOCKER_USERNAME=dwentzel
cd src
docker build -t ${DOCKER_USERNAME}/tf-mnist .

# check your image is available locally
docker images|grep tf

# now run it, we decrease the training steps to 100 so it only takes a few mins on our machine
docker run -it ${DOCKER_USERNAME}/tf-mnist --max_steps 100

# with any luck your accuracy should be above 90%

# But this will create a CPU optimized docker container.  We want a GPU optimized container.  We can do this even if your laptop doesn't have a GPU to test with.
# Notice we are using the `Dockerfile.gpu` this time

docker build -t ${DOCKER_USERNAME}/tf-mnist:gpu -f Dockerfile.gpu .
# we won't be able to test this image without installing nvidia-docker, which you can research on your own.  Note that gpu-based docker containers will only work on Linux or WSL, hence why we aren't testing locally.  We'll instead test in Azure later.  

# publish both images
docker login
docker push ${DOCKER_USERNAME}/tf-mnist
docker push ${DOCKER_USERNAME}/tf-mnist:gpu
```

## Run our MNIST model on AKS

We need to use the YAML template provided.  Note that:
* the deployment is a Job because we want it to complete and not restart
* it should run the image that YOU created, not mine (although you can use that if you want to)
* We call the job `mnist-training-v1`.  We'll modify it in the next few labs
* we want 500 steps
* it should use the GPU

```bash
# deploy it
kubectl apply -f mnist-training.yaml
#kubectl delete pod mnist-training-v1-6fl7k
kubectl get job
kubectl get pods
# this may take awhile
kubectl logs mnist-training-v1-qdj9t
```

At this point the training doesn't do anything valuable.  We aren't saving the model or metrics anywhere, we'll do that next.  

But first, let's get helm working locally, if needed.

```bash
# make sure everything is working locally
helm repo add stable https://charts.helm.sh/stable
helm install stable/wordpress --generate-name
# we won't use this helm chart, we just want to make sure helm is working
helm delete wordpress-1604957819

# now you can create your own chart using
helm create mnist-gpu
# note that this creates a folder which includes all of the files necessary to create your own package.  
```

