from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pickle
import numpy as np


# Initialize FastAPI app
app = FastAPI()

model = None

@app.on_event("startup")
async def load_model():
    global model
    with open("model.pkl", "rb") as model_file:
        model = pickle.load(model_file)
        
# Input data structure
class IrisInput(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

# Home route and
@app.get("/")
async def home(): 
    return {"message": "Welcome to Iris API"}

# Prediction route
@app.post("/predict")
def predict_iris(data: IrisInput):
    features = np.array([[data.sepal_length, data.sepal_width, data.petal_length, data.petal_width]])
    prediction = model.predict(features)
    class_names = ["Setosa", "Versicolor", "Virginica"]
    predicted_class = class_names[prediction[0]]
    return {"prediction": predicted_class}
