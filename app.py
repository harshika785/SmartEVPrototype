import streamlit as st
from pathlib import Path
from utils.common import apply_theme, initialise_state, render_sidebar_controls

BASE_DIR = Path(__file__).resolve().parent

st.set_page_config(
    page_title="Smart EV Battery Intelligence",
    page_icon="🔋",
    layout="wide",
    initial_sidebar_state="expanded",
)

apply_theme()
initialise_state()

st.sidebar.markdown(
    """
    <div class="brand-block">
        <div class="brand-kicker">SMART MOBILITY</div>
        <div class="brand-title">⚡ EV MONITOR</div>
        <div class="brand-subtitle">Battery Intelligence System</div>
    </div>
    """,
    unsafe_allow_html=True,
)
render_sidebar_controls()

pages = {
    "MONITORING": [
        st.Page("pages/dashboard.py", title="Dashboard", icon=":material/dashboard:", default=True),
        st.Page("pages/battery_intelligence.py", title="Battery Intelligence", icon=":material/battery_charging_full:"),
        st.Page("pages/digital_twin.py", title="Battery Digital Twin", icon=":material/precision_manufacturing:"),
    ],
    "OPTIMIZATION": [
        st.Page("pages/smart_charging.py", title="Smart Charging", icon=":material/bolt:"),
        st.Page("pages/energy_coach.py", title="Energy Saving Coach", icon=":material/eco:"),
        st.Page("pages/ai_prediction.py", title="AI Range Prediction", icon=":material/psychology:"),
    ],
    "RECORDS & SYSTEM": [
        st.Page("pages/prediction_history.py", title="Prediction History", icon=":material/history:"),
        st.Page("pages/model_information.py", title="Model Information", icon=":material/info:"),
    ],
}

pg = st.navigation(pages, position="sidebar")
pg.run()
