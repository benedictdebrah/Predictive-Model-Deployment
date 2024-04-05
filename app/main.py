from fastapi import FastAPI
from models import Item
import joblib
import pandas as pd

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Welcome to the Wine Quality Prediction API" }




@app.post("/predict/")
async def predict(item: Item):
    model = joblib.load("src/predictive_model.pkl")
    
    input_data = pd.DataFrame([item.dict()])
    
    prediction = model.predict(input_data)
    
    prediction_result = prediction[0]
    
    return {"prediction": prediction_result}
    
  
