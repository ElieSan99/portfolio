from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import pandas as pd
from pathlib import Path
import os

app = FastAPI(
    title="Fraud Detection API",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Configuration des chemins
BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "models" / "model.joblib"
SCALER_PATH = BASE_DIR / "models" / "scaler.joblib"

# Chargement du modèle et du scaler
if MODEL_PATH.exists() and SCALER_PATH.exists():
    model = joblib.load(MODEL_PATH)
    scaler = joblib.load(SCALER_PATH)
else:
    model = None
    scaler = None

class Transaction(BaseModel):
    Time: float
    V1: float
    V2: float
    V3: float
    V4: float
    V5: float
    V6: float
    V7: float
    V8: float
    V9: float
    V10: float
    V11: float
    V12: float
    V13: float
    V14: float
    V15: float
    V16: float
    V17: float
    V18: float
    V19: float
    V20: float
    V21: float
    V22: float
    V23: float
    V24: float
    V25: float
    V26: float
    V27: float
    V28: float
    Amount: float

@app.get("/")
def read_root():
    return {"status": "online", "model_loaded": model is not None}

@app.post("/predict")
def predict(transaction: Transaction):
    if model is None or scaler is None:
        raise HTTPException(status_code=503, detail="Model or Scaler not loaded")
    
    # Conversion en DataFrame
    data = pd.DataFrame([transaction.model_dump()])
    
    # Preprocessing (Scaling)
    data_scaled = scaler.transform(data)
    
    # Prédiction
    prediction = model.predict(data_scaled)
    probability = model.predict_proba(data_scaled)[:, 1]
    
    return {
        "is_fraud": int(prediction[0]),
        "probability": float(probability[0])
    }
