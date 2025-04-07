# Script for updating the README file with the approved tools
import json
import sys
import os

def update_readme():
    # Get the absolute paths
    script_dir = os.path.dirname(os.path.abspath(__file__))
    repo_root = os.path.dirname(os.path.dirname(script_dir))
    tools_json_path = os.path.join(script_dir, "tools.json")
    readme_path = os.path.join(repo_root, "README.md")
    
    # Load the approved tools from the tools.json file
    try:
        with open(tools_json_path, "r") as f:
            tools = json.load(f)
    except FileNotFoundError:
        print(f"Error: tools.json file not found at {tools_json_path}.")
        sys.exit(1)
    
    # Load the README.md file to update it
    try:
        with open(readme_path, "r") as f:
            readme_content = f.readlines()
    except FileNotFoundError:
        print(f"Error: README.md file not found at {readme_path}.")
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
        "| Category | Tool Name | Description | Status | Deployment | Technical Level | Documentation |\n",
        "|----------|-----------|-------------|---------|------------|-----------------|---------------|\n"
    ]
    
    for tool in tools:
        tool_name = tool.get("tool_name", "Unknown Tool")
        tool_url = tool.get("tool_url", "#")
        category = tool.get("category", "Unknown Category")
        description = tool.get("description", "No description available.")
        status = "Active"  # Assuming the tool is active upon approval
        deployment = ", ".join(tool.get("deployment", []))
        technical_level = "Beginner"  # Default level, can be modified based on tool's complexity
        documentation_url = f"docs/tools/{category.lower().replace(' ', '-')}/{tool_name.lower().replace(' ', '-')}.md"

        tools_section.append(f"| {category} | [{tool_name}]({tool_url}) | {description} | {status} | {deployment} | {technical_level} | [Details]({documentation_url}) |\n")

    # Insert the updated tools section into the README
    updated_readme_content = (
        readme_content[:tools_section_start + 1] + tools_section + readme_content[tools_section_end:]
    )

    # Write the updated content back to README.md
    with open(readme_path, "w") as f:
        f.writelines(updated_readme_content)

    print("README.md updated successfully with the evaluated tools.")

if __name__ == "__main__":
    update_readme()
