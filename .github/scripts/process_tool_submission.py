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


def parse_tool_body(body, is_edit, username, is_submission):
    sections = {}
    current_section = None
    print(body)

    for line in body.splitlines():
        line = line.strip()
        if line.startswith("### "):  # New section
            current_section = line[4:].strip()
            sections[current_section] = []
        elif current_section:
            sections[current_section].append(line)

    data = {
        "id": str(uuid.uuid4()),
        "date_updated": int(datetime.now().timestamp()),
        "submitted_by": username
    }

    def get_value(key):
        # First try to get by ID
        if key in sections:
            return "\n".join(sections[key]).strip()
        # Then try by label if ID not found
        label_key = key.replace("-", " ").title()
        return "\n".join(sections.get(label_key, [])).strip()

    # Basic Information
    data["tool-name"] = get_value("tool-name")
    tool_url = get_value("tool-url")
    if tool_url:  # Only set if we actually got a URL
        data["tool-url"] = add_https_to_url(tool_url)
    data["category"] = get_value("category")
    data["description"] = get_value("description")
    data["status"] = get_value("status")

    # Core Features & Compatibility
    data["core-features"] = get_value("core-features")
    data["os-compatibility"] = get_value("os-compatibility")
    data["offline-functionality"] = get_value("offline-functionality")
    data["mobile-friendly"] = get_value("mobile-friendly")
    data["languages-supported"] = get_value("languages-supported")
    data["technical-level"] = get_value("technical-level")

    # Security & Privacy
    data["security-privacy-features"] = get_value("security-privacy-features")
    data["data-collection-level"] = get_value("data-collection-level")
    data["security-privacy-strength-rating"] = get_value("security-privacy-rating")

    # Deployment & Technical
    data["deployment-architecture"] = get_value("deployment-architecture")
    data["license"] = get_value("license")
    data["cost"] = get_value("cost")

    # Maintenance & Support
    data["maintenance-sustainability"] = get_value("maintenance-sustainability")
    data["community-support"] = get_value("community-support")
    data["maintenance-sustainability-rating"] = get_value("maintenance-sustainability-rating")

    # Performance & Ratings
    data["operational-functionality-rating"] = get_value("operational-functionality-rating")
    data["usability-rating"] = get_value("usability-rating")
    data["effectiveness-reliability-rating"] = get_value("effectiveness-reliability-rating")
    data["overall-rating"] = get_value("overall-rating")

    # Documentation & Testing
    data["full-documentation"] = get_value("full-documentation")
    data["version-tested"] = get_value("version-tested")
    data["date-tested"] = get_value("date-tested")
    data["testing-environment"] = get_value("testing-environment")

    # Additional Information
    data["limitations-vulnerabilities"] = get_value("limitations-vulnerabilities")
    data["additional-notes"] = get_value("additional-notes")

    # Submission metadata
    if not is_edit:
        data["date_submitted"] = int(datetime.now().timestamp())

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

    # Must have 'approved' AND be a tool-submission
    if not is_approved or not is_submission:
        fail("Only approved tool-submission issues can be processed.")

    # Tool suggestions are not processed yet
    if is_suggestion:
        fail("Tool suggestions cannot be processed yet as the feature is not implemented.")

    issue_body = event_data["issue"]["body"]
    issue_user = event_data["issue"]["user"]["login"]
    tool_data = parse_tool_body(issue_body, is_edit=False, username=issue_user, is_submission=True)

    # Load tools list
    with open(".github/scripts/tools.json", "r") as f:
        tools = json.load(f)

    # Check for existing tool only if we have a URL
    existing_tool = None
    if "tool-url" in tool_data:
        existing_tool = next((t for t in tools if t.get("tool-url") == tool_data["tool-url"]), None)

    if existing_tool:
        fail("This tool already exists. Submit an edit instead.")
    else:
        tool_data["date_submitted"] = int(datetime.now().timestamp())
        tools.append(tool_data)
        set_output("commit_message", "added tool: " + get_commit_text(tool_data))

    with open(".github/scripts/tools.json", "w") as f:
        f.write(json.dumps(tools, indent=4))


if __name__ == "__main__":
    main()
