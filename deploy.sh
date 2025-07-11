#!/bin/bash

echo "⏳ Deploying to KIND cluster..."

# Apply Kubernetes manifests
kubectl apply -f k8s-deploy.yml

# Wait for deployment
kubectl rollout status deployment/diabetes-api

# Port forward (background)
echo "🔁 Starting port-forward..."
nohup kubectl port-forward svc/diabetes-api-service 1111:80 --address=0.0.0.0 > port-forward.log 2>&1 &

sleep 5

# Test /docs
echo "🔍 Testing FastAPI /docs endpoint..."
curl --fail http://localhost:1111/docs || (echo "❌ API not reachable" && exit 1)

# Auto open in browser (optional)
if which xdg-open > /dev/null; then
  xdg-open http://localhost:1111/docs
elif which start > /dev/null; then
  start http://localhost:1111/docs
else
  echo "🔗 Open in browser: http://localhost:1111/docs"
fi
