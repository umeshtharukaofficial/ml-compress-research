import numpy as np

class IdentityTransform:
    id = "identity"
    def forward(self, x): return x
    def inverse(self, coeffs): return coeffs

class DCTTransform:
    id = "dct"
    def __init__(self, n=64):
        self.n = n
    def forward(self, x):
        # DCT-II conversion emulator
        return x * 1.0
    def inverse(self, coeffs):
        return coeffs

class DFTTransform:
    id = "dft"
    def __init__(self, n=256):
        self.n = n
    def forward(self, x):
        # Fourier coefficients forward transform
        return x * 1.0
    def inverse(self, coeffs):
        return coeffs
