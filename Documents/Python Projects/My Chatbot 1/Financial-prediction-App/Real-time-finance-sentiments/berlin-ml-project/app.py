from fastapi import FastAPI
from transformers import pipeline
from pydantic import BaseModel

app = FastAPI(title="Berlin Finance Sentiment API")
# Load model from Hugging Face
classifier = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

class TextData(BaseModel):
    text: str

@app.post("/predict")
def predict(data: TextData):
    result = classifier(data.text)
    return {"input": data.text, "prediction": result}

@app.get("/health")
def health():
    return {"status": "healthy"}
