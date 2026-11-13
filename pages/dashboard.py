import streamlit as st
from utils.common import page_header, current_values, disclaimer

v = current_values()
page_header("EV Battery Dashboard", "A clean overview of the current simulated battery state.")

st.markdown('<span class="status-pill">● SIMULATION READY</span>', unsafe_allow_html=True)
st.write("")
a, b, c, d = st.columns(4)
a.metric("Battery health", f'{v["health"]:.0f}%')
b.metric("State of charge", f'{v["soc"]:.0f}%')
c.metric("Estimated range", f'{v["range_km"]:.1f} km')
d.metric("Temperature", f'{v["temperature"]:.0f} °C')

st.markdown("### Battery charge")
st.progress(int(v["soc"]), text=f'Current charge: {v["soc"]:.0f}%')
left, right = st.columns([1.2, 1], gap="large")
with left:
    # Use Streamlit's native container rather than opening/closing HTML tags
    # across separate st.markdown calls (those tags are not guaranteed to pair).
    with st.container(border=True):
        st.markdown("**ENERGY AVAILABLE**")
        st.metric("Estimated remaining energy", f'{v["energy"]:.1f} kWh')
        st.caption(
            f'Calculated using {v["capacity"]:.0f} kWh usable capacity and '
            f'{v["health"]:.0f}% assumed state of health.'
        )
with right:
    with st.container(border=True):
        st.markdown("**BATTERY CONDITION**")
        if v["temperature"] >= 45:
            st.warning("High temperature in this demonstration. Review the vehicle manufacturer's guidance.")
        elif v["temperature"] >= 35:
            st.info("Temperature is in the prototype's watch range.")
        else:
            st.success("Temperature is within the prototype's lower-temperature range.")
        st.caption("These are illustrative thresholds, not a battery safety diagnosis.")

st.markdown("### Quick navigation")
st.write("Use the sidebar to open Battery Intelligence, Digital Twin, Smart Charging, Energy Coach, AI Prediction and your saved records.")
disclaimer()
