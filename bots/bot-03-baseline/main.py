import os
import sys
import zlib
import time
import json
import csv
import pickle
from datetime import datetime

# Access Arithmetic Coder
from bots.bot_09_arithmetic_coder.main import ArithmeticCoder

def main():
    print("Running bot-03-baseline neural evaluation analysis...")
    os.makedirs("data", exist_ok=True)
    os.makedirs("experiments/logs", exist_ok=True)
    
    # Load RNN Model
    model_path = "src/models/rnn_model.pkl"
    probabilities = {}
    if os.path.exists(model_path):
        with open(model_path, "rb") as f:
            probabilities = pickle.load(f)
            
    coder = ArithmeticCoder(probabilities)
    
    files = [f for f in os.listdir("data") if os.path.isfile(os.path.join("data", f))]
    if not files:
        print("Data directory empty. No files to test.")
        return
        
    results = []
    for filename in files:
        filepath = os.path.join("data", filename)
        with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
            data_str = f.read()
        with open(filepath, "rb") as f:
            data_bytes = f.read()
            
        if len(data_bytes) == 0:
            continue
            
        # 1. Evaluate standard Zlib baseline
        zlib_start = time.time()
        zlib_compressed = zlib.compress(data_bytes, level=9)
        zlib_end = time.time()
        zlib_ratio = len(data_bytes) / len(zlib_compressed) if len(zlib_compressed) > 0 else 1.0
        
        # 2. Evaluate our Neural Predictor + Arithmetic Coder
        neural_start = time.time()
        neural_compressed_size = coder.compress(data_str)
        neural_end = time.time()
        neural_ratio = len(data_bytes) / neural_compressed_size if neural_compressed_size > 0 else 1.0
        
        results.append({
            "File": filename,
            "Original_Bytes": len(data_bytes),
            "Zlib_Compressed_Bytes": len(zlib_compressed),
            "Zlib_Ratio": round(zlib_ratio, 4),
            "Neural_Compressed_Bytes": neural_compressed_size,
            "Neural_Ratio": round(neural_ratio, 4),
            "Neural_Time_MS": round((neural_end - neural_start) * 1000, 4)
        })
        
    # Log JSON configuration
    with open("experiments/logs/baseline_results.json", "w") as f:
        json.dump(results, f, indent=4)
        
    # Log CSV configuration for live tracking performance
    csv_file = "experiments/logs/performance_tracker.csv"
    file_exists = os.path.exists(csv_file)
    with open(csv_file, "a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=[
            "Timestamp", "File", "Original_Bytes", 
            "Zlib_Compressed_Bytes", "Zlib_Ratio", 
            "Neural_Compressed_Bytes", "Neural_Ratio", "Neural_Time_MS"
        ])
        if not file_exists:
            writer.writeheader()
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        for res in results:
            writer.writerow({
                "Timestamp": timestamp,
                "File": res["File"],
                "Original_Bytes": res["Original_Bytes"],
                "Zlib_Compressed_Bytes": res["Zlib_Compressed_Bytes"],
                "Zlib_Ratio": res["Zlib_Ratio"],
                "Neural_Compressed_Bytes": res["Neural_Compressed_Bytes"],
                "Neural_Ratio": res["Neural_Ratio"],
                "Neural_Time_MS": res["Neural_Time_MS"]
            })
            
    # Calculate hourly average log updates
    hourly_csv = "experiments/logs/hourly_averages.csv"
    hourly_exists = os.path.exists(hourly_csv)
    
    # Read the last hour logs from the performance tracker
    total_zlib_ratio = 0.0
    total_neural_ratio = 0.0
    total_neural_time = 0.0
    count = 0
    
    if os.path.exists(csv_file):
        with open(csv_file, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    total_zlib_ratio += float(row["Zlib_Ratio"])
                    total_neural_ratio += float(row["Neural_Ratio"])
                    total_neural_time += float(row["Neural_Time_MS"])
                    count += 1
                except:
                    pass
                    
    if count > 0:
        avg_zlib_ratio = round(total_zlib_ratio / count, 4)
        avg_neural_ratio = round(total_neural_ratio / count, 4)
        avg_neural_time = round(total_neural_time / count, 4)
        
        with open(hourly_csv, "a", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=["Timestamp", "Average_Zlib_Ratio", "Average_Neural_Ratio", "Average_Neural_Time_MS", "Evaluated_Test_Count"])
            if not hourly_exists:
                writer.writeheader()
            writer.writerow({
                "Timestamp": timestamp,
                "Average_Zlib_Ratio": avg_zlib_ratio,
                "Average_Neural_Ratio": avg_neural_ratio,
                "Average_Neural_Time_MS": avg_neural_time,
                "Evaluated_Test_Count": count
            })
            
    print(f"Baselines and hourly averages successfully updated in {hourly_csv}")

if __name__ == "__main__":
    main()
