# Script for updating the README file with the approved tools
import json
import sys
import os
from datetime import datetime

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
        "| Tool Name | Category | Description | Status | Deployment | Technical Level | Documentation | Overall Rating | Last Tested |\n",
        "|----------|-----------|-------------|---------|------------|-----------------|---------------|----------------|-------------|\n"
    ]
    
    # Only include tools that have been tested and approved
    evaluated_tools = [tool for tool in tools if "version-tested" in tool]
    
    for tool in evaluated_tools:
        tool_name = tool.get("tool-name", "Unknown Tool")
        tool_url = tool.get("tool-url", "#")
        category = tool.get("category", "Unknown Category")
        description = tool.get("description", "No description available.")
        status = tool.get("status", "Active")  # Default to Active for evaluated tools
        deployment = ", ".join(tool.get("deployment-type", []))  # Join array into comma-separated string
        technical_level = tool.get("technical-level", "Unknown Technical Level")
        overall_rating = tool.get("overall-rating", "N/A")
        date_tested = tool.get("date-tested", "N/A")
        tool_name_safe = tool_name.replace(" ", "-")
        # Construct documentation path
        doc_dir = f"docs/tools/categories/{category.lower().replace(' ', '-')}"
        doc_file = f"{doc_dir}/{tool_name_safe}.md"
        documentation_url = f"docs/tools/categories/{category.lower().replace(' ', '-')}/{tool_name_safe}.md"

        # Ensure the directory exists
        os.makedirs(doc_dir, exist_ok=True)

        # Create or update documentation file with testing information
        with open(doc_file, "w") as df:
            df.write(f"# {tool_name}\n\n")
            
            # Basic Information
            df.write(f"## Basic Information\n")
            df.write(f"- **Category**: {tool.get('category', 'N/A')}\n")
            df.write(f"- **URL**: {tool.get('tool-url', 'N/A')}\n")
            df.write(f"- **Description**: {tool.get('description', 'N/A')}\n")
            df.write(f"- **Status**: {tool.get('status', 'Active')}\n\n")
            
            # Deployment Information
            df.write(f"## Deployment Information\n")
            df.write(f"- **Deployment Types**: {', '.join(tool.get('deployment-type', []))}\n")
            df.write(f"- **Technical Level Required**: {tool.get('technical-level', 'N/A')}\n\n")
            
            # Testing Information
            df.write(f"## Testing Information\n")
            df.write(f"- **Version Tested**: {tool.get('version-tested', 'N/A')}\n")
            df.write(f"- **Date Tested**: {tool.get('date-tested', 'N/A')}\n")
            df.write(f"- **Testing Environment**: {tool.get('testing-environment', 'N/A')}\n")
            df.write(f"- **Testing Documentation**: {tool.get('testing-documentation', 'N/A')}\n")
            df.write(f"- **Overall Rating**: {tool.get('overall-rating', 'N/A')}\n")
            df.write(f"- **Evaluation Checklist**:\n")
            for item in tool.get('evaluation-checklist', []):
                df.write(f"  - {item}\n")
            df.write("\n")
            
            # Additional Information
            if tool.get('additional-notes'):
                df.write(f"## Additional Notes\n")
                df.write(f"{tool.get('additional-notes')}\n\n")
            
            # Submission Information
            df.write(f"## Submission Information\n")
            df.write(f"- **Submitted By**: {tool.get('submitted_by', 'N/A')}\n")
            df.write(f"- **Submission Date**: {datetime.fromtimestamp(tool.get('date_submitted', 0)).strftime('%Y-%m-%d')}\n")
            df.write(f"- **Last Updated**: {datetime.fromtimestamp(tool.get('date_updated', 0)).strftime('%Y-%m-%d')}\n")

        # Ensure all fields are properly formatted for the table
        description = description.replace("|", "\\|")  # Escape pipe characters
        deployment = deployment.replace("|", "\\|")
        technical_level = technical_level.replace("|", "\\|")

        tools_section.append(f"| [{tool_name}]({tool_url}) | {category} | {description} | {status} | {deployment} | {technical_level} | [Details]({documentation_url}) | {overall_rating} | {date_tested} |\n")

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
