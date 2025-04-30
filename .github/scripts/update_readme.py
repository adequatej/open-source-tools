# Script for updating the README file with the approved tools
import json
import sys
import os
from datetime import datetime

def format_star_rating(rating):
    try:
        rating_float = float(rating)
        full_stars = int(rating_float)
        half_star = rating_float - full_stars >= 0.25 and rating_float - full_stars < 0.99
        stars = "⭐" * full_stars
        if half_star:
            stars += "⯪"
        total_stars = full_stars + (1 if half_star else 0)
        empty_stars = 5 - total_stars
        stars += "☆" * empty_stars
        return f"{stars} ({rating_float:.2f})"
    except ValueError:
        return "N/A"

def format_yes_no(value):
    if isinstance(value, str):
        value = value.lower()
        if value in ['yes', 'true']:
            return "✅"
        elif value in ['no', 'false']:
            return "❌"
        elif value in ['partial', 'partially', 'limited']:
            return "⚠️"
    return value

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

    # Create the tools section with link to evaluated tools
    tools_section = [
        "## Evaluated Tools\n\n",
        "### List of Tools\n"
        "View our evaluated tools in a comprehensive list with detailed ratings and information:\n\n",
        "- [Complete List of Evaluated Tools](docs/tools/evaluated-tools.md)\n\n"
    ]

    # Generate the evaluated tools list
    os.makedirs("docs/tools", exist_ok=True)
    with open("docs/tools/evaluated-tools.md", "w") as f:
        f.write("# Evaluated Tools\n\n")
        f.write("| Tool Name | Category | Description | Status | Deployment | Technical Level | Documentation | Overall Rating | Last Tested |\n")
        f.write("|----------|-----------|-------------|---------|------------|-----------------|---------------|----------------|-------------|\n")
        
        # Only include tools that have been tested and approved
        evaluated_tools = [tool for tool in tools if "version-tested" in tool]
        
        for tool in evaluated_tools:
            tool_name = tool.get("tool-name", "Unknown Tool")
            tool_url = tool.get("tool-url", "#")
            category = tool.get("category", "Unknown Category")
            description = tool.get("description", "No description available.")
            status = tool.get("status", "Active")
            deployment = tool.get("deployment-architecture", "N/A")
            technical_level = tool.get("technical-level", "Unknown Technical Level")
            overall_rating = tool.get("overall-rating", "N/A")
            date_tested = tool.get("date-tested", "N/A")
            tool_name_safe = tool_name.lower().replace(" ", "-")
            
            # Construct documentation path
            doc_dir = f"docs/tools/categories/{category.lower().replace(' ', '-')}"
            doc_file = f"{doc_dir}/{tool_name_safe}.md"
            documentation_url = f"categories/{category.lower().replace(' ', '-')}/{tool_name_safe}.md"

            # Ensure the directory exists
            os.makedirs(doc_dir, exist_ok=True)

            # Create or update documentation file with all information from tools.json
            with open(doc_file, "w") as df:
                df.write(f"# {tool_name}\n\n")
                
                # Basic Information
                df.write("## Basic Information\n")
                df.write(f"- **Tool Name**: {tool.get('tool-name', 'N/A')}\n")
                df.write(f"- **Category**: {tool.get('category', 'N/A')}\n")
                df.write(f"- **URL**: {tool.get('tool-url', 'N/A')}\n")
                df.write(f"- **Description**: {tool.get('description', 'N/A')}\n")
                df.write(f"- **Status**: {tool.get('status', 'Active')}\n\n")
                
                # Core Features and Compatibility
                df.write("## Core Features and Compatibility\n")
                df.write(f"- **Core Features**: {tool.get('core-features', 'N/A')}\n")
                df.write(f"- **Operating Systems**: {tool.get('os-compatibility', 'N/A')}\n")
                df.write(f"- **Offline Functionality**: {format_yes_no(tool.get('offline-functionality', 'N/A'))}\n")
                df.write(f"- **Mobile Support**: {format_yes_no(tool.get('mobile-friendly', 'N/A'))}\n")
                df.write(f"- **Languages Supported**: {tool.get('languages-supported', 'N/A')}\n")
                df.write(f"- **Technical Level**: {tool.get('technical-level', 'N/A')}\n\n")
                
                # Security and Privacy
                df.write("## Security and Privacy\n")
                df.write(f"- **Security Features**: {tool.get('security-privacy-features', 'N/A')}\n")
                df.write(f"- **Data Collection Level**: {tool.get('data-collection-level', 'N/A')}\n")
                df.write(f"- **Security and Privacy Rating**: {format_star_rating(tool.get('security-privacy-strength-rating', 'N/A'))}\n\n")
                
                # Deployment and Technical Details
                df.write("## Deployment and Technical Details\n")
                df.write(f"- **Deployment Architecture**: {tool.get('deployment-architecture', 'N/A')}\n")
                df.write(f"- **License**: {tool.get('license', 'N/A')}\n")
                df.write(f"- **Cost**: {tool.get('cost', 'N/A')}\n\n")
                
                # Maintenance and Support
                df.write("## Maintenance and Support\n")
                df.write(f"- **Maintenance Status**: {tool.get('maintenance-sustainability', 'N/A')}\n")
                df.write(f"- **Community Support**: {format_yes_no(tool.get('community-support', 'N/A'))}\n")
                df.write(f"- **Maintenance and Sustainability Rating**: {format_star_rating(tool.get('maintenance-sustainability-rating', 'N/A'))}\n\n")
                
                # Performance and Ratings
                df.write("## Performance and Ratings\n")
                df.write(f"- **Operational Functionality**: {format_star_rating(tool.get('operational-functionality-rating', 'N/A'))}\n")
                df.write(f"- **Usability**: {format_star_rating(tool.get('usability-rating', 'N/A'))}\n")
                df.write(f"- **Effectiveness and Reliability**: {format_star_rating(tool.get('effectiveness-reliability-rating', 'N/A'))}\n")
                df.write(f"- **Overall Rating**: {format_star_rating(tool.get('overall-rating', 'N/A'))}\n\n")
                
                # Documentation & Testing
                df.write("## Documentation & Testing\n")
                df.write(f"- **Full Documentation**: [{tool.get('tool-name', 'N/A')} Documentation]({tool.get('full-documentation', 'N/A')})\n")
                df.write(f"- **Version Tested**: {tool.get('version-tested', 'N/A')}\n")
                df.write(f"- **Date Tested**: {tool.get('date-tested', 'N/A')}\n")
                df.write(f"- **Testing Environment**: {tool.get('testing-environment', 'N/A')}\n\n")
                
                # Additional Information
                df.write("## Additional Information\n")
                df.write(f"- **Limitations and Vulnerabilities**: {tool.get('limitations-vulnerabilities', 'N/A')}\n")
                if tool.get('additional-notes'):
                    df.write(f"- **Additional Notes**: {tool.get('additional-notes')}\n\n")
                
                # Submission Information
                df.write("## Submission Information\n")
                df.write(f"- **Submitted By**: {tool.get('submitted_by', 'N/A')}\n")
                df.write(f"- **Submission Date**: {datetime.fromtimestamp(tool.get('date_submitted', 0)).strftime('%Y-%m-%d')}\n")
                df.write(f"- **Last Updated**: {datetime.fromtimestamp(tool.get('date_updated', 0)).strftime('%Y-%m-%d')}\n")

            # Add entry to evaluated tools list
            f.write(
                f"| [{tool_name}]({tool_url}) | {category} | {description} | {status} | {deployment} | {technical_level} | [Details]({documentation_url}) | {format_star_rating(overall_rating)} | {date_tested} |\n"
            )

    # Create comparisons README
    os.makedirs("docs/tools/comparisons", exist_ok=True)
    with open("docs/tools/comparisons/README.md", "w") as f:
        f.write("# Tool Comparisons by Category\n\n")
        # Get unique categories
        categories = sorted(set(tool.get("category") for tool in tools))
        for category in categories:
            category_safe = category.lower().replace(" ", "-")
            f.write(f"- [{category}]({category_safe}.md)\n")

    # Insert the updated tools section into the README
    updated_readme_content = (
        readme_content[:tools_section_start + 1] + tools_section + readme_content[tools_section_end:]
    )

    # Write the updated content back to README.md
    with open("README.md", "w") as f:
        f.writelines(updated_readme_content)

    print("✅ README.md updated successfully with links to evaluated tools.")

if __name__ == "__main__":
    update_readme()
