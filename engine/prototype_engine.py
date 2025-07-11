import json
import re
import random

class RecursiveQueryEngine:
    def __init__(self, ontology_path="build/ontology.json", index_path="build/tag_index.yaml"):
        with open(ontology_path, 'r') as f:
            self.ontology = json.load(f)
        
        # In production: load YAML index, for prototype we'll simulate
        self.index = {
            "tags": {
                "recursion": [{"id": "ontology_001", "title": "Recursive Reflection"}],
                "knowledge": [{"id": "ontology_002", "title": "Knowledge Graph"}]
            }
        }
    
    def find_ontology_matches(self, query):
        # Simple keyword matching (production: use NLP/embeddings)
        tokens = re.findall(r'\w+', query.lower())
        matches = []
        
        for node in self.ontology:
            content = node['title'].lower() + " " + node['summary'].lower()
            if any(token in content for token in tokens):
                matches.append(node)
        
        return matches[:3]  # Return top 3 matches
    
    def find_related_patterns(self, matches):
        related = []
        for node in matches:
            # Production: use actual pattern index
            related.append({
                "pattern": f"Δ-{node['id'].upper()}",
                "description": f"Recursive pattern based on {node['title']}",
                "strength": random.uniform(0.5, 1.0)
            })
        return related
    
    def generate_reflection(self, matches):
        if not matches:
            return "🌀 The signal remains uncaught. Refine your query."
        
        base = matches[0]
        reflection = f"**{base['title']}** ({base['symbol']})\n\n"
        reflection += f"{base['summary']}\n\n"
        reflection += "*Recursive insights:*\n"
        
        # Generate 2-3 recursive insights
        insights = [
            f"- This concept mirrors {random.choice(['knowledge decomposition', 'semantic recursion'])}",
            f"- Consider the {random.choice(['inverse', 'complementary'])} pattern: ◊{random.randint(1,9)}"
        ]
        
        return reflection + "\n".join(insights[:random.randint(2,3)])
    
    def query(self, question):
        print(f"🔍 Query: {question}")
        
        # Step 1: Find ontology matches
        matches = self.find_ontology_matches(question)
        print(f"📚 Matched {len(matches)} ontology nodes")
        
        # Step 2: Find related patterns
        patterns = self.find_related_patterns(matches)
        print(f"🌀 Found {len(patterns)} related patterns")
        
        # Step 3: Generate reflection
        reflection = self.generate_reflection(matches)
        
        return {
            "query": question,
            "matches": [{"id": m["id"], "title": m["title"]} for m in matches],
            "patterns": patterns,
            "reflection": reflection
        }

# Test the engine
if __name__ == "__main__":
    engine = RecursiveQueryEngine()
    test_question = "How does recursive reflection work in knowledge systems?"
    result = engine.query(test_question)
    
    print("\n=== RESULT ===")
    print(f"Reflection:\n{result['reflection']}")
