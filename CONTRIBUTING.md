# Contributing to OCF x WPI Open Source Tools

Thank you for your interest in contributing to our open source tools collection! This document provides guidelines and instructions for contributing.

## Types of Contributions

### 1. Tool Submissions
- Submit open source tools that align with our mission
- Tools must be well-documented and maintained
- Must include all required information in the submission template

### 2. Documentation Improvements
- Enhance existing tool documentation
- Fix typos or unclear instructions
- Add usage examples or tutorials

### 3. Bug Reports
- Report issues with listed tools
- Provide clear reproduction steps
- Include system information when relevant

### 4. Feature Suggestions
- Propose new features for listed tools
- Suggest improvements to the repository structure
- Recommend new categories or tags

## Tool Submission Requirements

### Required Information
- Tool name and description
- Source code repository link
- Documentation/website link (if available)
- Installation instructions
- Usage examples
- License information
- Maintenance status
- Categories and tags

### Quality Standards
1. **Documentation**
   - Clear and comprehensive README
   - Installation instructions
   - Usage examples
   - API documentation (if applicable)

2. **Code Quality**
   - Well-structured and readable code
   - Appropriate comments and documentation
   - Tests (if applicable)
   - No security vulnerabilities

3. **Maintenance**
   - Active maintenance or clear maintenance status
   - Issue tracking enabled
   - Clear contribution guidelines

## Submission Process

1. **Initial Submission**
   - Create a new issue using the "New Tool Submission" template
   - Provide basic tool information (name, URL, category)
   - Describe deployment method and requirements
   - Explain target users and use cases

2. **Initial Review**
   - OCF/WPI team reviews the submission
   - Assess if tool meets basic criteria:
     - Open source
     - Active maintenance
     - Clear documentation
     - Appropriate license
   - Determine if tool warrants full evaluation
   cases

3. **Evaluation Phase**
   - Install and test the tool
   - Document installation process
   - Test with both technical and non-technical users
   - Assess security implications
   - Evaluate accessibility and usability
   - Compare with similar tools
   - Document any issues or limitations

4. **Documentation Creation**
   - Create a new branch: `tools/your-tool-name`
   - Add tool documentation in `docs/tools/$category$/tool-name.md`
   - Include:
     - Installation guide
     - Usage instructions
     - Test results
     - Security assessment
     - User feedback
     - Screenshots/examples

5. **Final Review & Integration**
   - Submit pull request with documentation
   - Team reviews documentation completeness
   - Community feedback period
   - Make requested revisions
   - Tool is added to the list upon approval


Note: This is an iterative process focused on thorough evaluation and documentation. The goal is to provide 
comprehensive, reliable information about each tool's usability, security, and effectiveness for both 
technical and non-technical users.


## Review Process

*not a complete/comprehensive process yet, but will be refined as we test*

1. **Initial Check**
   - All required information provided
   - Meets basic quality standards
   - Appropriate categorization

2. **Technical Review**
   - Code quality assessment
   - Security check
   - Documentation review

3. **Community Feedback**
   - Community members can comment
   - Suggestions for improvements
   - Use case validation

4. **Final Approval**
   - OCF/WPI team approval
   - Automatic integration
   - README update

## New tool approval
For a more in-depth perspective on how our automation and approval process works, look [here](.github/README-scripts.md).

### When issue is labeled "approved":
1. GitHub Action triggers
2. Script reads issue form data
3. Extracts tool information
4. Updates tool listing
5. Generates documentation
6. Commits changes
7. Closes issue

General:
You'll need a GitHub Action workflow that:
Triggers when a label is added to an issue
Checks if the label is "approved"
If approved, processes the issue form data.

## Style Guidelines

### Documentation
- Use clear, concise language
- Include code examples when relevant
- Follow markdown best practices
- Keep formatting consistent

### Metadata
- Use appropriate categories and tags 
- Keep descriptions informative but brief
- Include all required links
- Update timestamps when needed

## Need Help?
- Check existing issues
- Join our community chat (*coming soon*) 
- Contact maintainers
- Review existing submissions

## Questions?

If you have questions about contributing, please:
1. Check existing issues
2. Create a new issue with the label `question`
3. Contact the maintainers

Thank you for contributing to making open source tools more accessible and useful for everyone!
