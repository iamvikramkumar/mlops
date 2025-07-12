# 🩺 Diabetes Prediction Model – MLOps Project (FastAPI + Docker + K8s)

This beginner-friendly project walks you through building and deploying a machine learning model for diabetes prediction. You’ll learn how to:

- ✅ Train a model using Random Forest
- ✅ Serve it with FastAPI
- ✅ Dockerize the application
- ✅ Deploy it on Kubernetes (with Kind)
- ✅ Understand CI/CD and monitoring steps for future improvements

---

## 📊 Problem Statement

Predict if a person is diabetic based on:

- Pregnancies
- Glucose
- Blood Pressure
- BMI
- Age

Model used: **Random Forest Classifier**  
Dataset: **Pima Indians Diabetes Dataset**

---

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/iam-veeramalla/first-mlops-project.git
cd first-mlops-project
```

---

## 💻 Setup and Model Training

### 2. Create a Virtual Environment

> 🔹 **Windows (CMD)**

```cmd
python -m venv .mlops
.mlops\Scripts\activate
```

> 🔹 **Windows (PowerShell)**

```powershell
python -m venv .mlops
.\.mlops\Scripts\Activate.ps1
```

> 🔹 **macOS/Linux**

```bash
python3 -m venv .mlops
source .mlops/bin/activate
```

> 🔹 **Windows with Git Bash**

```bash
python -m venv .mlops
source .mlops/Scripts/activate
```

### 3. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 4. Train the Model

```bash
python train.py
```

➡️ This will generate a `model.pkl` file used for predictions.

---

## 🌐 Run FastAPI Locally

### 5. Start FastAPI Server

```bash
uvicorn main:app --reload
```

Open your browser: [http://localhost:8000/docs](http://localhost:8000/docs)

### 6. Sample Input for `/predict` endpoint

```json
{
  "Pregnancies": 2,
  "Glucose": 130,
  "BloodPressure": 70,
  "BMI": 28.5,
  "Age": 45
}
```

---

## 🐳 Dockerize the API

### 7. Build Docker Image

```bash
docker build -t diabetes-prediction-model .
```

### 8. Run the Docker Container

```bash
docker run -p 8000:8000 diabetes-prediction-model
```

### 9. Tag Docker Image

```bash
docker tag <image-id> iamvikramkumar/diabetes-prediction-model:v1
```

(Find `<image-id>` using `docker images`)

### 10. Push to Docker Hub

```bash
docker login
docker push iamvikramkumar/diabetes-prediction-model:v1
```

---

## ☸️ Deploy on Kubernetes (Using Kind)

> 📝 **Note:** Please install [Docker Desktop](https://docs.docker.com/get-started/get-docker/), [Kubectl](https://kubernetes.io/docs/tasks/tools/), and [Kind](https://kind.sigs.k8s.io/) before proceeding.

### 11. Create a Kind Cluster

```bash
kind create cluster --name demo-mlops
```

### 12. Check Cluster Status

```bash
kubectl config current-context
kubectl get nodes
```

### 13. Apply Kubernetes Manifest

```bash
kubectl apply -f deploy.yaml
```

### 14. Monitor Kubernetes Resources

```bash
kubectl get pods -w
kubectl get svc
```

### 15. Port Forward to Access API

```bash
kubectl port-forward svc/diabetes-api-service 1111:80 --address=0.0.0.0
```

🔗 Open: [http://localhost:1111/docs](http://localhost:1111/docs)

---

## 🔄 Future Scope: CI/CD and Monitoring

### 🧪 CI/CD (GitHub Actions, Not Implemented Yet)

- Auto test and validate model updates
- Build Docker images
- Push to Docker Hub
- Deploy to Kubernetes

### 📈 Monitoring (Not Implemented Yet)

- Prometheus + Grafana for API performance
- Evidently AI or WhyLogs for data drift and prediction accuracy
- Alerts for latency or failure spikes

---

🙌 Credits

Created by `ABHISHEK VEERAMALLA`

Subscribe for more DevOps + MLOps content on the YouTube Channel - `Abhishek.Veeramalla`
