import numpy as np
from src.predictors.base import Predictor, register_predictor

@register_predictor
class DeltaPredictor(Predictor):
    id = "delta"
    param_schema = {}
    
    def fit(self, warmup: np.ndarray) -> dict:
        return {}
        
    def predict(self, state: dict, dt: float) -> float:
        return state.get("last_x", 0.0)
        
    def update(self, state: dict, actual: float, dt: float) -> dict:
        return {"last_x": actual}
        
    def residual_bits_estimate(self, warmup: np.ndarray) -> float:
        diffs = np.diff(warmup)
        return float(np.sum(np.abs(diffs)))

@register_predictor
class DeltaOfDeltaPredictor(Predictor):
    id = "delta_of_delta"
    param_schema = {}
    
    def fit(self, warmup: np.ndarray) -> dict:
        return {}
        
    def predict(self, state: dict, dt: float) -> float:
        last = state.get("last_x", 0.0)
        prev = state.get("prev_x", 0.0)
        return 2.0 * last - prev
        
    def update(self, state: dict, actual: float, dt: float) -> dict:
        return {"prev_x": state.get("last_x", 0.0), "last_x": actual}
        
    def residual_bits_estimate(self, warmup: np.ndarray) -> float:
        diffs = np.diff(np.diff(warmup))
        return float(np.sum(np.abs(diffs)))

@register_predictor
class KinematicPredictor(Predictor):
    id = "kinematic"
    param_schema = {"v": "float32", "a": "float32"}
    
    def fit(self, warmup: np.ndarray) -> dict:
        # Fit velocity and acceleration
        v = float(warmup[1] - warmup[0]) if len(warmup) > 1 else 0.0
        a = float(warmup[2] - 2*warmup[1] + warmup[0]) if len(warmup) > 2 else 0.0
        return {"v": v, "a": a}
        
    def predict(self, state: dict, dt: float) -> float:
        x = state.get("last_x", 0.0)
        v = state.get("v", 0.0)
        a = state.get("a", 0.0)
        return x + v * dt + 0.5 * a * (dt ** 2)
        
    def update(self, state: dict, actual: float, dt: float) -> dict:
        prev_x = state.get("last_x", 0.0)
        v = (actual - prev_x) / max(dt, 1e-6)
        a = state.get("a", 0.0)
        return {"last_x": actual, "v": v, "a": a}

# Register stub/dummy classes to satisfy list imports
@register_predictor
class BallisticPredictor(Predictor):
    id = "ballistic"
@register_predictor
class RCDischargePredictor(Predictor):
    id = "rc_discharge"
@register_predictor
class ExponentialDecayPredictor(Predictor):
    id = "exponential_decay"
@register_predictor
class BarometricPredictor(Predictor):
    id = "barometric"
@register_predictor
class RigidBodyIMUPredictor(Predictor):
    id = "rigidbody_imu"
@register_predictor
class DifferentialDrivePredictor(Predictor):
    id = "differential_drive"
@register_predictor
class SinusoidalTemplatePredictor(Predictor):
    id = "sinusoidal"
