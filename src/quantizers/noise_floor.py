import numpy as np

class NoiseFloorQuantizer:
    def characterize(self, quiescent: np.ndarray) -> np.ndarray:
        return np.std(quiescent) if len(quiescent) > 0 else np.array([1.0])
        
    def dead_zone_quantize(self, coeffs: np.ndarray, delta: float) -> np.ndarray:
        # DZ-USQ Implementation matching L3 logic
        q = np.zeros_like(coeffs)
        half_d = delta / 2.0
        mask = np.abs(coeffs) >= half_d
        q[mask] = np.sign(coeffs[mask]) * np.floor((np.abs(coeffs[mask]) - half_d) / delta + 1.0)
        return q.astype(int)
        
    def dequantize(self, q: np.ndarray, delta: float) -> np.ndarray:
        return (q * delta).astype(float)
