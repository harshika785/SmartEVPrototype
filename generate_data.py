
import numpy as np
import pandas as pd

# Reproducible simulated data
rng = np.random.default_rng(42)
n = 1000

# Simulated battery and driving conditions
soc = rng.uniform(10, 100, n)
health = rng.uniform(60, 100, n)
temperature = rng.uniform(10, 50, n)
efficiency = rng.uniform(4, 9, n)
capacity = 40.0  # Assumed usable capacity when new, in kWh

# Illustrative temperature effect on driving efficiency
temperature_factor = 1 - 0.008 * np.maximum(
    np.abs(temperature - 22) - 5, 0
)
temperature_factor = np.clip(temperature_factor, 0.65, 1.0)

# Consistent simplified range calculation
remaining_energy = capacity * (health / 100) * (soc / 100)
effective_efficiency = efficiency * temperature_factor

# Add small simulated variation to represent unmodelled factors
noise = rng.normal(0, 4, n)

range_km = np.maximum(
    0,
    remaining_energy * effective_efficiency + noise
)

df = pd.DataFrame({
    "soc": soc.round(1),
    "health": health.round(1),
    "temperature": temperature.round(1),
    "efficiency": efficiency.round(2),
    "range_km": range_km.round(1),
})

df.to_csv("ev_training_data.csv", index=False)

print("Generated simulated EV dataset successfully!")
print(f"Number of examples: {len(df)}")
print("\nFirst five rows:")
print(df.head())
print("\nRange summary:")
print(df["range_km"].describe().round(1))