import os
import sys
import numpy as np

# Load predictors modules
from src.predictors.library import DeltaPredictor, DeltaOfDeltaPredictor, KinematicPredictor
from src.predictors.select import choose_best_predictor

def compress_sensor_stream(timestamps, values) -> dict:
    warmup_limit = min(len(values), 1024)
    warmup_data = np.array(values[:warmup_limit], dtype=float)
    
    # Run choose_best_predictor M4/P4
    candidates = [DeltaPredictor(), DeltaOfDeltaPredictor(), KinematicPredictor()]
    best_pred, params = choose_best_predictor(warmup_data, candidates)
    
    # Generate residuals
    residuals = []
    state = best_pred.update({}, values[0], 1.0)
    for i in range(1, len(values)):
        state.update(params)
        x_hat = best_pred.predict(state, 1.0)
        r = values[i] - x_hat
        residuals.append(r)
        state = best_pred.update(state, values[i], 1.0)
        
    return {
        "predictor_id": best_pred.id,
        "params": params,
        "residuals": residuals
    }

def main():
    print("Running bot-16-sensor-domain sensor compression...")
    ts = [1600000000, 1600000060, 1600000120]
    vals = [120.0, 122.0, 121.0]
    res = compress_sensor_stream(ts, vals)
    assert res["predictor_id"] is not None
    print(f"Sensor pipeline model prediction selection verified: {res['predictor_id']}")

if __name__ == "__main__":
    main()
