from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()

class SymptomRequest(BaseModel):
    symptoms: str

@app.post("/predict")
async def predict_disease(request: SymptomRequest):
    # In a real application, load your model (e.g., model.pkl) here
    # and use it to predict based on symptoms.
    # For now, a dummy prediction
    if "fever" in request.symptoms.lower() and "cough" in request.symptoms.lower():
        prediction = "Flu"
    elif "headache" in request.symptoms.lower() and "nausea" in request.symptoms.lower():
        prediction = "Migraine"
    else:
        prediction = "Common Cold"

    return {"prediction": prediction, "confidence": 0.85}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)