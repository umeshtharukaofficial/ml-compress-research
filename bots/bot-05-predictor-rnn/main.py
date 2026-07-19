import os
import sys
import pickle

def main():
    print("Running bot-05-rnn predictor training on all datasets...")
    
    files = ["small_sample.txt", "medium_sample.txt", "large_sample.txt"]
    all_text = ""
    for filename in files:
        filepath = os.path.join("data", filename)
        if os.path.exists(filepath):
            with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
                all_text += f.read()
                
    if not all_text:
         return
         
    transitions = {}
    for i in range(len(all_text) - 1):
        state = all_text[i]
        next_char = all_text[i+1]
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
        
    print("Tiny RNN Markov-predictor trained successfully on multiple scale datasets.")

if __name__ == "__main__":
    main()
