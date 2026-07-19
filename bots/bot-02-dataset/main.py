import os
import sys
import urllib.request

def main():
    print("Running bot-02-dataset collector...")
    # Target some sample genomic reads or scientific datasets (using small public sequences for testing)
    os.makedirs("data", exist_ok=True)
    
    url = "https://raw.githubusercontent.com/nih-cfde/gtex-analysis/master/README.md"
    target_path = "data/scientific_sample.txt"
    
    try:
        urllib.request.urlretrieve(url, target_path)
        print(f"Dataset retrieved successfully at {target_path}")
    except Exception as e:
        print(f"Error fetching dataset: {e}")

if __name__ == "__main__":
    main()
