import json
import sys
import os
from collections import defaultdict

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
    # Load tools from file
    try:
        with open(".github/scripts/tools.json", "r") as f:
            tools = json.load(f)
    except FileNotFoundError:
        print("Error: tools.json file not found.")
        sys.exit(1)

    # Group tools by category
    grouped_by_category = defaultdict(list)
    for tool in tools:
        grouped_by_category[tool.get("category", "Uncategorized")].append(tool)

    # Create category markdown files and build comparison README content
    os.makedirs("docs/tools/comparisons", exist_ok=True)
    
    # Create the main comparison README
    comparison_readme = [
        "# Tool Comparisons by Category\n\n",
        "Our comparison pages help you make informed decisions by comparing tools within the same category. Each comparison includes:\n\n",
        "- Feature comparison matrices\n",
        "- Security and privacy analysis\n",
        "- Performance benchmarks\n",
        "- Usability ratings\n",
        "- Deployment requirements\n",
        "- Cost comparisons\n",
        "- Maintenance status\n\n",
        "## Available Categories\n\n"
    ]

    # Process each category
    for category, tools_in_cat in grouped_by_category.items():
        # Create category-specific markdown file
        category_filename = category.lower().replace(' ', '-') + '.md'
        category_filepath = f"docs/tools/comparisons/{category_filename}"
        comparison_readme.append(f"- [{category}]({category_filename})\n")

        # Generate markdown for the category
        category_markdown = []
        category_markdown.append(f"# {category} Tools Comparison\n")
        
        # Add overview section
        category_markdown.append("## Overview\n")
        category_markdown.append("Quick comparison of key features and ratings:\n\n")
        category_markdown.append("| Tool | Overall Rating | Cost | Technical Level | Key Features |\n")
        category_markdown.append("|------|----------------|------|-----------------|--------------|\n")
        
        for tool in tools_in_cat:
            tool_name = tool.get("tool-name", "Unknown")
            tool_url = tool.get("tool-url", "#")
            overall_rating = format_star_rating(tool.get("overall-rating", "N/A"))
            cost = tool.get("cost", "N/A")
            tech_level = tool.get("technical-level", "N/A")
            
            # Get key features (first 3 most important ones)
            core_features = tool.get("core-features", "").split(", ")[:3]
            key_features = ", ".join(core_features) if core_features else "N/A"
            
            category_markdown.append(
                f"| [{tool_name}]({tool_url}) | {overall_rating} | {cost} | {tech_level} | {key_features} |\n"
            )

        # Add platform support section
        category_markdown.append("\n## Platform Support\n")
        category_markdown.append("| Tool | Operating Systems | Mobile Support | Offline Use | Languages | Usability Rating |\n")
        category_markdown.append("|------|------------------|----------------|--------------|-----------|------------------|\n")
        
        for tool in tools_in_cat:
            tool_name = tool.get("tool-name", "Unknown")
            tool_url = tool.get("tool-url", "#")
            platforms = tool.get("os-compatibility", "N/A")
            mobile = format_yes_no(tool.get("mobile-friendly", "N/A"))
            offline = format_yes_no(tool.get("offline-functionality", "N/A"))
            languages = tool.get("languages-supported", "N/A")
            usability_rating = format_star_rating(tool.get("usability-rating", "N/A"))
            
            category_markdown.append(
                f"| [{tool_name}]({tool_url}) | {platforms} | {mobile} | {offline} | {languages} | {usability_rating} |\n"
            )

        # Add security and privacy section
        category_markdown.append("\n## Security & Privacy\n")
        category_markdown.append("| Tool | Security Features | Data Collection | License | Community Support | Security Rating |\n")
        category_markdown.append("|------|-------------------|-----------------|----------|------------------|----------------|\n")
        
        for tool in tools_in_cat:
            tool_name = tool.get("tool-name", "Unknown")
            tool_url = tool.get("tool-url", "#")
            security = tool.get("security-privacy-features", "N/A")
            data_collection = tool.get("data-collection-level", "N/A")
            license_info = tool.get("license", "N/A")
            community = format_yes_no(tool.get("community-support", "N/A"))
            security_rating = format_star_rating(tool.get("security-privacy-strength-rating", "N/A"))
            
            category_markdown.append(
                f"| [{tool_name}]({tool_url}) | {security} | {data_collection} | {license_info} | {community} | {security_rating} |\n"
            )

        # Add maintenance and deployment section
        category_markdown.append("\n## Maintenance & Deployment\n")
        category_markdown.append("| Tool | Deployment Type | Maintenance Status | Last Tested | Maintenance Rating |\n")
        category_markdown.append("|------|----------------|-------------------|-------------|-------------------|\n")
        
        for tool in tools_in_cat:
            tool_name = tool.get("tool-name", "Unknown")
            tool_url = tool.get("tool-url", "#")
            # Fix deployment type formatting
            deployment = tool.get("deployment-architecture", "N/A")
            if isinstance(deployment, list):
                deployment = ", ".join(deployment)
            maintenance = tool.get("maintenance-sustainability", "N/A")
            last_tested = tool.get("date-tested", "N/A")
            maintenance_rating = format_star_rating(tool.get("maintenance-sustainability-rating", "N/A"))
            
            category_markdown.append(
                f"| [{tool_name}]({tool_url}) | {deployment} | {maintenance} | {last_tested} | {maintenance_rating} |\n"
            )

        # Write the category markdown to file
        print(f"Creating comparison page: {category_filepath}")
        with open(category_filepath, "w") as f:
            f.writelines(category_markdown)

    # Write the main comparison README
    with open("docs/tools/comparisons/README.md", "w") as f:
        f.writelines(comparison_readme)

    print("✅ Comparison pages and README successfully updated.")

if __name__ == "__main__":
    update_readme()
