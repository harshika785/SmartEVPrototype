import streamlit as st
from utils.common import page_header, current_values, disclaimer

v = current_values()
page_header("Personalized Energy Saving Coach", "Compare illustrative driving habits and see how efficiency assumptions affect estimated range.")

style = st.selectbox("Driving style", ["Eco", "Normal", "Aggressive"], index=1)
speed = st.selectbox("Typical driving speed", ["Steady moderate speed", "Frequent high-speed driving"], index=0)
climate = st.selectbox("Cabin climate use", ["Low", "Moderate", "High"], index=1)
regen = st.selectbox("Regenerative braking use", ["Frequent", "Occasional", "Minimal"], index=0)

style_factor = {"Eco": 1.08, "Normal": 1.00, "Aggressive": 0.88}[style]
speed_factor = {"Steady moderate speed": 1.00, "Frequent high-speed driving": 0.90}[speed]
climate_factor = {"Low": 1.02, "Moderate": 1.00, "High": 0.94}[climate]
regen_factor = {"Frequent": 1.03, "Occasional": 1.00, "Minimal": 0.97}[regen]

factor = style_factor * speed_factor * climate_factor * regen_factor
adjusted_efficiency = v["efficiency"] * factor
adjusted_range = v["energy"] * adjusted_efficiency
baseline_range = v["range_km"]
change = adjusted_range - baseline_range

st.markdown("### Your estimated driving profile")
a, b, c = st.columns(3)
a.metric("Baseline range", f"{baseline_range:.1f} km")
b.metric("Scenario range", f"{adjusted_range:.1f} km", delta=f"{change:+.1f} km")
c.metric("Scenario efficiency", f"{adjusted_efficiency:.2f} km/kWh")

st.markdown("### Coaching suggestions")
tips = []
if style == "Aggressive":
    tips.append("Try smoother acceleration and braking to reduce energy demand.")
elif style == "Eco":
    tips.append("Continue using smoother acceleration and a steady driving style.")
else:
    tips.append("Try an Eco driving profile when additional range is important.")
if speed == "Frequent high-speed driving":
    tips.append("A steadier, moderate speed may reduce aerodynamic energy losses.")
if climate == "High":
    tips.append("Use cabin climate settings thoughtfully; auxiliary loads can reduce available range.")
if regen == "Minimal":
    tips.append("Where supported and appropriate, use regenerative braking to recover some energy.")
if not tips:
    tips.append("Your selected assumptions represent an efficiency-focused scenario. Keep monitoring actual consumption.")

for tip in tips:
    st.markdown(f"- {tip}")

st.caption("The scenario factors are illustrative demonstration assumptions, not measured vehicle-specific efficiency gains.")
disclaimer()
