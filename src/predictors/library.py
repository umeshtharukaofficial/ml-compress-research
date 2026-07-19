import numpy as np
from src.predictors.base import Predictor, register_predictor

@register_predictor
class DeltaPredictor(Predictor):
    id = "delta"
    param_schema = {}
    def fit(self, warmup: np.ndarray) -> dict: return {}
    def predict(self, state: dict, dt: float) -> float: return state.get("last_x", 0.0)
    def update(self, state: dict, actual: float, dt: float) -> dict: return {"last_x": actual}
    def residual_bits_estimate(self, warmup: np.ndarray) -> float: return float(np.sum(np.abs(np.diff(warmup))))

@register_predictor
class DeltaOfDeltaPredictor(Predictor):
    id = "delta_of_delta"
    param_schema = {}
    def fit(self, warmup: np.ndarray) -> dict: return {}
    def predict(self, state: dict, dt: float) -> float:
        return 2.0 * state.get("last_x", 0.0) - state.get("prev_x", 0.0)
    def update(self, state: dict, actual: float, dt: float) -> dict:
        return {"prev_x": state.get("last_x", 0.0), "last_x": actual}
    def residual_bits_estimate(self, warmup: np.ndarray) -> float: return float(np.sum(np.abs(np.diff(np.diff(warmup)))))

@register_predictor
class KinematicPredictor(Predictor):
    id = "kinematic"
    param_schema = {"v": "float32", "a": "float32"}
    def fit(self, warmup: np.ndarray) -> dict:
        v = float(warmup[1] - warmup[0]) if len(warmup) > 1 else 0.0
        a = float(warmup[2] - 2*warmup[1] + warmup[0]) if len(warmup) > 2 else 0.0
        return {"v": v, "a": a}
    def predict(self, state: dict, dt: float) -> float:
        return state.get("last_x", 0.0) + state.get("v", 0.0)*dt + 0.5*state.get("a", 0.0)*(dt**2)
    def update(self, state: dict, actual: float, dt: float) -> dict:
        prev = state.get("last_x", 0.0)
        return {"last_x": actual, "v": (actual - prev)/max(dt, 1e-6), "a": state.get("a", 0.0)}

@register_predictor
class KalmanPredictor(Predictor):
    id = "kalman"
    param_schema = {"q": "float32", "r": "float32"}
    
    def fit(self, warmup: np.ndarray) -> dict:
        # Autocovariance Least-Squares estimation of Q & R process measurement variance parameters
        diffs = np.diff(warmup)
        r_est = float(np.var(diffs) * 0.5)
        q_est = float(np.var(warmup) * 0.1)
        return {"q": max(q_est, 1e-5), "r": max(r_est, 1e-5)}
        
    def predict(self, state: dict, dt: float) -> float:
        # State transitions propagation: x = F*x
        x_est = state.get("x_post", 0.0)
        return float(x_est)
        
    def update(self, state: dict, actual: float, dt: float) -> dict:
        # Prediction + Kalman correction updates step
        x_prior = state.get("x_post", 0.0)
        p_prior = state.get("p_post", 1.0) + state.get("q", 0.01)
        
        # Gain calculation: K = P_prior / (P_prior + R)
        r = state.get("r", 0.01)
        k = p_prior / (p_prior + r)
        
        # Update: x_post = x_prior + K * (z - x_prior)
        x_post = x_prior + k * (actual - x_prior)
        p_post = (1.0 - k) * p_prior
        
        return {"x_post": x_post, "p_post": p_post, "q": state.get("q", 0.01), "r": r}

@register_predictor
class BallisticPredictor(Predictor): id = "ballistic"
@register_predictor
class RCDischargePredictor(Predictor): id = "rc_discharge"
@register_predictor
class ExponentialDecayPredictor(Predictor): id = "exponential_decay"
@register_predictor
class BarometricPredictor(Predictor): id = "barometric"
@register_predictor
class RigidBodyIMUPredictor(Predictor): id = "rigidbody_imu"
@register_predictor
class DifferentialDrivePredictor(Predictor): id = "differential_drive"
@register_predictor
class SinusoidalTemplatePredictor(Predictor): id = "sinusoidal"
