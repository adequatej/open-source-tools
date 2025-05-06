# Understanding Repository Automation

## Table of Contents
1. [Overview](#overview)
2. [GitHub Issue Templates](#github-issue-templates)
3. [Tool Submission Workflow](#tool-submission-workflow)
   - [Initial Submission](#1-initial-submission)
   - [Review Process](#2-review-process)
   - [Automation](#3-automation)
4. [GitHub Action Details](#github-action-details)
   - [Workflow Steps](#workflow-steps)
   - [Scripts](#scripts)
5. [Error Handling](#error-handling)
6. [Contributing to Scripts](#contributing-to-scripts)
   - [Testing Locally](#testing-locally)
7. [Need Help?](#need-help)

## Overview

This repository uses GitHub Issues and Actions to automate the tool submission, review, and integration process. The automation helps maintain consistency and reduces manual work while ensuring quality standards.

## GitHub Issue Templates

We use two standardized issue templates in `.github/ISSUE_TEMPLATE/`:

| Template | Filename | Purpose | Initial Labels |
|----------|----------|---------|----------------|
| Tool Submission | `tool_submission.yml` | Submit a fully tested tool with complete assessment | `tool-submission`, `needs-review` |
| Tool Suggestion | `tool_suggestion.yml` | Suggest a tool for future evaluation | `tool-suggestion`, `needs-review` |

### Template Fields

#### Tool Submission Template
- Basic Information (name, URL, category, description, status)
- Core Features & Compatibility (features, OS support, offline functionality, mobile support)
- Security & Privacy (features, data collection, ratings)
- Deployment & Technical (architecture, license, cost)
- Maintenance & Support (sustainability, community support, ratings)
- Performance & Ratings (operational, usability, reliability, overall)
- Documentation & Testing (full documentation, version tested, test environment)
- Additional Information (limitations, notes)

#### Tool Suggestion Template
- Basic Information (name, URL, category, description)
- Value Proposition (why valuable, similar tools)
- Known Limitations
- Documentation Links
- Interest in Testing

## Tool Submission Workflow

### 1. Initial Submission
When a user submits a new tool:
- User chooses appropriate template (Submission or Suggestion)
- Fills out comprehensive assessment data (for Submissions)
- Issue is automatically labeled based on template type
- System performs initial validation checks

### 2. Review Process
During the review phase:
- Maintainers review submission completeness
- Community feedback is gathered
- Tool assessment is verified
- Additional information may be requested
- Upon approval, `approved` label is added

### 3. Automation
When a submission is approved:
1. GitHub Action workflow triggers on `approved` label
2. Tool data is extracted and validated
3. Documentation is automatically generated:
   - Tool details page
   - Category comparison updates
   - README updates
4. Changes are committed to the repository
5. Issue is automatically closed

## GitHub Action Details

### Workflow Steps

1. **Data Processing** (`process_tool_submission.py`)
   - Validates submission data
   - Processes tool information
   - Updates tools database
   - Handles metadata (timestamps, IDs)

2. **Documentation Generation** (`update_readme.py`)
   - Creates individual tool pages
   - Updates main tools list
   - Generates comparison tables
   - Updates README

3. **Category Comparisons** (`comparison.py`)
   - Creates category-specific comparisons
   - Generates comparison matrices
   - Updates comparison index

### Scripts

The automation uses three main Python scripts:

1. **`process_tool_submission.py`**
   - Processes issue form data
   - Validates required fields
   - Updates tools database
   - Handles tool metadata

2. **`update_readme.py`**
   - Generates tool documentation
   - Updates main README
   - Creates tool detail pages
   - Maintains documentation structure

3. **`comparison.py`**
   - Generates category comparisons
   - Creates comparison matrices
   - Formats ratings and metrics
   - Updates comparison pages

## Error Handling

If errors occur during automation:
1. Workflow execution stops
2. Error details are posted as issue comment
3. Issue remains open with `error` label
4. No partial changes are committed
5. Maintainers are notified

## Contributing to Scripts

To improve the automation:
1. Fork the repository
2. Make your changes
3. Test thoroughly using the local testing process
4. Submit a PR with your improvements

### Testing Locally

Test the automation scripts locally:
```bash
# Set up test environment
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Test tool processing
python .github/scripts/process_tool_submission.py --test

# Test README update
python .github/scripts/update_readme.py --test

# Test comparison generation
python .github/scripts/comparison.py --test
```

## Need Help?

If you encounter issues:
1. Check the Action workflow logs
2. Review error messages in issue comments
3. Check existing issues for similar problems
4. Create a new issue with `automation-help` label
5. Contact repository maintainers
