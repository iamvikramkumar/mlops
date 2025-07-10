# main.py
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# Import necessary libraries
# joblib is used for loading the trained model
# numpy is used for handling numerical data
# FastAPI is used to create the web API
# pydantic is used for data validation and serialization
# Ensure you have the necessary libraries installed:
# pip install fastapi[all] joblib numpy pydantic
# Load the trained model
# Ensure the model is saved as 'diabetes_model.pkl' in the same directory
# You can train and save the model using scikit-learn or any other library
# Example: from sklearn.ensemble import RandomForestClassifier
# model = RandomForestClassifier()
# model.fit(X_train, y_train)
# joblib.dump(model, 'diabetes_model.pkl')  

app = FastAPI()
model = joblib.load("diabetes_model.pkl")

class DiabetesInput(BaseModel):
    Pregnancies: int
    Glucose: float
    BloodPressure: float
    BMI: float
    Age: int

@app.get("/")
def read_root():
    return {"message": "Diabetes Prediction API is live"}

@app.post("/predict")
def predict(data: DiabetesInput):
    input_data = np.array([[data.Pregnancies, data.Glucose, data.BloodPressure, data.BMI, data.Age]])
    prediction = model.predict(input_data)[0]
    return {"diabetic": bool(prediction)}
