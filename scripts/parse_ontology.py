import glob
import frontmatter
import json
import yaml
from pathlib import Path

def parse_ontology_files(input_path="ontology/*.md", output_format="json"):
    ontology_nodes = []
    
    for file_path in glob.glob(input_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            post = frontmatter.load(f)
            
            node = {
                "id": Path(file_path).stem,
                "title": post.metadata.get('title', ''),
                "tags": post.metadata.get('tags', []),
                "summary": post.metadata.get('summary', ''),
                "content": post.content,
                "relations": post.metadata.get('relations', {}),
                "symbol": post.metadata.get('symbol', ''),
                "file_path": file_path
            }
            ontology_nodes.append(node)
    
    if output_format == "json":
        with open('build/ontology.json', 'w') as f:
            json.dump(ontology_nodes, f, indent=2)
    elif output_format == "yaml":
        with open('build/ontology.yaml', 'w') as f:
            yaml.dump(ontology_nodes, f, sort_keys=False)
    
    return ontology_nodes

if __name__ == "__main__":
    nodes = parse_ontology_files(output_format="json")
    print(f"✅ Parsed {len(nodes)} ontology nodes to build/ontology.json")
