import streamlit as st
from utils.common import page_header, current_values, disclaimer

v = current_values()
page_header("Battery Digital Twin", "A virtual battery model that responds immediately when you change the simulation inputs.")

st.markdown("### Virtual battery pack")
fill = max(0, min(100, v["soc"]))
st.markdown(
    f"""
    <div class="panel">
      <div style="display:flex;justify-content:space-between;align-items:center;">
        <div style="font-size:12px;letter-spacing:1.5px;color:#91AEC5;font-weight:700;">VIRTUAL BATTERY STATE</div>
        <div class="status-pill">● INTERACTIVE MODEL</div>
      </div>
      <div style="display:flex;align-items:center;gap:12px;margin:22px 0 8px;">
        <div style="flex:1;border:2px solid #00E5FF;border-radius:12px;padding:5px;height:42px;">
          <div style="height:28px;width:{fill}%;max-width:100%;background:linear-gradient(90deg,#00E5FF,#39FF88);border-radius:6px;"></div>
        </div>
        <div style="font-size:23px;font-weight:800;color:#00E5FF;min-width:65px;">{fill:.0f}%</div>
      </div>
      <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin-top:20px;">
        <div><div class="small-muted">STATE OF HEALTH</div><b style="color:#EAF4FF;font-size:20px;">{v["health"]:.0f}%</b></div>
        <div><div class="small-muted">TEMPERATURE</div><b style="color:#EAF4FF;font-size:20px;">{v["temperature"]:.0f}°C</b></div>
        <div><div class="small-muted">AVAILABLE ENERGY</div><b style="color:#EAF4FF;font-size:20px;">{v["energy"]:.1f} kWh</b></div>
      </div>
    </div>
    """,
    unsafe_allow_html=True,
)
st.markdown("### Virtual operating conditions")
load = st.slider("Simulated driving load (%)", 0, 100, 35, help="A demonstration input; it does not connect to a real vehicle.")
aux = st.selectbox("Auxiliary systems", ["Low (lights/electronics)", "Normal (AC and electronics)", "High (strong AC and accessories)"], index=1)
aux_kw = {"Low (lights/electronics)": 0.3, "Normal (AC and electronics)": 1.2, "High (strong AC and accessories)": 2.2}[aux]
load_kw = 2.0 + (load / 100) * 18 + aux_kw
remaining_hours = v["energy"] / load_kw if load_kw else 0
remaining_distance = remaining_hours * v["efficiency"]

a, b, c = st.columns(3)
a.metric("Illustrative power demand", f"{load_kw:.1f} kW")
b.metric("Estimated operating time", f"{remaining_hours:.1f} h")
c.metric("Illustrative distance at this load", f"{remaining_distance:.1f} km")

if v["temperature"] >= 45:
    st.warning("The selected temperature is above this prototype's demonstration threshold.")
elif v["temperature"] >= 35:
    st.info("The virtual battery is in the prototype's temperature watch range.")
else:
    st.success("No temperature watch message is triggered by the current demonstration rule.")

st.caption("Changing the sidebar controls or operating-condition slider reruns the model and refreshes this virtual state. This is interactive simulation, not live BMS telemetry.")
disclaimer()
