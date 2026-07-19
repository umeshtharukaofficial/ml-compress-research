import os
import sys

def main():
    print("Running bot-02-dataset generator...")
    os.makedirs("data", exist_ok=True)
    
    # Generate datasets of varying sizes (small, medium, large)
    # Using repeating character patterns so they compress differently
    datasets = {
        "small_sample.txt": ("A" * 1000 + "B" * 500 + "C" * 250),
        "medium_sample.txt": ("A" * 10000 + "B" * 5000 + "C" * 2500),
        "large_sample.txt": ("A" * 100000 + "B" * 50000 + "C" * 25000)
    }
    
    for filename, content in datasets.items():
        filepath = os.path.join("data", filename)
        with open(filepath, "w") as f:
            f.write(content)
        print(f"Generated dataset {filepath} (Size: {len(content)} bytes)")

if __name__ == "__main__":
    main()
