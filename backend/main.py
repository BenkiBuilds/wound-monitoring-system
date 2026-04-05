from fastapi import FastAPI
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