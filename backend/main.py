import cv2
import numpy as np
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
app=FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # allow all (for now)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/")
def home():
    return{"message": "Backend is running!"}

@app.get("/predict")
def predict():
    return{"result":"dummy output"}

@app.post("/upload-image")
async def upload_image(file:UploadFile = File(...)):
    filename = file.filename
    content_type = file.content_type
    contents = await file.read()

    #convert to numpy array
    nparr = np.frombuffer(contents, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    #convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    #simple thresholding
    _, thresh = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY)

    #calculate the white area ratio
    white_pixels = np.sum(thresh==255)
    total_pixels = thresh.size
    ratio = white_pixels/total_pixels

    if ratio>0.5:
        result = "Wound Condition: Likely Healing"
        advice = "Keep area clean and monitor progress"
    else:
        result = "Infection Risk: Moderate"
        advice = "Consider cleaning and medical attention"

    return {"result" : result,
            "healing_score": f"{round(ratio*100,2)}%",
            "advice": advice}
