from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class SymptomInput(BaseModel):
    symptoms: str

@app.post("/predict")
async def predict_disease(input: SymptomInput):
    # In a real application, load model.pkl and make a prediction
    # For now, return a dummy prediction based on symptoms
    if "fever" in input.symptoms.lower() and "cough" in input.symptoms.lower():
        prediction = "Flu"
    elif "headache" in input.symptoms.lower() and "nausea" in input.symptoms.lower():
        prediction = "Migraine"
    else:
        prediction = "Unknown Disease"
    return {"prediction": prediction}
