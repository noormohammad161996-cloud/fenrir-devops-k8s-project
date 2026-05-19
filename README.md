# 🚀 Fenrir Kubernetes App (Flask + Docker + Kubernetes)

## 📌 Overview

This project demonstrates an **end-to-end Kubernetes workflow** by deploying a Flask-based application inside a Kubernetes cluster using Minikube.

It includes:

* Application development (Flask)
* Containerization (Docker)
* Deployment (Kubernetes)
* Service exposure (NodePort & Port Forward)
* Environment variable handling

---

## 🧱 Architecture

```
User (Browser)
     ↓
Kubernetes Service
     ↓
Pods (Flask App Containers)
     ↓
Docker Image (Fenrir App)
```

---

## 📂 Project Structure

```bash
fenrir/
│
├── Backend/
├── Frontend/
├── k8s/
│   ├── mongo.yaml
│   ├── mongo-express.yaml
│   ├── backend.yaml
│   └── frontend.yaml
│
├── README.md

---

## ⚙️ Technologies Used

* Python (Flask)
* Docker
* Kubernetes
* Minikube
* kubectl

---

## 🐍 Application Details

The app:

* Displays environment variables
* Runs on configurable PORT
* Uses Jinja2 templating

---

## 📦 Docker Commands Used

### Build Docker Image

```
docker build -t fenrir-app .
```

### Run Container

```
docker run -p 8000:8000 fenrir-app
```

### Tag Image

```
docker tag fenrir-app noormohammad07/fenrir:v1
```

### Push to Docker Hub

```
docker push noormohammad07/fenrir:v1
```

---

## ☸️ Kubernetes Setup

### Start Minikube

```
minikube start
```

### Create Namespace

```
kubectl create namespace fenrir
```

---

## 🚀 Deployment

### Apply Deployment

```
kubectl apply -f k8s/deployment.yaml
```

### Check Pods

```
kubectl get pods -n fenrir
```

### Describe Pod (Debugging)

```
kubectl describe pod <pod-name> -n fenrir
```

---

## 🌐 Service (Expose Application)

### Apply Service

```
kubectl apply -f k8s/service.yaml
```

### Check Service

```
kubectl get svc -n fenrir
```

---

## 🔗 Access Application

### Method 1: Port Forward (Recommended)

```
kubectl port-forward svc/fenrir-service 8000:8000 -n fenrir
```

👉 Open in browser:

```
http://127.0.0.1:8000
```

---

### Method 2: Minikube Service

```
minikube service fenrir-service -n fenrir --url
```

👉 Example URL:

```
http://127.0.0.1:XXXXX
```

---

### Method 3: NodePort (Optional)

```
minikube ip
```

👉 Example:

```
http://192.168.49.2:<NodePort>
```

---

## 📊 Kubernetes Dashboard

### Open Dashboard

```
minikube dashboard --url
```

👉 Example:

```
http://127.0.0.1:XXXXX/api/v1/namespaces/kubernetes-dashboard/services/http:kubernetes-dashboard:/proxy/
```

---

## 🔍 Important Commands Used

### Cluster Info

```
kubectl get nodes
```

### Get All Resources

```
kubectl get all -n fenrir
```

### Logs

```
kubectl logs <pod-name> -n fenrir
```

### Delete Resources

```
kubectl delete deployment fenrir -n fenrir
kubectl delete service fenrir-service -n fenrir
```

---

## 🌱 Environment Variables

Defined in Deployment:

```
env:
  - name: PORT
    value: "8000"
```

Automatically injected by Kubernetes:

* KUBERNETES_SERVICE_HOST
* KUBERNETES_SERVICE_PORT
* HOSTNAME

---

## 🐞 Issues Faced & Fixes

### ❌ TemplateNotFound

✔ Fixed by using `templates/` folder

### ❌ Docker build failed

✔ Missing `requirements.txt`

### ❌ Service not accessible

✔ Used port-forward / NodePort

### ❌ WSL browser issue

✔ Used `explorer.exe` or manual URL

### ❌ NodePort already allocated

✔ Removed nodePort or changed port

### ❌ Folder corruption (/mnt/g)

✔ Moved project to Linux home (`~/`)

---

## 🎯 Key Learnings

* Kubernetes Deployment & Service concepts
* Difference between ClusterIP, NodePort, Port-forward
* Docker image creation & pushing
* Debugging real DevOps issues
* Environment variable usage in Kubernetes

---

## 🚀 Future Improvements

* Add Ingress (custom domain)
* Add CI/CD pipeline (GitHub Actions)
* Deploy on AWS EKS
* Add database (MongoDB/PostgreSQL)


# Fenrir Kubernetes App==============================================================

End-to-end Flask + Docker + Kubernetes project using Minikube and MongoDB.

## 🚀 Tech Stack

- Python Flask
- Docker
- Kubernetes
- Minikube
- MongoDB
- Mongo Express

---

## 📚 What I Practiced

### Docker
- Created Dockerfiles
- Built Docker images
- Managed containers
- Used Docker Desktop with WSL

### Kubernetes
- Deployments
- Services
- NodePort
- ClusterIP
- Pods
- kubectl commands
- Logs debugging
- Minikube service
- Image loading into Minikube

### MongoDB
- MongoDB container deployment
- Mongo Express setup
- Flask to MongoDB connection

### DevOps Skills
- Troubleshooting containers
- Debugging pod logs
- Kubernetes networking
- Restarting deployments
- Service exposure
- Local Kubernetes development

⚙️ Docker Commands

Build backend image:

docker build -t fenrir-backend ./Backend

Build frontend image:

docker build -t fenrir-frontend ./Frontend

Load images into Minikube:

minikube image load fenrir-backend
minikube image load fenrir-frontend

☸️ Kubernetes Commands

Start Minikube:

minikube start --driver=docker

Apply manifests:

kubectl apply -f mongo.yaml
kubectl apply -f mongo-express.yaml
kubectl apply -f backend.yaml
kubectl apply -f frontend.yaml

Check pods:

kubectl get pods

Check services:

kubectl get svc

View logs:

kubectl logs -l app=fenrir-backend

Open frontend service:

minikube service fenrir-frontend
🧠 Key Learnings
How Kubernetes services communicate internally
Difference between localhost and service names in Kubernetes
Debugging container networking issues
Managing Docker images inside Minikube
Using MongoDB inside Kubernetes cluster

---

## 👨‍💻 Author

**Noor Mohammad**

GitHub:
https://github.com/noormohammad161996-cloud

---

## ⭐ If you like this project

Give it a ⭐ on GitHub!
