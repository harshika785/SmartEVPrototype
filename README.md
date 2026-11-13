# Smart EV Battery Intelligence System

A multipage Streamlit educational prototype using simulated EV battery data.

## Included features

1. Battery Degradation Forecast (illustrative scenario model)
2. Battery Digital Twin (interactive virtual battery state)
3. Smart Charging Optimizer (constant-power charging estimate)
4. Personalized Energy Saving Coach (illustrative driving scenarios)
5. Existing Random Forest range prediction
6. Prediction history and model information

The Range Confidence / Uncertainty Estimator is intentionally not included.

## 1. Install and run (Windows)

Open this folder in VS Code. Open Terminal > New Terminal and run:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python generate_data.py
python train_model.py
streamlit run app.py
```

Open the local address printed by Streamlit, usually http://localhost:8501.

## 2. Live development workflow

- Keep `streamlit run app.py` running in the VS Code terminal.
- Edit a Python file.
- Press Ctrl+S.
- Streamlit will rerun the application; review the browser.
- Use the sidebar controls to change the shared simulated battery inputs.
- If Streamlit asks whether to rerun, choose Rerun.

## 3. Project layout

- `app.py`: app setup and sidebar navigation
- `pages/`: one Python file per page
- `utils/common.py`: theme, shared inputs and calculations
- `utils/model.py`: model loading and prediction
- `data/`: generated dataset, model, metrics and prediction history
- `generate_data.py`: creates the synthetic training dataset
- `train_model.py`: trains and evaluates the Random Forest model

## 4. Important notes

- This prototype is not connected to a real EV, battery management system, OBD device or charging station.
- The training dataset is synthetic. Model metrics are synthetic holdout results, not real-world validation.
- The degradation forecast uses editable illustrative assumptions. It is not a battery remaining-useful-life model trained on ageing measurements.
- The digital twin is a virtual simulation, not a physics-validated electrochemical model.
- Charging time uses a constant-power approximation and will differ from real vehicle charging curves.
- Energy-coach percentage adjustments are illustrative assumptions, not measured guaranteed savings.
- Do not use this educational prototype for vehicle safety decisions.
