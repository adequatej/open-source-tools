# Tool Scoring System

This document outlines how tools are scored and rated in our repository.

## Scoring Metrics

These five categories contribute to the overall tool assessment score. Each category has sub-metrics with assigned weights, and the category score is calculated as a weighted average of its sub-metrics.

### 1. Operational Functionality (Weight: 10%)
| Sub-Metric                       | Data Type | Example Value |
|-----------------------------------------|----------|--------------|
| Functionality     | Integer (1-5) | 3 |
| Localization and Language Support         | Integer (1-5) | 5 |
| Mobile Accessibility      | Integer (1-5) | 2 |

### 2. Usability for Non-Technical Users (Weight: 25%)
| Sub-Metric                      |  Data Type | Example Value |
|---------------------------------|----------|--------------|
| Ease of installation/deployment |  Integer (1-5) | 3 |
| User onboarding experience      |  Integer (1-5) | 4 |
| Technical experience required   |  Integer (1-5) | 2 |

### 3. Security & Privacy Strength (Weight: 30%)
| Sub-Metric                      |  Data Type | Example Value |
|---------------------------------|----------|--------------|
| Encryption standards            | Integer (1-5) | 5 |
| Resilience against known threats| Integer (1-5) | 4 |
| Compliance with security best practices | Integer (1-5) | 3 |
| Data minimization               |  Integer (1-5) | 4 |
| Privacy policy transparency     |  Integer (1-5) | 5 |

### 4. Maintenance & Sustainability (Weight: 15%)
| Sub-Metric                      |  Data Type | Example Value |
|---------------------------------|----------|--------------|
| Active development              |  Integer (1-5) | 5 |
| Community support               |  Integer (1-5) | 3 |
| Funding & sponsorship           |  Integer (1-5) | 2 |

### 5. Performance Efficiency (Weight: 20%)
| Sub-Metric                      |  Data Type | Example Value |
|---------------------------------|----------|--------------|
| CSO Function                      | Integer (1-5)   | 4 |
| Relevance          |  Integer (1-5) | 3 |
| Effectiveness |  Integer (1-5) | 2 |

## Final Scoring Calculation

Each category is scored as a weighted average of its sub-metrics which are just simply added and divided by the number of sub-metrics for that category. The final tool score is then computed as a weighted sum of all five categories:

$$
\text{Final Score} = (0.10 \times \text{Operational Functionality}) + (0.25 \times \text{Usability}) + (0.30 \times \text{Security}) + (0.15 \times \text{Maintenance/Sustainability}) + (0.20 \times \text{Performance})
$$

We are planning to create a system that allows users to adjust weights dynamically on a webpage to find tools that match their specific needs. *Coming Soon!* 