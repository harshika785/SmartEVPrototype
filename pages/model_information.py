import streamlit as st
import json
from utils.common import page_header, METRICS_PATH, TRAINING_DATA_PATH, disclaimer

page_header("Model Information", "Technical notes about the prototype's range-estimation model.")

st.markdown("### Model details")
st.write("- Algorithm: Random Forest Regressor")
st.write("- Inputs: battery charge, battery health, temperature and driving efficiency")
st.write("- Target: simulated estimated driving range in kilometres")
st.write("- Training source: generated synthetic dataset included in the project")

if METRICS_PATH.exists():
    metrics = json.loads(METRICS_PATH.read_text(encoding="utf-8"))
    a, b = st.columns(2)
    a.metric("Mean Absolute Error", f'{metrics.get("mae_km", 0):.2f} km')
    b.metric("R² score", f'{metrics.get("r2_score", 0):.3f}')
else:
    st.info("Model metrics will appear after the first model training run.")

if TRAINING_DATA_PATH.exists():
    st.write(f"Training dataset: `{TRAINING_DATA_PATH.name}`")
    st.write("Rows in training dataset:", sum(1 for _ in TRAINING_DATA_PATH.open(encoding="utf-8")) - 1)

st.warning("Important limitation: the dataset is simulated. Strong test scores on synthetic data do not prove real-world prediction accuracy. Do not describe this model as a validated vehicle battery management system.")
disclaimer()
