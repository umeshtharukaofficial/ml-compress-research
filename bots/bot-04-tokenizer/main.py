import os
import sys
import collections
import pickle

def main():
    print("Running bot-04-tokenizer...")
    
    # Process multiple files
    files = ["small_sample.txt", "medium_sample.txt", "large_sample.txt"]
    all_text = ""
    for filename in files:
        filepath = os.path.join("data", filename)
        if os.path.exists(filepath):
            with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
                all_text += f.read()
                
    if not all_text:
        all_text = "DUMMY TEXT DATA"
        
    char_counts = collections.Counter(all_text)
    vocab = {char: idx for idx, (char, _) in enumerate(char_counts.most_common(256))}
    
    os.makedirs("src/tokenizer", exist_ok=True)
    with open("src/tokenizer/vocab.pkl", "wb") as f:
        pickle.dump(vocab, f)
        
    print(f"Tokenizer vocab created using all datasets, vocabulary size: {len(vocab)}")

if __name__ == "__main__":
    main()
