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
    return {"filename": filename, "type": content_type}
