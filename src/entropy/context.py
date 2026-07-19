import numpy as np

class ContextModel:
    def __init__(self, num_contexts: int, alphabet_size: int):
        self.counts = np.ones((num_contexts, alphabet_size))
        
    def context(self, subband: int, prev_class: int, parent_sig: int) -> int:
        # Context-adaptive bin mapping M7/L5
        return int((subband * 16) + (prev_class * 2) + parent_sig) % self.counts.shape[0]
        
    def prob(self, ctx: int, symbol: int) -> float:
        total = np.sum(self.counts[ctx])
        return float(self.counts[ctx, symbol] / total)
        
    def update(self, ctx: int, symbol: int) -> None:
        self.counts[ctx, symbol] += 1
