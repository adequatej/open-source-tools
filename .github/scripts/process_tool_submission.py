# Script for approving tools 

import json
import sys
import uuid
from datetime import datetime
import re
import os


def add_https_to_url(url):
    if not url.startswith(("http://", "https://")):
        return f"https://{url}"
    return url


def set_output(name, value):
    with open(os.environ['GITHUB_OUTPUT'], 'a') as fh:
        print(f'{name}={value}', file=fh)


def fail(message):
    set_output("error_message", message)
    sys.exit(1)


def parse_tool_body(body, is_edit, username):
    sections = {}
    current_section = None
    checklist = []
    additional_notes = []

    for line in body.splitlines():
        line = line.strip()
        if line.startswith("### "):  # New section
            current_section = line[4:].strip()
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
        return "\n".join(sections.get(key, [])).strip()

    # Basic tool information
    data["tool-name"] = get_value("Tool Name")
    tool_url = get_value("Tool URL")
    if tool_url:  # Only set if we actually got a URL
        data["tool-url"] = add_https_to_url(tool_url)
    data["category"] = get_value("Category")
    data["description"] = get_value("Description")

    # Submission type specific fields
    submission_type = get_value("Submission Type")
    if "I have completed testing" in submission_type:
        # Fields for tested tools
        data["version-tested"] = get_value("Version Tested")
        data["testing-environment"] = get_value("Testing Environment")
        data["testing-documentation"] = get_value("Testing Documentation")
        data["evaluation-checklist"] = [
            re.sub(r"^- \[.\] ?", "", item).strip()
            for item in checklist if "[x]" in item.lower()
        ]
        # Fields for evaluated tools list
        data["status"] = "Active"  # All approved tools are active
        data["deployment-type"] = [d.strip() for d in get_value("Deployment Type").split(",")]
        data["technical-level"] = get_value("Technical Level")
        data["overall-rating"] = get_value("Overall Rating")
    else:
        # Fields for suggested tools
        data["why-valuable"] = get_value("Why is this tool valuable?")
        data["similar-tools"] = get_value("Similar Tools")
        data["known-limitations"] = get_value("Known Limitations")
        data["existing-documentation"] = get_value("Documentation")
        data["interest-in-testing"] = get_value("Interest in Testing")

    # Common fields
    data["additional-notes"] = get_value("Additional Notes")

    # Guess email
    last_lines = body.strip().splitlines()[-5:]
    for line in last_lines:
        if "@" in line and "." in line:
            set_output("commit_email", line.strip())
            set_output("commit_username", username)
            break
    else:
        set_output("commit_email", "action@github.com")
        set_output("commit_username", "GitHub Action")

    return data


def get_commit_text(tool):
    return f"{tool['tool-name']} ({tool['category']})"


def main():
    event_file_path = sys.argv[1]
    with open(event_file_path) as f:
        event_data = json.load(f)

    labels = [label["name"].lower() for label in event_data["issue"]["labels"]]

    is_submission = "tool-submission" in labels
    is_suggestion = "tool-suggestion" in labels
    is_approved = "approved" in labels

    # Must have 'approved' AND either 'tool-submission' or 'tool-suggestion'
    if not is_approved or not (is_submission or is_suggestion):
        fail("Only approved tool-submission or tool-suggestion issues can be processed.")

    issue_body = event_data["issue"]["body"]
    issue_user = event_data["issue"]["user"]["login"]
    tool_data = parse_tool_body(issue_body, is_edit=False, username=issue_user)

    # Load tools list
    with open(".github/scripts/tools.json", "r") as f:
        tools = json.load(f)

    # Check for existing tool only if we have a URL
    existing_tool = None
    if "tool-url" in tool_data:
        existing_tool = next((t for t in tools if t.get("tool-url") == tool_data["tool-url"]), None)

    if existing_tool:
        if is_submission:
            fail("This tool already exists. Submit an edit instead.")
        existing_tool.update(tool_data)
        set_output("commit_message", "updated tool: " + get_commit_text(existing_tool))
    else:
        if is_suggestion and "tool-url" in tool_data:
            fail("This tool was not found. Make sure the tool URL matches.")
        tool_data["date_submitted"] = int(datetime.now().timestamp())
        tools.append(tool_data)
        set_output("commit_message", "added tool: " + get_commit_text(tool_data))

    with open(".github/scripts/tools.json", "w") as f:
        f.write(json.dumps(tools, indent=4))


if __name__ == "__main__":
    main()
