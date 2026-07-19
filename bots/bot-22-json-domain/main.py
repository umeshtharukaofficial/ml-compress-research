import os
import sys
import json
import collections

def json_compress(json_text: str) -> dict:
    try:
        data = json.loads(json_text)
    except Exception:
        return {}
        
    # Flat frequency analysis
    keys = []
    def traverse(obj):
        if isinstance(obj, dict):
            for k, v in obj.items():
                keys.append(k)
                traverse(v)
        elif isinstance(obj, list):
            for item in obj:
                traverse(item)
                
    traverse(data)
    
    # Top keys dictionary mappings
    freq = collections.Counter(keys)
    top_keys = [k for k, _ in freq.most_common(256)]
    key_map = {k: idx for idx, k in enumerate(top_keys)}
    
    return {
        "key_dictionary": top_keys,
        "encoded_map": key_map
    }

def main():
    print("Running bot-22-json-domain parser...")
    dummy_json = '{"name": "test", "metric": {"val": 10}}'
    res = json_compress(dummy_json)
    assert len(res["key_dictionary"]) > 0
    print("JSON schema key mapping tables built.")

if __name__ == "__main__":
    main()
