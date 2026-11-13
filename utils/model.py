import json
import subprocess
import sys
from pathlib import Path
import joblib
import pandas as pd
from .common import MODEL_PATH, METRICS_PATH, TRAINING_DATA_PATH, ROOT

FEATURES = ["soc", "health", "temperature", "efficiency"]

def ensure_model():
    if not MODEL_PATH.exists() or not METRICS_PATH.exists():
        subprocess.run(
            [sys.executable, str(ROOT / "train_model.py")],
            cwd=str(ROOT),
            check=True,
        )
    model = joblib.load(MODEL_PATH)
    metrics = json.loads(METRICS_PATH.read_text(encoding="utf-8"))
    return model, metrics

def predict_range(soc, health, temperature, efficiency):
    model, metrics = ensure_model()
    row = pd.DataFrame([{
        "soc": float(soc),
        "health": float(health),
        "temperature": float(temperature),
        "efficiency": float(efficiency),
    }], columns=FEATURES)
    prediction = float(model.predict(row)[0])
    return max(0.0, prediction), metrics
