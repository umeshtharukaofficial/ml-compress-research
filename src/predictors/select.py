import numpy as np
import math
from src.predictors.base import Predictor

def simulate_residuals(predictor: Predictor, params: dict, warmup: np.ndarray) -> np.ndarray:
    residuals = []
    state = predictor.update({}, warmup[0], 1.0)
    for i in range(1, len(warmup)):
        state.update(params)
        x_hat = predictor.predict(state, 1.0)
        r = warmup[i] - x_hat
        residuals.append(r)
        state = predictor.update(state, warmup[i], 1.0)
    return np.array(residuals)

def entropy_bits(residuals: np.ndarray) -> float:
    if len(residuals) == 0:
        return 0.0
    # Basic Shannon entropy calculation based on bin counting
    counts = np.bincount(np.abs(residuals.astype(int)))
    probs = counts / len(residuals)
    entropy = -sum(p * math.log2(p) for p in probs if p > 0)
    return float(entropy)

def quantize(residuals: np.ndarray) -> np.ndarray:
    # Scale and map values to integers to estimate Shannon entropy range values
    return np.round(residuals * 10.0).astype(int)

def choose_best_predictor(warmup: np.ndarray, candidates: list[Predictor]) -> tuple[Predictor, dict]:
    scored = []
    for P in candidates:
        try:
            params = P.fit(warmup)
            residuals = simulate_residuals(P, params, warmup)
            bits = entropy_bits(quantize(residuals))
            scored.append((bits, P, params))
        except Exception:
            # High penalty on fit failures
            scored.append((999.0, P, {}))
            
    scored.sort(key=lambda x: x[0])
    best_candidate = scored[0]
    return best_candidate[1], best_candidate[2]
