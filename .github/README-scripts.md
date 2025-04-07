# Understanding Repository Automation

This document explains how the automated processes work in this repository, including issue templates, GitHub Actions, and the tool approval workflow.

## Overview

The repository uses a combination of GitHub Issue Templates and GitHub Actions to automate the tool submission and approval process. The automation is split into two main workflows:

1. **Tool Approval Workflow**: Handles the submission and approval of new tools
2. **README Update Workflow**: Keeps the README synchronized with the tools list

## GitHub Issue Templates

Our repository uses standardized issue templates located in `.github/ISSUE_TEMPLATE/`:

| Template | Filename | Purpose | Initial Labels |
|----------|----------|---------|----------------|
| New Tool | `new_tool.yml` | Submit a new tool for evaluation | `new-tool`, `needs-review` |

## Tool Submission Process

### 1. Initial Submission
- User fills out the new tool template
- Issue is automatically labeled with `new-tool` and `needs-review`
- Maintainers are notified of the new submission

### 2. Review Process
- Maintainers review the submission
- Community can provide feedback
- Tool is evaluated according to criteria in CONTRIBUTING.md

### 3. Approval Automation
When a maintainer adds the `approved` label:
- Tool Approval workflow is triggered
- Tool information is extracted from the issue
- Tool is added to `tools.json`
- Issue is automatically closed
- README Update workflow is automatically triggered

## GitHub Actions

### Tool Approval Action (`tool_approved.yml`)

This action handles the initial tool approval process:

**Trigger:**
- Runs when a label is added to an issue
- Only processes issues with the `approved` label

**Process Steps:**
1. **Repository Setup**
   - Checkout repository
   - Set up Python environment
   - Debug event data for troubleshooting

2. **Data Processing**
   - Extract issue form data using `process_tool_submission.py`
   - Validate tool information
   - Check for duplicate tools
   - Update `tools.json` with new tool data

3. **Repository Updates**
   - Commit changes with contributor attribution
   - Push updates to main branch
   - Close the issue with success message

4. **Error Handling**
   - If any step fails, post error to issue
   - Maintainers can review logs in Actions tab
   - Process can be manually retriggered

### README Update Action (`update_readme.yml`)

This action keeps the README synchronized with the tools list:

**Trigger:**
- Runs automatically when `tools.json` is updated
- Can be manually triggered if needed

**Process:**
1. **Repository Setup**
   - Checkout repository
   - Set up Python environment

2. **README Update**
   - Run `update_readme.py`
   - Update tools table
   - Maintain consistent formatting

3. **Commit Changes**
   - Get contributor info from last commit
   - Commit changes with proper attribution
   - Push updates to main branch

## Scripts

### `process_tool_submission.py`
- Extracts data from issue form
- Validates tool information
- Handles both new tools and updates
- Checks for duplicate tools
- Updates `tools.json`
- Sets up contributor attribution
- Generates commit messages

### `update_readme.py`
- Reads tool data from `tools.json`
- Updates the README tools table
- Maintains consistent formatting
- Handles tool categorization
- Preserves existing tool information
- Updates documentation links

## Error Handling

If the automation encounters any issues:

1. **Tool Approval Errors**
   - Invalid form data
   - Duplicate tool detection
   - JSON parsing errors
   - File access issues

2. **README Update Errors**
   - Missing tool data
   - Formatting issues
   - File access problems
   - Merge conflicts

3. **General Workflow Errors**
   - GitHub API issues
   - Permission problems
   - Network connectivity
   - Resource limitations

## Troubleshooting

Common issues and solutions:

1. **Tool Approval Issues**
   - Check if the issue has the correct labels
   - Verify the workflow file is in the correct location
   - Check GitHub Actions permissions
   - Review form data format

2. **README Update Issues**
   - Verify `tools.json` format
   - Check for merge conflicts
   - Ensure Python scripts have correct permissions
   - Check for file access issues

3. **Documentation Issues**
   - Check issue form data format
   - Verify template files exist
   - Review error logs in Actions tab
   - Check for missing required fields

4. **Contributor Attribution Issues**
   - Verify issue author information
   - Check commit history
   - Review GitHub token permissions

## Need Help?

If you encounter any issues with the automation:
1. Check the Actions tab for error logs
2. Review the issue comments for error messages
3. Contact the maintainers
4. Create an issue with the `bug` label
