
import streamlit as st

import plotly.express as px
st.set_page_config(
    page_title="Smart EV Battery Monitor",
    page_icon="🔋",
    layout="wide"
)

# Sidebar navigation
st.sidebar.markdown(
    """
    <div style="padding: 8px 0 20px 0;">
        <div style="font-size: 12px; color: #00E5FF;
                    letter-spacing: 2px; font-weight: bold;">
            SMART MOBILITY
        </div>
        <h2 style="color: #EAF4FF; margin: 8px 0;">
            ⚡ EV Monitor
        </h2>
        <p style="color: #91AEC5; font-size: 12px;">
            Battery Intelligence System
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

page = st.sidebar.radio(
    "NAVIGATION",
    [
        "Dashboard",
        "Driving Simulator",
        "Scenario Comparison",
        "ML Predictions",
        "Prediction History",
        "Model Performance",
    ],
)
st.sidebar.markdown("---")
st.sidebar.caption("Smart EV Monitor • Educational Prototype")



st.markdown("""
<div style="
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 12px 18px;
    margin-bottom: 18px;
    background: #101F33;
    border: 1px solid #174B65;
    border-radius: 12px;
">
    <div>
        <div style="
            color: #00E5FF;
            font-size: 11px;
            letter-spacing: 2px;
            font-weight: bold;
        ">SMART MOBILITY / BATTERY INTELLIGENCE</div>
        <h2 style="
            color: #EAF4FF;
            margin: 5px 0 0 0;
        ">⚡ EV Battery Dashboard</h2>
    </div>
    <div style="
        color: #39FF88;
        border: 1px solid #27664D;
        border-radius: 20px;
        padding: 7px 12px;
        font-size: 12px;
        white-space: nowrap;
    ">● PROTOTYPE</div>
</div>
""", unsafe_allow_html=True)



st.markdown("""
<div style="
    background: linear-gradient(135deg, #101F33, #0B2940);
    border: 1px solid #00E5FF;
    border-radius: 14px;
    padding: 24px;
    margin: 10px 0 20px 0;
">
    <h3 style="color: #00E5FF; margin-top: 0;">
        ◈ PROJECT OVERVIEW
    </h3>
    <p style="color: #EAF4FF;">
        An interactive prototype for monitoring electric vehicle
        battery conditions and estimating remaining driving range.
    </p>
    <h4 style="color: #00E5FF;">Key Features</h4>
    <ul style="color: #D5E6F5; line-height: 1.9;">
        <li>Battery charge, health, and temperature monitoring</li>
        <li>Estimated remaining energy and driving range</li>
        <li>Driving scenario simulation and risk alerts</li>
        <li>Formula-based versus machine-learning predictions</li>
        <li>Model evaluation and prediction history</li>
        <li>Downloadable reports</li>
    </ul>
    <p style="color: #91AEC5; font-size: 13px;">
        TECHNOLOGY: Python · Streamlit · Pandas · NumPy · Scikit-learn
    </p>
</div>
""", unsafe_allow_html=True)


st.info(
    "This is an educational prototype using simulated data. "
    "It is not connected to a real EV battery management system, "
    "and its predictions are not validated for real-world driving."
)
st.write(
    "An interactive software prototype for monitoring "
    "battery condition and estimating remaining driving range."
)

st.sidebar.header("Battery Simulation Controls")

soc = st.sidebar.slider(
    "Battery charge (SoC %)", 0, 100, 64
)

health = st.sidebar.slider(
    "Battery health (%)", 50, 100, 87
)

temperature = st.sidebar.slider(
    "Battery temperature (°C)", 0, 60, 35
)

driving_efficiency = st.sidebar.slider(
    "Driving efficiency (km per kWh)", 3.0, 10.0, 7.0, 0.5
)

battery_capacity = st.sidebar.slider(
    "Usable battery capacity when new (kWh)",
    10, 100, 40
)

# Illustrative estimate for this software prototype
remaining_energy = battery_capacity * (health / 100) * (soc / 100)
estimated_range = remaining_energy * driving_efficiency

# Simple demonstration rule, not a validated battery diagnostic
if temperature >= 45:
    stress = "HIGH"
    recommendation = "Reduce battery load and investigate cooling."
elif temperature >= 35:
    stress = "MODERATE"
    recommendation = "Monitor temperature during driving."
else:
    stress = "LOW"
    recommendation = "Temperature is within this demo's low-stress range."



st.markdown("""
<style>
div[data-testid="stMetric"] {
    background: linear-gradient(145deg, #101F33, #142D46);
    border: 1px solid #174B65;
    border-radius: 12px;
    padding: 12px 14px;
    min-height: 105px;
}
div[data-testid="stMetricLabel"] {
    color: #A9C8DE;
    font-size: 12px;
}
div[data-testid="stMetricValue"] {
    color: #00E5FF;
    font-size: 25px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("### 🔋 Battery Overview")

m1, m2, m3, m4 = st.columns(4, gap="small")

m1.metric("Battery Health", f"{health}%")
m2.metric("State of Charge", f"{soc}%")
m3.metric("Remaining Range", f"{estimated_range:.1f} km")
m4.metric("Temperature", f"{temperature} °C")

st.progress(
    soc / 100,
    text=f"Battery charge level: {soc}%"
)

with st.expander("View additional battery details"):
    st.metric("Estimated Remaining Energy", f"{remaining_energy:.1f} kWh")


col1, col2, col3 = st.columns(3, gap="medium")

col1.metric("🔋 Battery Health", f"{health}%")
col2.metric("⚡ State of Charge", f"{soc}%")
col3.metric("🌡️ Temperature", f"{temperature} °C")

col4, col5 = st.columns(2, gap="medium")

col4.metric(
    "🛣️ Estimated Remaining Range",
    f"{estimated_range:.1f} km"
)
col5.metric(
    "🔌 Estimated Remaining Energy",
    f"{remaining_energy:.1f} kWh"
)


st.subheader("Battery Status")


st.markdown("""
<style>
div[data-testid="stProgressBar"] > div > div {
    background: linear-gradient(90deg, #00E5FF, #39FF88);
    border-radius: 20px;
}
div[data-testid="stProgressBar"] {
    background-color: #1B3045;
    border-radius: 20px;
}
</style>
""", unsafe_allow_html=True)

st.progress(
    soc / 100,
    text=f"⚡ Battery charge level: {soc}%"
)


if stress == "HIGH":
    st.error(f"Battery stress: {stress}")
elif stress == "MODERATE":
    st.warning(f"Battery stress: {stress}")
else:
    st.success(f"Battery stress: {stress}")

st.info(recommendation)

st.caption(
    "Student prototype: values are simulated. Range and stress are "
    "illustrative estimates, not validated predictions or safety advice."
)


st.divider()


st.markdown("""
<div style="
    background: linear-gradient(135deg, #101F33, #0B2940);
    border: 1px solid #174B65;
    border-left: 4px solid #00E5FF;
    border-radius: 14px;
    padding: 20px;
    margin: 18px 0;
">
    <h3 style="color: #00E5FF; margin: 0 0 8px 0;">
        🧪 Driving Scenario Simulator
    </h3>
    <p style="color: #B8D5E8; margin: 0;">
        Explore how weather, battery charge, and battery health
        affect your estimated driving range.
    </p>
</div>
""", unsafe_allow_html=True)


scenario = st.selectbox(
    "Select a driving scenario",
    [
        "Normal City Driving",
        "Hot Weather",
        "Low Battery",
        "Degraded Battery",
    ],
)

scenarios = {
    "Normal City Driving": {
        "soc": 64,
        "health": 87,
        "temperature": 30,
        "efficiency": 7.0,
    },
    "Hot Weather": {
        "soc": 64,
        "health": 87,
        "temperature": 50,
        "efficiency": 5.5,
    },
    "Low Battery": {
        "soc": 15,
        "health": 87,
        "temperature": 30,
        "efficiency": 7.0,
    },
    "Degraded Battery": {
        "soc": 64,
        "health": 65,
        "temperature": 30,
        "efficiency": 7.0,
    },
}

selected = scenarios[scenario]

scenario_energy = (
    battery_capacity
    * (selected["health"] / 100)
    * (selected["soc"] / 100)
)

scenario_range = scenario_energy * selected["efficiency"]

st.write(f"**Scenario:** {scenario}")

left, right = st.columns(2)

left.metric(
    "Scenario Estimated Range",
    f"{scenario_range:.1f} km",
)

right.metric(
    "Scenario Remaining Energy",
    f"{scenario_energy:.1f} kWh",
)

st.caption(
    "These scenarios use illustrative inputs and a simplified formula. "
    "They are not validated predictions of real vehicle performance."
)

st.divider()
st.subheader("🛡️ Battery Risk Indicator")


# Simple demonstration rules, not a validated diagnostic
if (
    selected["temperature"] >= 45
    or selected["health"] < 70
):
    risk_level = "HIGH"
    risk_message = (
        "The simulated temperature or battery health "
        "has crossed this prototype's high-risk threshold. "
        "Check manufacturer guidance."
    )
elif selected["soc"] <= 20:
    risk_level = "MODERATE"
    risk_message = (
        "The simulated battery charge is low. "
        "Consider planning a charging stop."
    )
else:
    risk_level = "LOW"
    risk_message = (
        "No elevated risk is flagged by this prototype's "
        "simple demonstration rules."
    )

if risk_level == "HIGH":
    st.error(f"Risk Level: {risk_level}")
elif risk_level == "MODERATE":
    st.warning(f"Risk Level: {risk_level}")
else:
    st.success(f"Risk Level: {risk_level}")

st.write(risk_message)

# Compare all driving scenarios
st.divider()

st.markdown("""
<div style="
    background: linear-gradient(135deg, #101F33, #0B2940);
    border: 1px solid #174B65;
    border-left: 4px solid #39FF88;
    border-radius: 14px;
    padding: 20px;
    margin: 18px 0;
">
    <h3 style="color: #39FF88; margin: 0 0 8px 0;">
        📊 Scenario Comparison Dashboard
    </h3>
    <p style="color: #B8D5E8; margin: 0;">
        Compare estimated range, battery charge, battery health,
        and temperature across different driving conditions.
    </p>
</div>
""", unsafe_allow_html=True)


scenario_names = list(scenarios.keys())

comparison_data = []

for name in scenario_names:
    data = scenarios[name]

    energy = (
        battery_capacity
        * (data["health"] / 100)
        * (data["soc"] / 100)
    )

    distance = energy * data["efficiency"]

    comparison_data.append({
        "Scenario": name,
        "Estimated Range (km)": round(distance, 1),
        "Battery Charge (%)": data["soc"],
        "Battery Health (%)": data["health"],
        "Temperature (°C)": data["temperature"],
    })

# Convert the results into a table
import pandas as pd

comparison_df = pd.DataFrame(comparison_data)



left_chart, right_chart = st.columns([1.3, 1], gap="medium")

with left_chart:
    st.markdown("### ⚡ Estimated Range")

    fig_range = px.bar(
        comparison_df,
        x="Scenario",
        y="Estimated Range (km)",
        color="Estimated Range (km)",
        color_continuous_scale=["#00E5FF", "#39FF88"],
        template="plotly_dark",
        text_auto=".1f",
    )

    fig_range.update_layout(
        paper_bgcolor="#101F33",
        plot_bgcolor="#101F33",
        font_color="#EAF4FF",
        coloraxis_showscale=False,
        margin=dict(l=10, r=10, t=20, b=10),
        xaxis=dict(
    title="",
    tickangle=0,
    tickfont=dict(size=10),
),
yaxis=dict(
    title="Range (km)",
    tickfont=dict(size=10),
),
    )

    fig_range.update_traces(textposition="outside")
    st.plotly_chart(fig_range, use_container_width=True)





with right_chart:
    st.markdown("### 🔋 Battery Health")

    charge_health_df = comparison_df[
        ["Scenario", "Battery Charge (%)", "Battery Health (%)"]
    ]

    fig_battery = px.bar(
        charge_health_df,
        x="Scenario",
        y=["Battery Charge (%)", "Battery Health (%)"],
        barmode="group",
        color_discrete_sequence=["#00E5FF", "#39FF88"],
        template="plotly_dark",
        text_auto=".0f",
    )

    fig_battery.update_layout(
        paper_bgcolor="#101F33",
        plot_bgcolor="#101F33",
        font_color="#EAF4FF",
        xaxis_title="",
        yaxis_title="Percentage (%)",
        yaxis_range=[0, 110],
        legend_title_text="",
        margin=dict(l=10, r=10, t=20, b=10),
        xaxis=dict(
    title="",
    tickangle=-25,
    tickfont=dict(size=9),
),
yaxis=dict(
    title="%",
    tickfont=dict(size=10),
),
bargap=0.25,
        
    )

    fig_battery.update_traces(textposition="outside")
    st.plotly_chart(fig_battery, use_container_width=True)





st.markdown("---")

temp_panel, details_panel = st.columns([1.4, 1], gap="medium")

with temp_panel:
    st.markdown("### 🌡️ Temperature Analysis")

    temperature_df = comparison_df[
        ["Scenario", "Temperature (°C)"]
    ]

    fig_temp = px.line(
        temperature_df,
        x="Scenario",
        y="Temperature (°C)",
        markers=True,
        template="plotly_dark",
        color_discrete_sequence=["#39FF88"],
    )

    fig_temp.update_layout(
        paper_bgcolor="#101F33",
        plot_bgcolor="#101F33",
        font_color="#EAF4FF",
        xaxis=dict(
            title="",
            tickangle=-20,
            tickfont=dict(size=9),
        ),
        yaxis=dict(
            title="Temperature (°C)",
            tickfont=dict(size=10),
        ),
        margin=dict(l=10, r=10, t=20, b=10),
    )

    fig_temp.update_traces(
        line=dict(width=3),
        marker=dict(size=7, color="#00E5FF"),
    )

    st.plotly_chart(fig_temp, use_container_width=True)

with details_panel:
    st.markdown("### ◈ Battery Summary")

    st.metric("Battery Health", f"{health}%")
    st.metric("State of Charge", f"{soc}%")
    st.metric("Estimated Range", f"{estimated_range:.1f} km")

    st.caption(
        "Summary values reflect the current prototype inputs."
    )



st.write("### Exact Comparison Values")

st.dataframe(comparison_df, hide_index=True, use_container_width=True)


st.divider()
st.subheader("📥 Download Scenario Report")

# Add the risk level to each scenario's comparison row
risk_levels = []

for name in scenario_names:
    data = scenarios[name]

    if data["temperature"] >= 45 or data["health"] < 70:
        risk_levels.append("HIGH")
    elif data["soc"] <= 20:
        risk_levels.append("MODERATE")
    else:
        risk_levels.append("LOW")

comparison_df["Risk Level"] = risk_levels

# Create a downloadable CSV report
csv_report = comparison_df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="Download Scenario Report (CSV)",
    data=csv_report,
    file_name="ev_battery_scenario_report.csv",
    mime="text/csv",
)

st.caption(
    "The report contains simulated scenario data, "
    "not measurements from a real electric vehicle."
)


st.divider()
st.header("🤖 Machine-Learning Range Prediction")

import joblib
import pandas as pd
from pathlib import Path

model_path = Path(__file__).parent / "ev_range_model.pkl"

if model_path.exists():
    ml_model = joblib.load(model_path)

    # Use the dashboard's current slider values
    input_data = pd.DataFrame([{
        "soc": soc,
        "health": health,
        "temperature": temperature,
        "efficiency": driving_efficiency,
    }])

    ml_range = float(ml_model.predict(input_data)[0])
    
    st.subheader("📝 Prediction History")

    history_path = Path(__file__).parent / "prediction_history.csv"

    if st.button("Save Current Prediction"):
        import datetime

        history_row = pd.DataFrame([{
            "Timestamp": datetime.datetime.now().isoformat(
                timespec="seconds"
            ),
            "Battery Charge (%)": soc,
            "Battery Health (%)": health,
            "Temperature (°C)": temperature,
            "Efficiency (km/kWh)": driving_efficiency,
            "Formula Range (km)": round(estimated_range, 1),
            "ML Range (km)": round(ml_range, 1),
        }])

        if history_path.exists():
            history_row.to_csv(
                history_path,
                mode="a",
                header=False,
                index=False,
            )
        else:
            history_row.to_csv(
                history_path,
                index=False,
            )

        st.success("Prediction saved to history!")

    if history_path.exists():
        history_df = pd.read_csv(history_path)

        st.write("### Saved Predictions")
        st.dataframe(
            history_df.tail(20),
            use_container_width=True,
            hide_index=True,
        )
        
        st.write("### Range Estimates Across Saved Predictions")

        chart_df = history_df.tail(20).copy()
        chart_df["Prediction Number"] = range(
            1, len(chart_df) + 1
        )

        chart_df = chart_df.set_index("Prediction Number")

        st.line_chart(
            chart_df[
                ["Formula Range (km)", "ML Range (km)"]
            ]
        )

        st.download_button(
            "Download Prediction History (CSV)",
            data=history_df.to_csv(index=False).encode("utf-8"),
            file_name="prediction_history.csv",
            mime="text/csv",
        )
    else:
        st.info(
            "No predictions saved yet. Click "
            "'Save Current Prediction' to create your first record."
        )

    # Compare against the existing formula estimate
    formula_range = estimated_range

    difference = abs(ml_range - formula_range)

    col1, col2, col3 = st.columns(3, gap="large")

    col1.metric(
        "Formula-Based Range",
        f"{formula_range:.1f} km",
    )

    col2.metric(
        "ML-Predicted Range",
        f"{ml_range:.1f} km",
    )

    col3.metric(
        "Difference",
        f"{difference:.1f} km",
    )

    st.caption(
        "The ML model was trained on a small simulated dataset. "
        "Its output is for demonstration, not a validated real-EV prediction."
    )
    
    
    st.subheader("🔎 Prediction Reliability")

    metrics_path = Path(__file__).parent / "ev_model_metrics.pkl"

    if metrics_path.exists():
        model_metrics = joblib.load(metrics_path)
        test_mae = model_metrics["mae_km"]

        st.write(
            f"On the held-out test examples, the model's "
            f"Mean Absolute Error was **{test_mae:.2f} km**."
        )

        st.warning(
            "This is a small demonstration model trained on "
            "simulated data. The test error is not a guarantee "
            "of the error for this individual prediction or "
            "for a real electric vehicle."
        )

        st.write(
            "**How to improve reliability:** Collect more "
            "representative driving data, use a separate test "
            "dataset, and evaluate performance across different "
            "temperatures, battery ages, and driving conditions."
        )
        st.write("")

    st.divider()
    st.subheader("📊 Range Estimate Comparison")

    range_comparison = pd.DataFrame({
        "Method": [
            "Formula-Based",
            "Machine Learning",
        ],
        "Estimated Range (km)": [
            formula_range,
            ml_range,
        ],
    })

    st.bar_chart(
        range_comparison,
        x="Method",
        y="Estimated Range (km)",
    )

    if difference > 30:
        st.warning(
            "The estimates differ substantially. "
            "The training data and model need further validation."
        )
    else:
        st.info(
            "The estimates are relatively close for this input, "
            "but agreement alone does not prove accuracy."
        )
else:
    st.warning(
        "Model file not found. Run predict_range.py first "
        "to create ev_range_model.pkl."
    )

    
st.divider()
st.header("📈 Model Evaluation")

metrics_path = Path(__file__).parent / "ev_model_metrics.pkl"

if metrics_path.exists():
    model_metrics = joblib.load(metrics_path)

    metric1, metric2 = st.columns(2)

    metric1.metric(
        "Test MAE",
        f"{model_metrics['mae_km']:.2f} km",
    )

    metric2.metric(
        "Test R² Score",
        f"{model_metrics['r2_score']:.3f}",
    )

    st.info(
        "MAE measures average absolute prediction error. "
        "R² measures how well predictions fit the variation "
        "in the test data. These scores use only five "
        "simulated test examples and are not real-world validation."
    )
else:
    st.warning(
        "Evaluation file not found. Run predict_range.py first."
    )


st.markdown("""
<div style="
    margin-top: 40px;
    padding: 18px;
    text-align: center;
    background: #101F33;
    border-top: 1px solid #00E5FF;
    border-radius: 10px;
">
    <p style="color: #00E5FF; margin-bottom: 6px;">
        ⚡ SMART EV MONITOR
    </p>
    <p style="color: #91AEC5; font-size: 12px; margin-bottom: 0;">
        Battery Health & Range Prediction • Educational Prototype
    </p>
    <p style="color: #91AEC5; font-size: 12px; margin-top: 6px;">
        Estimates are simulated and should not be used for safety-critical
        driving or battery decisions.
    </p>
</div>
""", unsafe_allow_html=True)
