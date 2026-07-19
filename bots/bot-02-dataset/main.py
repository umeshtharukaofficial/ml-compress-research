import os
import sys
import urllib.request
import json

def main():
    print("Running bot-02-dataset collector (fetching bio-datasets-1M)...")
    os.makedirs("data", exist_ok=True)
    
    # We will query the GitHub API to fetch raw file data from the user's bio-datasets-1M repository.
    # We target the AMR genomic fasta/fastq reads, amino acid alignments, or markdown datasets.
    repo_api_url = "https://api.github.com/repos/umeshtharukaofficial/bio-datasets-1M/contents"
    
    try:
        req = urllib.request.Request(repo_api_url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            files_list = json.loads(response.read().decode())
            
        text_files_found = 0
        for file_info in files_list:
            if file_info["type"] == "file" and not file_info["name"].startswith("."):
                raw_url = file_info["download_url"]
                dest_path = os.path.join("data", file_info["name"])
                
                print(f"Downloading dataset: {file_info['name']}...")
                urllib.request.urlretrieve(raw_url, dest_path)
                text_files_found += 1
                if text_files_found >= 5: # Limit downloads to save bandwidth/LFS storage
                    break
                    
        print(f"Dataset collector completed. Downloaded {text_files_found} real bio-datasets.")
    except Exception as e:
        print(f"Error fetching bio-datasets-1M: {e}")
        # Fallback to local scaling mock dataset in case of API rate limits
        print("Using scaled fallback data structures...")
        with open("data/scientific_sample.txt", "w") as f:
            f.write("A" * 50000 + "G" * 30000 + "C" * 20000 + "T" * 10000)

if __name__ == "__main__":
    main()
