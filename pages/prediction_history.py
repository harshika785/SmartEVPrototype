import streamlit as st
import pandas as pd
from utils.common import page_header, HISTORY_PATH, disclaimer

page_header("Prediction History", "Review and export saved range predictions.")

if HISTORY_PATH.exists():
    history = pd.read_csv(HISTORY_PATH)
    if history.empty:
        st.info("No predictions have been saved yet. Open AI Range Prediction and save a result.")
    else:
        st.metric("Saved prediction records", len(history))
        st.dataframe(history.tail(100), use_container_width=True, hide_index=True)
        st.download_button(
            "Download prediction history (CSV)",
            history.to_csv(index=False).encode("utf-8"),
            "prediction_history.csv",
            "text/csv",
        )
else:
    st.info("No prediction history exists yet. Save a prediction from the AI Range Prediction page.")
disclaimer()
