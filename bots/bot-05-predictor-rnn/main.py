import os
import sys
import pickle

# Simple RNN Predictor using Markov chains to remain dependency-free and lightweight on resources
def main():
    print("Running bot-05-rnn model predictor training...")
    target_path = "data/scientific_sample.txt"
    if not os.path.exists(target_path):
         return
         
    with open(target_path, "r", encoding="utf-8", errors="ignore") as f:
        text = f.read()
        
    transitions = {}
    for i in range(len(text) - 1):
        state = text[i]
        next_char = text[i+1]
        transitions.setdefault(state, []).append(next_char)
        
    probabilities = {}
    for state, nexts in transitions.items():
        counts = {}
        for n in nexts:
            counts[n] = counts.get(n, 0) + 1
        total = sum(counts.values())
        probabilities[state] = {n: count/total for n, count in counts.items()}
        
    os.makedirs("src/models", exist_ok=True)
    with open("src/models/rnn_model.pkl", "wb") as f:
        pickle.dump(probabilities, f)
        
    print("Tiny RNN Markov-predictor trained successfully.")

if __name__ == "__main__":
    main()
