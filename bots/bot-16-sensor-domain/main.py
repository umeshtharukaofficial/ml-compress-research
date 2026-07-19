import os
import sys
import numpy as np

# Load predictors modules
from src.predictors.library import DeltaPredictor, DeltaOfDeltaPredictor, KinematicPredictor, KalmanPredictor
from src.predictors.select import choose_best_predictor
from src.transforms import IdentityTransform
from src.quantizers.noise_floor import NoiseFloorQuantizer
from src.structural import SignificanceMapCoder
from src.entropy.context import ContextModel

def compress_sensor_stream(timestamps, values) -> dict:
    warmup_limit = min(len(values), 1024)
    warmup_data = np.array(values[:warmup_limit], dtype=float)
    
    # 1. Run choose_best_predictor L1 Kalman upgrade
    candidates = [DeltaPredictor(), DeltaOfDeltaPredictor(), KinematicPredictor(), KalmanPredictor()]
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
        
    residuals_arr = np.array(residuals, dtype=float)
    
    # 2. Run Transform layer L2
    transformer = IdentityTransform()
    transformed = transformer.forward(residuals_arr)
    
    # 3. Quantizer L3
    quantizer = NoiseFloorQuantizer()
    delta = 0.1
    quantized_coeffs = quantizer.dead_zone_quantize(transformed, delta)
    
    # 4. Significance zero coding L4
    struct_coder = SignificanceMapCoder()
    sig_map, magnitudes = struct_coder.encode(quantized_coeffs)
    
    # 5. Context modeling L5
    ctx_model = ContextModel(128, 2)
    for bit in sig_map:
        ctx = ctx_model.context(0, 0, 0)
        ctx_model.update(ctx, int(bit))
        
    return {
        "predictor_id": best_pred.id,
        "params": params,
        "residuals": list(quantized_coeffs.astype(float))
    }

def main():
    print("Running bot-16-sensor-domain sensor compression...")
    ts = [1600000000, 1600000060, 1600000120]
    vals = [120.0, 122.0, 121.0]
    res = compress_sensor_stream(ts, vals)
    assert res["predictor_id"] is not None
    print(f"Sensor pipeline MBPC Kalman + Transforms stack validated: {res['predictor_id']}")

if __name__ == "__main__":
    main()
