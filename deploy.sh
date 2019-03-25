minicube start
eval $(minikube docker-env)
docker build -t=latest .
kubectl create -f deployment.yaml 