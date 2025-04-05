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
    lines = [line.strip("# ").strip() for line in re.split(r'[\n\r]+', body) if line.strip()]
    data = {
        "id": str(uuid.uuid4()),
        "date_updated": int(datetime.now().timestamp()),
        "submitted_by": username
    }

    try:
        data["tool_name"] = lines[1]
        data["tool_url"] = add_https_to_url(lines[3])
        data["category"] = lines[5]
        data["deployment"] = [d.strip() for d in lines[7].split(",")]
        data["description"] = lines[9]
        data["target_users"] = lines[11]
        data["testing_status"] = lines[13]

        checklist_start = 15
        checklist = []
        while lines[checklist_start].startswith("- ["):
            if "[x]" in lines[checklist_start].lower():
                checklist.append(lines[checklist_start][6:].strip())
            checklist_start += 1
        data["evaluation_checklist"] = checklist

        data["additional_notes"] = "\n".join(lines[checklist_start:]) if checklist_start < len(lines) else ""

        email_line = lines[checklist_start - 1].lower() if checklist_start - 1 < len(lines) else "no response"
        if "no response" not in email_line:
            util.setOutput("commit_email", email_line)
            util.setOutput("commit_username", username)
        else:
            util.setOutput("commit_email", "action@github.com")
            util.setOutput("commit_username", "GitHub Action")

    except IndexError as e:
        util.fail(f"Error parsing submission: {e}")

    return data


def get_commit_text(tool):
    return f"{tool['tool_name']} ({tool['category']})"


def main():
    event_file_path = sys.argv[1]
    with open(event_file_path) as f:
        event_data = json.load(f)

    is_new = "new-tool" in [label["name"] for label in event_data["issue"]["labels"]]
    is_edit = "edit-tool" in [label["name"] for label in event_data["issue"]["labels"]]

    if not is_new and not is_edit:
        util.fail("Only new-tool and edit-tool issues can be approved.")

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
