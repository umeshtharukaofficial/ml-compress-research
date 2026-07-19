import os
import sys

def main():
    print("Running bot-04-stream-splitter split parser...")
    os.makedirs("src/tokenizer", exist_ok=True)
    
    # Store dynamic splitting tokens configurations
    configs = {"split_mode": "domains", "active_splitters": ["genomic", "csv", "sensor", "json"]}
    with open("src/tokenizer/vocab.pkl", "wb") as f:
        import pickle
        pickle.dump(configs, f)
    print("Stream splitter configurations initialized successfully.")

if __name__ == "__main__":
    main()
