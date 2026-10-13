
import pandas as pd
import joblib

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score

# Load the newly generated dataset
df = pd.read_csv("ev_training_data.csv")

features = ["soc", "health", "temperature", "efficiency"]
X = df[features]
y = df["range_km"]

# Keep 20% aside for testing
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
)

# Train the model
model = RandomForestRegressor(
    n_estimators=150,
    random_state=42,
    min_samples_leaf=3,
)

model.fit(X_train, y_train)

# Evaluate on held-out examples
predictions = model.predict(X_test)

mae = mean_absolute_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print("EV Range Prediction Model Retrained!")
print(f"Total examples: {len(df)}")
print(f"Training examples: {len(X_train)}")
print(f"Testing examples: {len(X_test)}")
print(f"Mean Absolute Error (MAE): {mae:.2f} km")
print(f"R² score: {r2:.3f}")

# Save the trained model
joblib.dump(model, "ev_range_model.pkl")

# Save evaluation metrics for the dashboard
joblib.dump(
    {"mae_km": float(mae), "r2_score": float(r2)},
    "ev_model_metrics.pkl",
)

print("\nModel and evaluation metrics saved successfully!")