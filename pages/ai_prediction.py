import streamlit as st
import pandas as pd
from utils.common import page_header, current_values, disclaimer, HISTORY_PATH, DATA_DIR
from utils.model import predict_range
from datetime import datetime

v = current_values()
page_header("AI Range Prediction", "Use your trained Random Forest model to estimate range from the current simulated battery inputs.")

try:
    prediction, metrics = predict_range(v["soc"], v["health"], v["temperature"], v["efficiency"])
    a, b, c = st.columns(3)
    a.metric("ML estimated range", f"{prediction:.1f} km")
    b.metric("Model test MAE", f'{metrics.get("mae_km", float("nan")):.2f} km')
    c.metric("Model test R²", f'{metrics.get("r2_score", float("nan")):.3f}')
    st.markdown("### Current prediction inputs")
    inputs = pd.DataFrame([{
        "Battery charge (%)": v["soc"],
        "Battery health (%)": v["health"],
        "Temperature (°C)": v["temperature"],
        "Efficiency (km/kWh)": v["efficiency"],
    }])
    st.dataframe(inputs, use_container_width=True, hide_index=True)

    if st.button("Save this prediction", type="primary"):
        row = pd.DataFrame([{
            "Timestamp": datetime.now().isoformat(timespec="seconds"),
            "Battery Charge (%)": v["soc"],
            "Battery Health (%)": v["health"],
            "Temperature (°C)": v["temperature"],
            "Efficiency (km/kWh)": v["efficiency"],
            "Formula Range (km)": round(v["range_km"], 1),
            "ML Range (km)": round(prediction, 1),
        }])
        DATA_DIR.mkdir(exist_ok=True)
        if HISTORY_PATH.exists():
            row.to_csv(HISTORY_PATH, mode="a", header=False, index=False)
        else:
            row.to_csv(HISTORY_PATH, index=False)
        st.success("Prediction saved.")
except Exception as exc:
    st.error(f"The prediction model could not be loaded: {exc}")
    st.info("Run `python train_model.py` in the project folder, then refresh the page.")

st.caption("The model is trained on simulated data. Its reported test metrics measure performance on a synthetic holdout set and should not be interpreted as real-world EV accuracy.")
disclaimer()
