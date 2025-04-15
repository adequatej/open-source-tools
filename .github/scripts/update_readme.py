# Script for updating the README file with the approved tools
import json
import sys
import os

def update_readme():
    # Load the approved tools from the tools.json file
    try:
        with open(".github/scripts/tools.json", "r") as f:
            tools = json.load(f)
    except FileNotFoundError:
        print("Error: tools.json file not found.")
        sys.exit(1)
    
    # Load the README.md file to update it
    try:
        with open("README.md", "r") as f:
            readme_content = f.readlines()
    except FileNotFoundError:
        print("Error: README.md file not found.")
        sys.exit(1)

    # Find the position where to insert the tools section in README.md
    tools_section_start = None
    tools_section_end = None

    for idx, line in enumerate(readme_content):
        if "<!-- BEGIN TOOLS -->" in line:
            tools_section_start = idx
            break
    
    if tools_section_start is None:
        print("Error: '<!-- BEGIN TOOLS -->' section not found in README.md.")
        sys.exit(1)

    # Look for the end of the tools section
    tools_section_end = tools_section_start + 1
    while tools_section_end < len(readme_content) and "<!-- END TOOLS -->" not in readme_content[tools_section_end]:
        tools_section_end += 1

    if tools_section_end >= len(readme_content):
        print("Error: '<!-- END TOOLS -->' section not found in README.md.")
        sys.exit(1)

    # Build the tools table section
    tools_section = [
        "| Tool Name | Category | Description | Status | Deployment | Technical Level | Documentation | Overall Rating |\n",
        "|----------|-----------|-------------|---------|------------|-----------------|---------------|-------|\n"
    ]
    
    for tool in tools:
        tool_name = tool.get("tool_name", "Unknown Tool")
        tool_url = tool.get("tool_url", "#")
        category = tool.get("category", "Unknown Category")
        description = tool.get("description", "No description available.")
        status = tool.get("status", "N/A")  # Assuming the tool is active upon approval
        deployment = ", ".join(tool.get("deployment", []))
        technical_level = tool.get("technical-level", "Unknown Technical Level") # Default level, can be modified based on tool's complexity
        overall_rating = tool.get("overall-rating", "N/A")
        documentation_url = f"docs/tools/{category.lower().replace(' ', '-')}/{tool_name.replace(' ', '-')}.md"

        # Construct documentation path
        doc_dir = f"docs/tools/{category.lower().replace(' ', '-')}"
        doc_file = f"{doc_dir}/{tool_name.replace(' ', '-')}.md"

        # Ensure the directory exists
        os.makedirs(doc_dir, exist_ok=True)

        if not os.path.exists(doc_file):
            with open(doc_file, "w") as df:
                df.write(f"# {tool_name}\n\n")
                df.write(tool.get("testing-documentation", "Documentation coming soon.") + "\n")
        else:
            with open(doc_file, "w") as df:
                df.write(f"# {tool_name}\n\n")
                df.write(tool.get("testing-documentation", "Documentation coming soon.") + "\n")


        tools_section.append(f"| [{tool_name}]({tool_url}) | {category} | {description} | {status} | {deployment} | {technical_level} | [Details]({documentation_url}) | {overall_rating} |\n")

    # Insert the updated tools section into the README
    updated_readme_content = (
        readme_content[:tools_section_start + 1] + tools_section + readme_content[tools_section_end:]
    )

    # Write the updated content back to README.md
    with open("README.md", "w") as f:
        f.writelines(updated_readme_content)

    print("README.md updated successfully with the evaluated tools.")

if __name__ == "__main__":
    update_readme()
