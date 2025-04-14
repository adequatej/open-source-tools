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

    # Find the '### Compare Tools' section
    compare_idx = None
    for idx, line in enumerate(readme_content):
        if line.strip().startswith("### Compare Tools"):
            compare_idx = idx
            break

    if compare_idx is None:
        print("Error: '### Compare Tools' section not found in README.md.")
        sys.exit(1)

    # Find <!-- BEGIN TOOLS --> and <!-- END TOOLS --> after 'Compare Tools'
    begin_idx = end_idx = None
    for idx in range(compare_idx, len(readme_content)):
        line = readme_content[idx]
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

    # Create category markdown files
    category_links = []
    for category, tools_in_cat in grouped_by_category.items():
        # Create category-specific markdown file
        category_filename = category.lower().replace(' ', '-') + '.md'
        category_filepath = f"docs/comparisonOfTools/{category_filename}"
        category_links.append(f"[{category}]({category_filepath})")

        # Generate markdown for the category
        category_markdown = []
        category_markdown.append(f"# {category} Tools\n")
        category_markdown.append("| Tool Name | Description | Status | Deployment | Tech Level | Docs |\n")
        category_markdown.append("|-----------|-------------|--------|------------|------------|------|\n")

        for tool in tools_in_cat:
            tool_name = tool.get("tool_name", "Unknown")
            tool_url = tool.get("tool_url", "#")
            description = tool.get("description", "No description available.")
            status = "Active"
            deployment = ", ".join(tool.get("deployment", []))
            tech_level = tool.get("technical-level", "N/A")

            # Construct documentation path
            doc_dir = f"docs/comparisonOfTools/{category.lower().replace(' ', '-')}"
            doc_file = f"{doc_dir}/{tool_name.replace(' ', '-')}.md"
            doc_link = f"[Details]({doc_file})"

            os.makedirs(doc_dir, exist_ok=True)
            if not os.path.exists(doc_file):
                with open(doc_file, "w").close()

            if not os.path.exists(doc_file):
                open(doc_file, "w").close()  # Create the file and close it immediately without writing content
                print(f"File created: {doc_file}")  # Print a message confirming the file creation
            else:
                print(f"File already exists: {doc_file}")  # If the file already exists, print this message

            category_markdown.append(
                f"| [{tool_name}]({tool_url}) | {description} | {status} | {deployment} | {tech_level} | {doc_link} |\n"
            )

        # Write the category markdown to file
        print(category_filepath)
        with open(category_filepath, "w") as f:
            f.writelines(category_markdown)

    # Prepare links in the README to the new category pages
    links_section = ["### Compare Tools\n"]
    links_section.append("For a comparison of tools by categories, visit the respective category pages below:\n")
    for link in category_links:
        links_section.append(f"- {link}\n")

    # Replace content in README between the markers
    new_readme = (
        readme_content[:begin_idx + 1] +
        links_section +
        readme_content[end_idx:]
    )

    with open("README.md", "w") as f:
        f.writelines(new_readme)

    print("✅ README.md and category pages successfully updated.")

if __name__ == "__main__":
    update_readme()
