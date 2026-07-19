import numpy as np

class RunLengthZeroCoder:
    def encode(self, coeffs: np.ndarray) -> list:
        # Map values to zero run-lengths and magnitudes
        stream = []
        zero_count = 0
        for val in coeffs:
            if val == 0:
                zero_count += 1
            else:
                stream.append((zero_count, int(val)))
                zero_count = 0
        if zero_count > 0:
            stream.append((zero_count, 0))
        return stream
        
    def decode(self, stream: list) -> np.ndarray:
        decoded = []
        for zero_count, val in stream:
            decoded.extend([0] * zero_count)
            if val != 0:
                decoded.append(val)
        return np.array(decoded)
        
class SignificanceMapCoder:
    def encode(self, coeffs: np.ndarray) -> tuple[np.ndarray, list]:
        sig_map = (coeffs != 0).astype(int)
        magnitudes = list(coeffs[coeffs != 0])
        return sig_map, magnitudes
        
    def decode(self, sig_map: np.ndarray, magnitudes: list) -> np.ndarray:
        decoded = np.zeros_like(sig_map, dtype=float)
        mag_idx = 0
        for i in range(len(sig_map)):
            if sig_map[i] == 1:
                decoded[i] = magnitudes[mag_idx]
                mag_idx += 1
        return decoded
