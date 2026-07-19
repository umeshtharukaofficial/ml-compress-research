import os
import sys
import collections
import pickle

def main():
    print("Running bot-04-tokenizer...")
    target_path = "data/scientific_sample.txt"
    if not os.path.exists(target_path):
        os.makedirs("data", exist_ok=True)
        with open(target_path, "w") as f:
            f.write("A" * 1000 + "B" * 500)
            
    with open(target_path, "r", encoding="utf-8", errors="ignore") as f:
        text = f.read()
        
    # Build simple frequency-based tokenizer mapping
    char_counts = collections.Counter(text)
    vocab = {char: idx for idx, (char, _) in enumerate(char_counts.most_common(256))}
    
    os.makedirs("src/tokenizer", exist_ok=True)
    with open("src/tokenizer/vocab.pkl", "wb") as f:
        pickle.dump(vocab, f)
        
    print(f"Tokenizer vocab created with size: {len(vocab)}")

if __name__ == "__main__":
    main()
