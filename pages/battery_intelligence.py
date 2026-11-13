import streamlit as st
import pandas as pd
from utils.common import page_header, current_values, disclaimer

v = current_values()
page_header("Battery Degradation Forecast", "Explore an illustrative battery-health projection under different usage assumptions.")

st.info("This is a scenario model, not a trained battery-life predictor. It uses user-selected annual degradation assumptions because the supplied dataset does not contain long-term battery ageing measurements.")

c1, c2, c3 = st.columns(3)
annual_km = c1.number_input("Estimated distance driven per year (km)", min_value=1000, max_value=60000, value=12000, step=1000)
usage_profile = c2.selectbox("Usage intensity", ["Light", "Moderate", "Heavy"], index=1)
charging_profile = c3.selectbox("Charging pattern", ["Mostly 20–80%", "Frequent 0–100%", "Frequent fast charging"], index=0)

base_rate = {"Light": 1.2, "Moderate": 1.8, "Heavy": 2.5}[usage_profile]
pattern_add = {"Mostly 20–80%": 0.0, "Frequent 0–100%": 0.5, "Frequent fast charging": 0.7}[charging_profile]
distance_add = max(0, (annual_km - 10000) / 10000) * 0.15
annual_loss = base_rate + pattern_add + distance_add

st.markdown("### Projection assumptions")
x, y = st.columns(2)
x.metric("Current assumed battery health", f'{v["health"]:.1f}%')
y.metric("Illustrative annual health change", f'-{annual_loss:.2f} percentage points')

rows = []
for years in [0.5, 1, 2, 3, 4, 5]:
    projected = max(0, v["health"] - annual_loss * years)
    rows.append({"Time from now": f"{years:g} year(s)", "Illustrative battery health": round(projected, 1)})
projection = pd.DataFrame(rows)

st.markdown("### Estimated battery-health timeline")
st.dataframe(projection, use_container_width=True, hide_index=True)
st.download_button("Download degradation scenario (CSV)", projection.to_csv(index=False).encode("utf-8"), "battery_degradation_scenario.csv", "text/csv")

st.markdown("### How to interpret this")
st.write(
    f"With the selected assumptions, the simple scenario subtracts about {annual_loss:.2f} health percentage points per year. "
    "Real degradation depends on chemistry, cell design, temperature exposure, charging behaviour, age and many other factors. "
    "Replace these assumptions with measured longitudinal battery data before making scientific claims."
)
disclaimer()
