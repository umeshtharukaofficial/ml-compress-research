import os
import sys
import urllib.request
import json
import xml.etree.ElementTree as ET

def main():
    print("Running bot-01-literature scraper...")
    query = 'neural compression'
    url = f'http://export.arxiv.org/api/query?search_query=all:{urllib.parse.quote(query)}&max_results=3'
    
    try:
        response = urllib.request.urlopen(url)
        data = response.read()
        
        root = ET.fromstring(data)
        namespaces = {'atom': 'http://www.w3.org/2005/Atom'}
        entries = root.findall('atom:entry', namespaces)
        
        os.makedirs("docs", exist_ok=True)
        with open("docs/literature.md", "w") as f:
            f.write("# Literature Logs (arXiv Auto-scraped)\n\n")
            for entry in entries:
                title = entry.find('atom:title', namespaces).text.strip().replace('\n', ' ')
                summary = entry.find('atom:summary', namespaces).text.strip().replace('\n', ' ')
                id_url = entry.find('atom:id', namespaces).text.strip()
                f.write(f"### [{title}]({id_url})\n")
                f.write(f"> {summary[:300]}...\n\n")
        print("Literature scraped and written successfully.")
    except Exception as e:
        print(f"Error scraping arXiv: {e}")

if __name__ == "__main__":
    main()
