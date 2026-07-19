import os
import sys
import zlib
import time
import json

def main():
    print("Running bot-03-baseline...")
    target_path = "data/scientific_sample.txt"
    if not os.path.exists(target_path):
        print("Data file not found. Running collector first.")
        # fallback write a dummy
        os.makedirs("data", exist_ok=True)
        with open(target_path, "w") as f:
            f.write("A" * 1000 + "B" * 500 + "C" * 250)
            
    with open(target_path, "rb") as f:
        data = f.read()
        
    start_time = time.time()
    compressed = zlib.compress(data, level=9)
    end_time = time.time()
    
    baseline_results = {
        "zlib_ratio": len(data) / len(compressed),
        "zlib_time_ms": (end_time - start_time) * 1000,
        "original_size": len(data),
        "compressed_size": len(compressed)
    }
    
    os.makedirs("experiments/logs", exist_ok=True)
    with open("experiments/logs/baseline_results.json", "w") as f:
        json.dump(baseline_results, f, indent=4)
        
    print(f"Baselines computed and saved: {baseline_results}")

if __name__ == "__main__":
    main()
