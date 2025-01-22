from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np

# Load the trained model
with open("model.pkl", "rb") as model_file:
    model = pickle.load(model_file)

# Initialize FastAPI app
app = FastAPI()

# Input data structure
class IrisInput(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

# Home route ddsdsd
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
