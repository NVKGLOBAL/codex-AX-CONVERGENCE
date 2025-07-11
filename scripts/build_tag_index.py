import json
import yaml
from collections import defaultdict

def build_semantic_index(ontology_path="build/ontology.json", output_file="build/tag_index.yaml"):
    with open(ontology_path, 'r') as f:
        nodes = json.load(f)
    
    tag_index = defaultdict(list)
    pattern_index = defaultdict(list)
    symbol_index = defaultdict(list)
    
    for node in nodes:
        # Tag indexing
        for tag in node.get('tags', []):
            tag_index[tag].append({
                "id": node["id"],
                "title": node["title"],
                "summary": node["summary"]
            })
        
        # Symbol/pattern indexing (basic implementation)
        if node.get('symbol'):
            symbol_index[node['symbol']].append(node["id"])
        
        # Relation indexing
        for rel_type, rel_targets in node.get('relations', {}).items():
            pattern_index[rel_type].append({
                "source": node["id"],
                "targets": rel_targets
            })
    
    index = {
        "tags": dict(tag_index),
        "patterns": dict(pattern_index),
        "symbols": dict(symbol_index),
        "metadata": {
            "node_count": len(nodes),
            "unique_tags": len(tag_index),
            "unique_patterns": len(pattern_index)
        }
    }
    
    with open(output_file, 'w') as f:
        yaml.dump(index, f, sort_keys=False)
    
    print(f"✅ Built semantic index with {len(nodes)} nodes to {output_file}")
    return index

if __name__ == "__main__":
    build_semantic_index()
