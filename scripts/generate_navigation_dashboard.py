import os

SECTIONS = {
    "Entries": "entries",
    "Echoes": "echos",
    "Ontology": "ontology",
    "Protocols": "protocols",
    "Tools": "tools",
    "Milestones": "milestones",
    "Core Principles": "core-principles",
}

OUTPUT_FILE = "meta/index/navigation_dashboard.md"

def extract_files(folder):
    if not os.path.exists(folder):
        return []
    return sorted([f for f in os.listdir(folder) if f.endswith(".md")])

def build_dashboard():
    lines = ["# 🗂️ Navigation Dashboard\n"]
    for section, folder in SECTIONS.items():
        lines.append(f"## {section}\n")
        files = extract_files(folder)
        if not files:
            lines.append("_No files found_\n")
            continue
        for filename in files:
            title = filename.replace("_", " ").replace(".md", "")
            link = f"{folder}/{filename}".replace("\\", "/")
            lines.append(f"- [{title}]({link})")
        lines.append("")  # blank line between sections
    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"✅ Navigation dashboard generated at {OUTPUT_FILE}")

if __name__ == "__main__":
    build_dashboard()
