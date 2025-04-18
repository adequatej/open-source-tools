# Understanding Repository Automation

## Table of Contents
1. [Overview](#overview)
2. [GitHub Issue Templates](#github-issue-templates)
3. [Tool Approval Process](#tool-approval-process)
   - [Initial Submission](#1-initial-submission)
   - [Review Process](#2-review-process)
   - [Automation](#3-automation)
4. [GitHub Action Workflow](#github-action-workflow)
   - [Process Steps](#process-steps)
   - [Scripts](#scripts)
5. [Error Handling](#error-handling)
6. [Contributing to Scripts](#contributing-to-scripts)
   - [Testing Locally](#testing-locally)
7. [Need Help?](#need-help)

## Overview

The repository uses a combination of GitHub Issue Templates and GitHub Actions to automate the tool submission and approval process. 

## GitHub Issue Templates

Our repository uses standardized issue templates located in `.github/ISSUE_TEMPLATE/`:

| Template | Filename | Purpose | Initial Labels |
|----------|----------|---------|----------------|
| New Tool | `new_tool.yml` | Submit a new tool for evaluation | `new-tool`, `needs-review` |

**To Edit Tool, simply change label from 'new-tool' to 'edit-tool'

## Tool Approval Process

### 1. Initial Submission
- User fills out the new tool template
- Issue is automatically labeled with `new-tool` and `needs-review`
- Maintainers are notified of the new submission
- If tool already exists in the toolkit/list, change label 'new-tool' to 'edit-tool' while keeping 'needs-review' label as well

### 2. Review Process
- Maintainers review the submission
- Community can provide feedback
- Tool is evaluated according to criteria in CONTRIBUTING.md
- If approved, the `approved` label is added and 'needs-review' label is removed

### 3. Automation
When the `approved` label is added, the automation process begins:
1. GitHub Action triggers
2. Script reads issue form data
3. Extracts tool information
4. Updates tool listing
5. Generates documentation
6. Commits changes
7. Closes issue

## GitHub Action Workflow

The `tool_approved_with_readme_updates.yml` workflow handles the entire automation process in one go:

### Process Steps

1. **Repository Setup**
   - Checks out the repository
   - Sets up Python environment
   - Configures git user

2. **Tool Processing**
   - Runs `process_tool_submission.py`
   - Validates tool data
   - Updates `tools.json`

3. **README Update**
   - Runs `update_readme.py`
   - Updates the tools table in README.md
   - Maintains proper formatting

4. **Repository Update**
   - Commits both `tools.json` and `README.md` changes
   - Pushes changes to the main branch
   - GitHub Action bot closes the issue automatically

### Scripts

Two main Python scripts handle the automation:

1. **`process_tool_submission.py`**
   - Processes the issue form data
   - Validates required fields
   - Updates `tools.json`
   - Handles both new tools and edits

2. **`update_readme.py`**
   - Reads the updated `tools.json`
   - Updates the tools table in README.md
   - Maintains proper formatting and structure

## Error Handling

If any part of the process fails:
1. The workflow stops
2. No changes are pushed
3. A comment is added to the issue with error details
4. The issue remains open for maintainer review

## Contributing to Scripts

To improve these automation scripts:
1. Fork the repository
2. Make your changes
3. Test thoroughly with sample issues
4. Submit a PR with your improvements

### Testing Locally

You can test the scripts locally:
```bash
# Test tool processing
python .github/scripts/process_tool_submission.py test_event.json

# Test README update
python .github/scripts/update_readme.py
```

## Need Help?

If you encounter issues:
1. Check the workflow run logs
2. Look for error messages in the issue comments
3. Contact the maintainers for assistance
