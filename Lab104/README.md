## TFJob

We are going to use our AKS cluster to submit tensorflow jobs.  

It's worth researching TFJob and learning about it on your own.  

But here is what a simple tf training job looks like:

```yaml
apiVersion: kubeflow.org/v1beta1
kind: TFJob
metadata:
  name: example-tfjob
spec:
  tfReplicaSpecs:
    MASTER:
      replicas: 1
      template:
        spec:
          containers:
            - image: <DOCKER_USERNAME>/tf-mnist:gpu
              name: tensorflow
              resources:
                limits:
                  nvidia.com/gpu: 1
          restartPolicy: OnFailure
```

There's a ton more we could say, but won't.  

Let's use our docker container for mnist that we built in Lab101.  

We want to ensure we are using GPUs.

Change tf-mnist.yaml as needed.  

```bash
kubectl create -f Lab104/tf-mnist.yaml 
kubectl get tfjob
kubectl get pod
kubectl logs lab104-gpu-master-0
```

## Persistent Storage

Once the container stops we lose the trained model so we still have some work to do.  We'll use PVC to do this

```bash
# first we need a storage class
kubectl create -f Lab104/az-file-sc.yaml 
# then the PVC
kubectl create -f Lab104/az-file-pvc.yaml 

kubectl get pvc my-azurefile

# now we modify the yaml to include the storage options.  I've done this in a different yaml file that you can compare
kubectl apply -f Lab104/tf-mnist-pvc.yaml 
kubectl get pod
kubectl logs lab104-gpu-master-0
```