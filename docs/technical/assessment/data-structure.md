# Data Structure Documentation

This document outlines the data structure used for tool submissions and evaluations in our repository.

## Overview

Tools are stored in a JSON array where each tool is represented by an object containing various fields that describe its features, capabilities, and evaluation results.

## Field Descriptions

### Metadata
- `id` (string): Unique identifier for the tool
- `date_submitted` (integer): Unix timestamp of initial submission
- `date_updated` (integer): Unix timestamp of last update
- `submitted_by` (string): GitHub username of the submitter

### Basic Information
- `tool-name` (string): Name of the tool
- `tool-url` (string): Official website or repository URL
- `category` (string): Tool category (e.g., Browser, Password Management)
- `description` (string): Brief description of the tool's purpose
- `status` (string): Current status (Active, Inactive, Experimental)

### Core Features & Compatibility
- `core-features` (string): Comma-separated list of main features
- `os-compatibility` (string): Supported operating systems
- `offline-functionality` (string): "Yes", "No", or "Partially"
- `mobile-friendly` (string): "Yes", "No", or "Partially"
- `languages-supported` (string): Supported languages
- `technical-level` (string): Required technical expertise (Beginner, Intermediate, Advanced)

### Security & Privacy
- `security-privacy-features` (string): Key security and privacy features
- `data-collection-level` (string): "None", "Minimal", or "Extensive"
- `security-privacy-strength-rating` (string): Rating from 1-5

### Deployment & Technical
- `deployment-architecture` (string): How the tool is deployed
- `license` (string): License type (SPDX identifier preferred)
- `cost` (string): "Fully Free", "Free Core", "Subscription Model", "One-time Purchase"

### Maintenance & Support
- `maintenance-sustainability` (string): Description of maintenance status and funding
- `community-support` (string): "Yes", "No", or "Limited"
- `maintenance-sustainability-rating` (string): Rating from 1-5

### Performance & Ratings
- `operational-functionality-rating` (string): Rating from 1-5
- `usability-rating` (string): Rating from 1-5
- `effectiveness-reliability-rating` (string): Rating from 1-5
- `overall-rating` (string): Weighted average of all ratings

### Documentation & Testing
- `full-documentation` (string): URL to complete documentation
- `version-tested` (string): Version number tested
- `date-tested` (string): Date of testing (YYYY-MM-DD)
- `testing-environment` (string): Description of testing environment

### Additional Information
- `limitations-vulnerabilities` (string): Known limitations or security concerns

## Example JSON

```json
{
    "id": "example-id-123",
    "date_submitted": 1744747334,
    "date_updated": 1744750500,
    "submitted_by": "username",
    "tool-name": "Example Tool",
    "tool-url": "https://example.com",
    "category": "Browser",
    "description": "A privacy-focused web browser",
    "status": "Active",
    "core-features": "Feature 1, Feature 2, Feature 3",
    "os-compatibility": "Windows, Linux, macOS",
    "offline-functionality": "Yes",
    "mobile-friendly": "Yes",
    "languages-supported": "English, Spanish, French",
    "technical-level": "Beginner",
    "security-privacy-features": "Feature A, Feature B",
    "data-collection-level": "Minimal",
    "security-privacy-strength-rating": "4.5",
    "deployment-architecture": "Desktop Application",
    "license": "MIT",
    "cost": "Fully Free",
    "maintenance-sustainability": "Regular updates, community-funded",
    "community-support": "Yes",
    "maintenance-sustainability-rating": "4.0",
    "operational-functionality-rating": "4.2",
    "usability-rating": "4.3",
    "effectiveness-reliability-rating": "4.4",
    "overall-rating": "4.3",
    "full-documentation": "https://docs.example.com",
    "version-tested": "1.0.0",
    "date-tested": "2024-03-21",
    "testing-environment": "Windows 11, macOS 14.2",
    "limitations-vulnerabilities": "Limited to specific use cases"
}
```

## Notes

1. All ratings are on a scale of 1-5, with higher numbers being better
2. Dates should be in YYYY-MM-DD format
3. URLs should include the protocol (https://)
4. The overall rating is calculated as a weighted average of individual ratings
5. All fields are required unless explicitly marked as optional
