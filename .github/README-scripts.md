# Understanding Repository Automation

This document explains how the automated processes work in this repository, including issue templates and GitHub Actions.

## GitHub Issue Templates

Our repository uses issue templates to standardize submissions. These can be found in `.github/ISSUE_TEMPLATE/`:

| Template | Filename | Purpose | Initial Labels |
|----------|----------|---------|----------------|
| New Tool | `new_tool.yml` | Submit a new tool for evaluation | `new-tool`, `needs-review` |

## Tool Approval Process

When a new tool is submitted through the issue template, it follows this automated workflow:

1. **Issue Creation**
   - User fills out the new tool template
   - Issue is automatically labeled with `new-tool` and `needs-review`
   - Maintainers are notified

2. **Review Process**
   - Maintainers review the submission
   - Community can provide feedback
   - Tool is evaluated according to criteria in CONTRIBUTING.md

3. **Approval Automation**
   When a maintainer adds the `approved` label:
   - GitHub Action is triggered
   - Tool information is extracted from the issue
   - Documentation is generated (*decide later if we want this or users to just their own docs upon PR request*)
   - Tool is added to the listings
   - Issue is automatically closed

## GitHub Actions

### Tool Approval Action

The "Tool Approved" action (`tool_approved.yml`) handles the automation when a tool is approved:

**Trigger:**
- Runs when a label is added to an issue
- Only processes issues with the `approved` label

**Process Steps:**
1. **Repository Setup**
   - Checkout repository
   - Set up Python environment

2. **Data Processing**
   - Extract issue form data
   - Validate tool information
   - Generate documentation from template
   - Update tool listings

3. **Repository Updates**
   - Commit changes
   - Credit contributor (if email provided)
   - Push updates
   - Close issue

4. **Error Handling**
   - If any step fails, error is posted to issue
   - Maintainers are notified of failures
   - Process can be manually retriggered

## Error Handling

If the automation encounters any issues:
1. The error message is posted as a comment on the issue
2. The process stops at the failed step
3. Maintainers can review logs in the Actions tab
4. Process can be manually restarted after fixes

## Contributing to the Scripts

If you want to improve these automation scripts:
1. Check the existing code in `.github/workflows/`
2. Test changes in a development branch
3. Submit a PR with detailed explanation of changes
4. Include testing results and error handling considerations
