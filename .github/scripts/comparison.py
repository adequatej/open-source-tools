import json
import sys
import os
from collections import defaultdict

def update_readme():
    # Load tools from file
    try:
        with open(".github/scripts/tools.json", "r") as f:
            tools = json.load(f)
    except FileNotFoundError:
        print("Error: tools.json file not found.")
        sys.exit(1)

    # Load README
    try:
        with open("README.md", "r") as f:
            readme_content = f.readlines()
    except FileNotFoundError:
        print("Error: README.md file not found.")
        sys.exit(1)

    # Find the section markers
    begin_idx = None
    end_idx = None
    for idx, line in enumerate(readme_content):
        if "<!-- BEGIN TOOLS -->" in line:
            begin_idx = idx
        elif "<!-- END TOOLS -->" in line:
            end_idx = idx
            break

    if begin_idx is None or end_idx is None:
        print("Error: Missing <!-- BEGIN TOOLS --> or <!-- END TOOLS --> markers in README.md.")
        sys.exit(1)

    # Group tools by category
    grouped_by_category = defaultdict(list)
    for tool in tools:
        grouped_by_category[tool.get("category", "Uncategorized")].append(tool)

    # Generate markdown content
    markdown_lines = []
    for category, tools_in_cat in grouped_by_category.items():
        markdown_lines.append(f"\n### Category: {category}\n")
        markdown_lines.append("| Tool Name | Description | Status | Deployment | Tech Level | Docs |")
        markdown_lines.append("|-----------|-------------|--------|------------|------------|------|")
        for tool in tools_in_cat:
            tool_name = tool.get("tool_name", "Unknown")
            tool_url = tool.get("tool_url", "#")
            description = tool.get("description", "No description available.")
            status = "Active"
            deployment = ", ".join(tool.get("deployment", []))
            tech_level = tool.get("technical-level", "N/A")

            # Construct documentation path
            doc_dir = f"docs/tools/{category.lower().replace(' ', '-')}"
            doc_file = f"{doc_dir}/{tool_name.replace(' ', '-')}.md"
            doc_link = f"[Details]({doc_file})"

            os.makedirs(doc_dir, exist_ok=True)
            if not os.path.exists(doc_file):
                with open(doc_file, "w") as df:
                    df.write(f"# {tool_name}\n\n")
                    df.write(f"**Category**: {category}\n\n")
                    df.write(f"**Description**: {description}\n\n")
                    df.write("Documentation coming soon.\n")

            markdown_lines.append(
                f"| [{tool_name}]({tool_url}) | {description} | {status} | {deployment} | {tech_level} | {doc_link} |"
            )

    # Replace content in README between the markers
    new_readme_content = (
        readme_content[:begin_idx + 1] +
        [line + "\n" for line in markdown_lines] +
        readme_content[end_idx:]
    )

    # Write back to README.md
    with open("README.md", "w") as f:
        f.writelines(new_readme_content)

    print("README.md updated successfully with categorized tool table.")

if __name__ == "__main__":
    update_readme()
