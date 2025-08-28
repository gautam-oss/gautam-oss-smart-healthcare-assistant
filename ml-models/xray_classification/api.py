from fastapi import FastAPI, File, UploadFile
from pydantic import BaseModel
import base64
import io
from PIL import Image

app = FastAPI()

class ImageInput(BaseModel):
    image: str # Base64 encoded image

@app.post("/predict")
async def classify_xray(input: ImageInput):
    try:
        # Decode the base64 image
        image_bytes = base64.b64decode(input.image)
        image = Image.open(io.BytesIO(image_bytes))

        # In a real application, load xray_model.h5 and make a prediction
        # For now, return a dummy classification
        # You might want to add more sophisticated dummy logic here
        if image.width > 100 and image.height > 100: # Simple dummy check
            prediction = "Normal Lung"
        else:
            prediction = "Pneumonia Detected"

        return {"prediction": prediction}
    except Exception as e:
        return {"error": f"Error processing image: {e}"}
