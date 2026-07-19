import os
import sys
import zlib
import time
import json
import csv

def main():
    print("Running bot-03-baseline analysis...")
    os.makedirs("data", exist_ok=True)
    os.makedirs("experiments/logs", exist_ok=True)
    
    # Process files downloaded in /data folder
    files = [f for f in os.listdir("data") if os.path.isfile(os.path.join("data", f))]
    if not files:
        print("Data directory empty. No files to test.")
        return
        
    results = []
    for filename in files:
        filepath = os.path.join("data", filename)
        with open(filepath, "rb") as f:
            data = f.read()
            
        if len(data) == 0:
            continue
            
        start_time = time.time()
        compressed = zlib.compress(data, level=9)
        end_time = time.time()
        
        ratio = len(data) / len(compressed) if len(compressed) > 0 else 1.0
        time_ms = (end_time - start_time) * 1000
        
        results.append({
            "File": filename,
            "Original_Bytes": len(data),
            "Compressed_Bytes": len(compressed),
            "Compression_Ratio": round(ratio, 4),
            "Time_MS": round(time_ms, 4)
        })
        
    # Log JSON configuration
    with open("experiments/logs/baseline_results.json", "w") as f:
        json.dump(results, f, indent=4)
        
    # Log CSV configuration for live tracking performance
    csv_file = "experiments/logs/performance_tracker.csv"
    file_exists = os.path.exists(csv_file)
    with open(csv_file, "a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["Timestamp", "File", "Original_Bytes", "Compressed_Bytes", "Compression_Ratio", "Time_MS"])
        if not file_exists:
            writer.writeheader()
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        for res in results:
            writer.writerow({
                "Timestamp": timestamp,
                "File": res["File"],
                "Original_Bytes": res["Original_Bytes"],
                "Compressed_Bytes": res["Compressed_Bytes"],
                "Compression_Ratio": res["Compression_Ratio"],
                "Time_MS": res["Time_MS"]
            })
            
    print(f"Baselines successfully updated in {csv_file} for bio-datasets.")

if __name__ == "__main__":
    main()
