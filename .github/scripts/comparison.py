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
            stars += "⯪"  # Optional: fallback to "½" or "☆"
        total_stars = full_stars + (1 if half_star else 0)
        empty_stars = 5 - total_stars
        stars += "☆" * empty_stars
        return f"{stars} ({rating_float:.2f})"
    except ValueError:
        return "N/A"
        

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
        category_filename = 'comparisonOf' + category.replace(' ', '-') + 'Tools.md'
        category_filepath = f"docs/tools/{category_filename}"
        category_links.append(f"[{category}]({category_filepath})")

        # Generate HTML for the category
        category_html = []
        category_html.append(f"<h1>{category} Tools</h1>\n")
        category_html.append('<table border="1">\n')
        category_html.append(
            "<thead><tr>"
            "<th>🛠️ Tool Name</th>"
            "<th>📝 Desc</th>"
            "<th>📊 Status</th>"
            "<th>🚀 Deployment</th>"
            "<th>🤝 Community Support</th>"
            "<th>🧠 Tech Level</th>"
            "<th>✨ Features</th>"
            "<th>💻 OS</th>"
            "<th>📴 Offline</th>"
            "<th>📱 Mobile</th>"
            "<th>🌐 Languages</th>"
            "<th>🔐 Security/Privacy Features</th>"
            "<th>🔧 Maintenance/Sustainability</th>"
            "<th>📥 Data Collection</th>"
            "<th>🧾 License</th>"
            "<th>💰 Cost</th>"
            "<th>📚 Docs</th>"
            "<th>⭐ Rating</th>"
            "</tr></thead>\n"
        )
        category_html.append("<tbody>\n")

        for tool in tools_in_cat:
            tool_name = tool.get("tool_name", "Unknown")
            tool_url = tool.get("tool_url", "#")
            description = tool.get("description", "No description available.")
            status = tool.get("status", "N/A")
            deployment = ", ".join(tool.get("deployment", []))
            community_support = tool.get("community-support", "N/A")
            tech_level = tool.get("technical-level", "N/A")
            core_features = tool.get("core-features", "N/A")
            os_compatability = tool.get("os-compatibility", "N/A")
            offline_functionality = tool.get("offline-functionality", "N/A")
            mobile_friendly = tool.get("mobile-friendly", "N/A")
            languages_supported = tool.get("languages-supported", "N/A")
            security_and_privacy = tool.get("security-privacy-features", "N/A")
            maintenance_and_sustainability = tool.get("maintenance-sustainability", "N/A")
            data_collection_level = tool.get("data-collection-level", "N/A")
            license = tool.get("license", "N/A")
            cost = tool.get("cost", "N/A")
            overall_rating_raw = tool.get("overall-rating", "N/A")
            overall_rating = format_star_rating(overall_rating_raw)

            # Construct documentation path
            doc_dir = f"{category.lower().replace(' ', '-')}"
            doc_file = f"{doc_dir}/{tool_name.replace(' ', '-')}.md"
            doc_link = f"[Details]({doc_file})"

            os.makedirs(doc_dir, exist_ok=True)
            if not os.path.exists(doc_file):
                open(doc_file, "w").close()

            category_html.append(
                f"<tr>"
                f"<td><a href='{tool_url}'>{tool_name}</a></td>"
                f"<td>{description}</td>"
                f"<td>{status}</td>"
                f"<td>{deployment}</td>"
                f"<td>{community_support}</td>"
                f"<td>{tech_level}</td>"
                f"<td>{core_features}</td>"
                f"<td>{os_compatability}</td>"
                f"<td>{offline_functionality}</td>"
                f"<td>{mobile_friendly}</td>"
                f"<td>{languages_supported}</td>"
                f"<td>{security_and_privacy}</td>"
                f"<td>{maintenance_and_sustainability}</td>"
                f"<td>{data_collection_level}</td>"
                f"<td>{license}</td>"
                f"<td>{cost}</td>"
                f"<td><a href='{doc_file}'>Details</a></td>"
                f"<td>{overall_rating}</td>"
                f"</tr>\n"
            )

        category_html.append("</tbody>\n")
        category_html.append("</table>\n")

        # Write the category HTML to file
        print(category_filepath)
        with open(category_filepath, "w") as f:
            f.writelines(category_html)

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
