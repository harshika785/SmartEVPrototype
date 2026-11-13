from pathlib import Path
import streamlit as st

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
MODEL_PATH = DATA_DIR / "ev_range_model.pkl"
METRICS_PATH = DATA_DIR / "ev_model_metrics.json"
TRAINING_DATA_PATH = DATA_DIR / "ev_training_data.csv"
HISTORY_PATH = DATA_DIR / "prediction_history.csv"

THEME_CSS = """
<style>
:root {
    --ev-bg: #0B1728;
    --ev-panel: #101F33;
    --ev-panel-2: #0B2940;
    --ev-cyan: #00E5FF;
    --ev-green: #39FF88;
    --ev-text: #EAF4FF;
    --ev-muted: #91AEC5;
    --ev-border: #174B65;
}
.stApp { background: var(--ev-bg); color: var(--ev-text); }
[data-testid="stSidebar"] { background: #0D192B; border-right: 1px solid #17344D; }
[data-testid="stSidebar"] > div { padding-top: 1rem; }
.brand-block { padding: 8px 4px 18px 4px; }
.brand-kicker { color: #00E5FF; font-size: 11px; letter-spacing: 2px; font-weight: 800; }
.brand-title { color: #EAF4FF; font-size: 25px; font-weight: 800; margin-top: 5px; }
.brand-subtitle { color: #91AEC5; font-size: 12px; margin-top: 3px; }
h1, h2, h3 { color: #EAF4FF !important; }
p, label, .stMarkdown { color: #D5E6F5; }
div[data-testid="stMetric"] {
    background: linear-gradient(145deg, #101F33, #142D46);
    border: 1px solid #174B65; border-radius: 13px;
    padding: 14px 16px; min-height: 108px;
}
div[data-testid="stMetricLabel"] { color: #A9C8DE; }
div[data-testid="stMetricValue"] { color: #00E5FF; }
div[data-testid="stProgressBar"] > div > div {
    background: linear-gradient(90deg, #00E5FF, #39FF88);
}
div[data-testid="stProgressBar"] { background: #1B3045; }
div[data-testid="stAlert"] { border-radius: 12px; }
div.stButton > button, div.stDownloadButton > button {
    border-radius: 9px; border: 1px solid #00AFC5;
    background: #10364A; color: #EAF4FF;
}
div.stButton > button:hover, div.stDownloadButton > button:hover {
    border-color: #39FF88; color: #39FF88;
}
section[data-testid="stSidebar"] .stRadio label { color: #D5E6F5; }
hr { border-color: #174B65; }
.small-muted { color: #91AEC5; font-size: 12px; }
.status-pill {
    display:inline-block; border:1px solid #27664D; color:#39FF88;
    padding:5px 10px; border-radius:20px; font-size:11px; letter-spacing:.5px;
}
.panel {
    background: linear-gradient(135deg, #101F33, #0B2940);
    border: 1px solid #174B65; border-radius: 14px; padding: 18px;
}
.battery-shell { border: 2px solid #00E5FF; border-radius: 13px; padding: 5px; height: 34px; }
.battery-fill { height: 20px; border-radius: 7px; background: linear-gradient(90deg,#00E5FF,#39FF88); }
</style>
"""

def apply_theme():
    st.markdown(THEME_CSS, unsafe_allow_html=True)

def initialise_state():
    defaults = {
        "soc": 64,
        "health": 87,
        "temperature": 35,
        "efficiency": 7.0,
        "capacity": 40.0,
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value

def render_sidebar_controls():
    st.sidebar.markdown("---")
    st.sidebar.markdown("**LIVE SIMULATION INPUTS**")
    st.sidebar.slider("Battery charge (SoC %)", 0, 100, key="soc")
    st.sidebar.slider("Battery health (SoH %)", 50, 100, key="health")
    st.sidebar.slider("Battery temperature (°C)", 0, 60, key="temperature")
    st.sidebar.slider("Driving efficiency (km/kWh)", 3.0, 10.0, step=0.5, key="efficiency")
    st.sidebar.slider("Usable capacity when new (kWh)", 10.0, 100.0, step=5.0, key="capacity")
    st.sidebar.markdown("---")
    st.sidebar.caption("Educational prototype • Simulated battery values")

def current_values():
    soc = float(st.session_state.soc)
    health = float(st.session_state.health)
    temperature = float(st.session_state.temperature)
    efficiency = float(st.session_state.efficiency)
    capacity = float(st.session_state.capacity)
    energy = capacity * (health / 100) * (soc / 100)
    range_km = energy * efficiency
    return {
        "soc": soc, "health": health, "temperature": temperature,
        "efficiency": efficiency, "capacity": capacity,
        "energy": energy, "range_km": range_km,
    }

def page_header(title, subtitle):
    st.markdown(
        f"""
        <div class="panel" style="margin-bottom:18px;">
          <div style="color:#00E5FF;font-size:11px;letter-spacing:1.8px;font-weight:800;">
            SMART MOBILITY / BATTERY INTELLIGENCE
          </div>
          <div style="font-size:27px;font-weight:800;color:#EAF4FF;margin-top:5px;">{title}</div>
          <div style="color:#91AEC5;font-size:13px;margin-top:5px;">{subtitle}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

def disclaimer():
    st.caption(
        "Educational simulation only. Values are not live vehicle telemetry, "
        "validated battery diagnostics, or guaranteed driving/charging advice."
    )
