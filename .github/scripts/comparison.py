# Script for comparing tools based off category

import json
from collections import defaultdict

def separate_tool():
    # Load tools from file
    with open(".github/scripts/tools.json", "r") as f:
        tools = json.load(f)
    
    # Group tools by category
    grouped_by_category = defaultdict(list)
    for tool in tools:
        grouped_by_category[tool["category"]].append(tool)
    
    # Attributes to compare
    attributes = [
        "tool_name", "tool_url", "deployment", "technical-level",
        "testing_status", "target_users"
    ]
    
    # Generate markdown table per category
    for category, tools_in_cat in grouped_by_category.items():
        print(f"\n## Category: {category}\n")
        headers = ["Tool Name", "URL", "Deployment", "Tech Level", "Testing Status", "Target Users"]
        print("| " + " | ".join(headers) + " |")
        print("|" + " --- |" * len(headers))
    
        for tool in tools_in_cat:
            row = [
                tool.get("tool_name", ""),
                f"[link]({tool.get('tool_url', '')})",
                ", ".join(tool.get("deployment", [])),
                tool.get("technical-level", ""),
                tool.get("testing_status", ""),
                tool.get("target_users", ""),
            ]
            print("| " + " | ".join(row) + " |")


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

    # Find the '### Compare Tools' section
    compare_section_start = None
    for idx, line in enumerate(readme_content):
        if "### Compare Tools" in line:
            compare_section_start = idx
            break

    if compare_section_start is None:
        print("Error: '### Compare Tools' section not found in README.md.")
        sys.exit(1)

    # Find <!-- BEGIN TOOLS --> and <!-- END TOOLS -->
    begin_idx = None
    end_idx = None
    for i in range(compare_section_start, len(readme_content)):
        if "<!-- BEGIN TOOLS -->" in readme_content[i]:
            begin_idx = i
        elif "<!-- END TOOLS -->" in readme_content[i]:
            end_idx = i
            break

    if begin_idx is None or end_idx is None:
        print("Error: Missing <!-- BEGIN TOOLS --> or <!-- END TOOLS --> markers.")
        sys.exit(1)

    separate_tool()

if __name__ == "__main__":
    update_readme()
