minikube start --vm-driver=docker
# minikube start

eval $(minikube docker-env)

minikube addons enable metallb
kubectl apply -f ./srcs/metallb.yaml
kubectl apply -f ./srcs/volumePostgres.yaml

#build postgresql
docker build -t postgres-service ./srcs/postgresql
kubectl apply -f ./srcs/postgresql/yaml

sh
