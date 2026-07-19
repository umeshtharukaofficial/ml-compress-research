import os
import sys

def main():
    print("Running bot-02-dataset collector...")
    
    # Establish domains targets directories matching B4 specifications
    domains = ["genomic", "csv", "sensor", "json"]
    for dom in domains:
        folder = os.path.join("data", dom)
        os.makedirs(folder, exist_ok=True)
        
    # Write real manifest URLs instead of committing huge raw data sequences
    manifest = {
        "genomic": [
            {"name": "SRR000001_100k.fastq", "url": "https://raw.githubusercontent.com/umeshtharukaofficial/bio-datasets-1M/main/SRR000001_100k.fastq", "size_kb": 1024},
            {"name": "NC_000913_ecoli.fasta", "url": "https://raw.githubusercontent.com/umeshtharukaofficial/bio-datasets-1M/main/NC_000913.3.fasta", "size_kb": 4600}
        ],
        "csv": [
            {"name": "uci_adult.csv", "url": "https://raw.githubusercontent.com/umeshtharukaofficial/bio-datasets-1M/main/adult.csv", "size_kb": 4000}
        ]
    }
    
    with open("data/manifest.json", "w") as f:
        json.dump(manifest, f, indent=4)
        
    print("Dataset manifests stored successfully.")

if __name__ == "__main__":
    main()
