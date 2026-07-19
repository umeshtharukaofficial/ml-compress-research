import numpy as np

class Predictor:
    id = "base"
    param_schema = {}
    
    def fit(self, warmup: np.ndarray) -> dict:
        return {}
        
    def predict(self, state: dict, dt: float) -> float:
        return 0.0
        
    def update(self, state: dict, actual: float, dt: float) -> dict:
        return state
        
    def residual_bits_estimate(self, warmup: np.ndarray) -> float:
        return 0.0

PREDICTOR_REGISTRY = {}

def register_predictor(cls):
    PREDICTOR_REGISTRY[cls.id] = cls
    return cls
