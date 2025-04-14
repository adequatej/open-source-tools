# Script for comparing tools based off category

import json
from collections import defaultdict

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
