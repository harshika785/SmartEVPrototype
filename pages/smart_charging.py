import streamlit as st
from utils.common import page_header, current_values, disclaimer

v = current_values()
page_header("Smart Charging Optimizer", "Estimate charging energy and time using a simple, transparent calculation.")

st.info("Charging estimates use a constant-power approximation. Real charging power changes with the vehicle, charger, temperature and battery state of charge.")

a, b, c = st.columns(3)
current_soc = a.number_input("Current charge (%)", 0, 99, int(v["soc"]))
target_soc = b.number_input("Target charge (%)", 1, 100, 80)
charger_kw = c.selectbox("Charger power (kW)", [3.3, 7.0, 11.0, 22.0, 50.0], index=1)

efficiency = st.slider("Assumed charging efficiency (%)", 80, 98, 90)
capacity = v["capacity"] * (v["health"] / 100)

if target_soc <= current_soc:
    st.warning("Choose a target charge higher than the current charge to estimate a charging session.")
else:
    required_kwh = capacity * ((target_soc - current_soc) / 100)
    input_energy = required_kwh / (efficiency / 100)
    hours = input_energy / charger_kw
    total_minutes = round(hours * 60)
    hh, mm = divmod(total_minutes, 60)

    st.markdown("### Recommended charging session")
    x, y, z = st.columns(3)
    x.metric("Energy stored", f"{required_kwh:.1f} kWh")
    y.metric("Energy from charger", f"{input_energy:.1f} kWh")
    z.metric("Estimated time", f"{hh} h {mm:02d} min")

    st.progress(int(target_soc), text=f"Target battery charge: {target_soc}%")
    st.markdown("### Charging recommendation")
    if target_soc <= 80:
        st.success("Your selected target is within the commonly used 20–80% planning window. Follow your vehicle maker's charging guidance.")
    else:
        st.info("The selected target is above 80%. This may be useful when extra range is needed, but charging speed and battery guidance vary by vehicle.")
    st.write(f"At an assumed {charger_kw:.1f} kW charger and {efficiency}% efficiency, the simplified model estimates approximately {hh} hours and {mm} minutes.")
disclaimer()
