# Script for approving tools 

import json
import sys
import uuid
from datetime import datetime
import re
import util  # assumes you have a `util.py` with `setOutput()` and `fail()` like in your internship script


def add_https_to_url(url):
    if not url.startswith(("http://", "https://")):
        return f"https://{url}"
    return url


def parse_tool_body(body, is_edit, username):
    sections = {}
    current_section = None
    checklist = []
    additional_notes = []

    for line in body.splitlines():
        line = line.strip()
        if line.startswith("### "):  # New section
            current_section = line[4:].strip().lower()
            sections[current_section] = []
        elif current_section:
            if line.startswith("- ["):
                checklist.append(line)
            else:
                sections[current_section].append(line)

    data = {
        "id": str(uuid.uuid4()),
        "date_updated": int(datetime.now().timestamp()),
        "submitted_by": username
    }

    def get_value(key):
        return "\n".join(sections.get(key.lower(), [])).strip()

    data["tool_name"] = get_value("Tool Name")
    data["tool_url"] = add_https_to_url(get_value("Tool URL"))
    data["category"] = get_value("Category")
    data["deployment"] = [d.strip() for d in get_value("Deployment Type").split(",")]
    data["description"] = get_value("Description")
    data["target_users"] = get_value("Target Users")
    data["testing_status"] = get_value("Testing Status")

    data["evaluation_checklist"] = [
        re.sub(r"^- \[.\] ?", "", item).strip()
        for item in checklist if "[x]" in item.lower()
    ]

    # Additional notes is usually the last section
    if "additional notes" in sections:
        data["additional_notes"] = get_value("Additional Notes")
    else:
        data["additional_notes"] = ""

    # Guess email
    last_lines = body.strip().splitlines()[-5:]
    for line in last_lines:
        if "@" in line and "." in line:
            util.setOutput("commit_email", line.strip())
            util.setOutput("commit_username", username)
            break
    else:
        util.setOutput("commit_email", "action@github.com")
        util.setOutput("commit_username", "GitHub Action")

    return data



def get_commit_text(tool):
    return f"{tool['tool_name']} ({tool['category']})"


def main():
    event_file_path = sys.argv[1]
    with open(event_file_path) as f:
        event_data = json.load(f)

    labels = [label["name"].lower() for label in event_data["issue"]["labels"]]

    is_new = "new-tool" in labels
    is_edit = "edit-tool" in labels
    is_approved = "approved" in labels

    # Must have 'approved' AND either 'new-tool' or 'edit-tool'
    if not is_approved or not (is_new or is_edit):
        util.fail("Only approved new-tool or edit-tool issues can be processed.")

    issue_body = event_data["issue"]["body"]
    issue_user = event_data["issue"]["user"]["login"]
    tool_data = parse_tool_body(issue_body, is_edit, issue_user)

    # Load tools list
    with open(".github/scripts/tools.json", "r") as f:
        tools = json.load(f)

    if existing_tool := next((t for t in tools if t["tool_url"] == tool_data["tool_url"]), None):
        if is_new:
            util.fail("This tool already exists. Submit an edit instead.")
        existing_tool.update(tool_data)
        util.setOutput("commit_message", "updated tool: " + get_commit_text(existing_tool))
    else:
        if is_edit:
            util.fail("This tool was not found. Make sure the tool URL matches.")
        tool_data["date_submitted"] = int(datetime.now().timestamp())
        tools.append(tool_data)
        util.setOutput("commit_message", "added tool: " + get_commit_text(tool_data))

    with open(".github/scripts/tools.json", "w") as f:
        f.write(json.dumps(tools, indent=4))


if __name__ == "__main__":
    main()