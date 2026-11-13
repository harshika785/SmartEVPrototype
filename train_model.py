from pathlib import Path
import json
import joblib
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data" / "ev_training_data.csv"
MODEL = ROOT / "data" / "ev_range_model.pkl"
METRICS = ROOT / "data" / "ev_model_metrics.json"

if not DATA.exists():
    import generate_data  # creates the synthetic dataset

df = pd.read_csv(DATA)
features = ["soc", "health", "temperature", "efficiency"]
X = df[features]
y = df["range_km"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
model = RandomForestRegressor(
    n_estimators=150, random_state=42, min_samples_leaf=3, n_jobs=-1
)
model.fit(X_train, y_train)
predictions = model.predict(X_test)

metrics = {
    "mae_km": float(mean_absolute_error(y_test, predictions)),
    "r2_score": float(r2_score(y_test, predictions)),
    "training_rows": int(len(X_train)),
    "testing_rows": int(len(X_test)),
    "data_type": "synthetic",
}
joblib.dump(model, MODEL)
METRICS.write_text(json.dumps(metrics, indent=2), encoding="utf-8")

print("Model trained and saved.")
print(f"MAE: {metrics['mae_km']:.2f} km")
print(f"R2: {metrics['r2_score']:.3f}")
