import joblib
import pandas as pd
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from schemas import HousingInput, IrisInput, SentimentInput

app = FastAPI(title="ML Model Serving API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

try:
    reg_model = joblib.load("models/regression.joblib")
    cls_model = joblib.load("models/classification.joblib")
    sentiment_model = joblib.load("models/sentiment.joblib")
except Exception as e:
    print(f"Error loading models: {e}. Please run python train.py first.")

@app.post("/predict/housing")
def predict_housing(data: HousingInput):
    df = pd.DataFrame([data.model_dump()])
    prediction = reg_model.predict(df)[0]
    return {"formatted_price": f"${prediction * 100000:,.2f}"}

@app.post("/predict/iris")
def predict_iris(data: IrisInput, threshold: float = 0.5):
    df = pd.DataFrame([{
        'sepal length (cm)': data.sepal_length,
        'sepal width (cm)': data.sepal_width,
        'petal length (cm)': data.petal_length,
        'petal width (cm)': data.petal_width
    }])
    proba = cls_model.predict_proba(df)[0][1]
    is_virginica = bool(proba >= threshold)
    return {
        "predicted_species": "Virginica" if is_virginica else "Non-Virginica",
        "probability": float(proba)
    }

@app.post("/predict/sentiment")
def predict_sentiment(data: SentimentInput):
    pred = sentiment_model.predict([data.text])[0]
    proba = sentiment_model.predict_proba([data.text])[0][1]
    return {
        "sentiment": "Positive" if pred == 1 else "Negative",
        "confidence": float(proba if pred == 1 else 1 - proba)
    }