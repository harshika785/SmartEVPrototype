from pathlib import Path
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "data" / "ev_training_data.csv"
OUT.parent.mkdir(parents=True, exist_ok=True)

rng = np.random.default_rng(42)
n = 1000
soc = rng.uniform(10, 100, n)
health = rng.uniform(60, 100, n)
temperature = rng.uniform(10, 50, n)
efficiency = rng.uniform(4, 9, n)
capacity = 40.0

temperature_factor = 1 - 0.008 * np.maximum(np.abs(temperature - 22) - 5, 0)
temperature_factor = np.clip(temperature_factor, 0.65, 1.0)
remaining_energy = capacity * (health / 100) * (soc / 100)
effective_efficiency = efficiency * temperature_factor
noise = rng.normal(0, 4, n)
range_km = np.maximum(0, remaining_energy * effective_efficiency + noise)

df = pd.DataFrame({
    "soc": soc.round(1),
    "health": health.round(1),
    "temperature": temperature.round(1),
    "efficiency": efficiency.round(2),
    "range_km": range_km.round(1),
})
df.to_csv(OUT, index=False)
print(f"Generated {len(df)} simulated training rows at {OUT}")
