# Open Source Tools

A curated collection of open source tools and resources developed through the collaboration between [Open Culture Foundation (OCF)](https://ocf.tw/en/) and [Worcester Polytechnic Institute (WPI)](https://www.wpi.edu/).

[![GitHub stars](https://img.shields.io/github/stars/adequatej/open-source-tools.svg?style=social&label=Star&maxAge=2592000)](https://github.com/adequatej/open-source-tools/stargazers/)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](CONTRIBUTING.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## About OCF

The Open Culture Foundation (OCF) is a non-profit organization dedicated to supporting and advancing open source software development, assessibility, security, and privacy.

## About WPI

Worcester Polytechnic Institute (WPI) is a technological university known for its innovative project-based curriculum and commitment to applying technology for social good. WPI's motto "Theory and Practice" reflects its dedication to combining academic excellence with practical application. 

## About WPI's collaboration with OCF

This collaboration between WPI and OCF represents a unique partnership aimed at fostering open source development, accessibility, privacy, and security for Civil Society Organizations in East Asia. Through this initiative, WPI students survey, test, develop, and maintain a list of open source tools that benefit the broader technology community, with a focus on:

- Evaluating usability for both technical and non-technical users
- Assessing security and privacy implications
- Testing deployment and maintenance requirements
- Providing comprehensive documentation and guides
- Suggesting alternatives when appropriate

### Quick Links
- [Contributing Guidelines](CONTRIBUTING.md)
- [Tool Submission Process](#tool-submission-process)
- [Tools List](#tools-list)
- [Scripts README](.github/README-scripts.md)

## Tool Submission Process

We welcome submissions of open source tools that can benefit both technical and non-technical users. The submission process involves:

1. **Initial Submission** - Submit a tool using our issue template
2. **Evaluation** - Tool is tested for usability, security, and effectiveness
3. **Documentation** - Comprehensive documentation is created
4. **Review** - Community feedback and team review
5. **Integration** - Tool is added to our curated list

For detailed submission guidelines, templates, and evaluation criteria, please see our [Contributing Guidelines](CONTRIBUTING.md).

## Tools List

### Legend
- 🌟 Featured Tool
- ⭐ Highly Rated
- 🆕 Recently Added
- 🔧 Utility
- 📊 Data Analysis
- 🤖 AI/ML
- 🔒 Security
- 🌐 Web Tool
- 📱 Mobile App
- 🔍 Privacy
- 🤝 Collaboration

### Evaluated Tools

<!-- BEGIN TOOLS -->
| Category | Tool Name | Description | Status | Deployment | Technical Level | Documentation |
|----------|-----------|-------------|---------|------------|-----------------|---------------|
| AI/ML | [CoolTool](https://cooltool.com) | A cool AI tool | Active | Web Application, Docker Container | Beginner | [Details](docs/tools/ai/ml/cooltool.md) |
| AI/ML | [CoolTool](https://cooltool2.com) | A cool AI tool | Active | Web Application, Docker Container | Beginner | [Details](docs/tools/ai/ml/cooltool.md) |
| AI/ML | [CoolTool](https://cooltool3.com) | A cool AI tool | Active | Web Application, Docker Container | Beginner | [Details](docs/tools/ai/ml/cooltool.md) |
| AI/ML | [CoolTool](https://cooltool4.com) | A cool AI tool | Active | Web Application, Docker Container | Beginner | [Details](docs/tools/ai/ml/cooltool.md) |
| AI/ML | [CoolTool](https://cooltool5.com) | A cool AI tool | Active | Web Application, Docker Container | Beginner | [Details](docs/tools/ai/ml/cooltool.md) |
| Privacy | [Privacy Badger](https://www.tahr.org.tw/news/3214) | ... | Active | Desktop Application | Beginner | [Details](docs/tools/privacy/privacy-badger.md) |
| Communication | [Signal Test](https://signal.org/) | ... | Active | Mobile App | Beginner | [Details](docs/tools/communication/signal-test.md) |
<!-- END TOOLS -->

## Tool Evaluation Process

Each tool in our repository undergoes a thorough evaluation process:

1. **Initial Assessment**
   - Documentation review
   - Installation requirements
   - Dependencies analysis
   - Deployment options

2. **Technical Testing**
   - Functionality verification
   - Performance testing
   - Security assessment
   - Scalability evaluation

3. **User Experience Testing**
   - Non-technical user perspective
   - Interface evaluation
   - Documentation clarity
   - Setup complexity

4. **Deployment Testing**
   - Local installation
   - Cloud deployment (if applicable)
   - Configuration requirements
   - Maintenance needs

## Documentation Structure

Each tool in our repository includes detailed documentation covering:

1. **Overview**
   - Tool purpose and features
   - Use cases and benefits
   - Target audience

2. **Technical Details**
   - System requirements
   - Dependencies
   - Installation guides
   - Configuration options

3. **User Guides**
   - Step-by-step setup
   - Basic usage
   - Advanced features
   - Troubleshooting

4. **Evaluation Results**
   - Performance metrics
   - Security assessment
   - Usability findings
   - Recommended alternatives

## Tool Assessment Data Structure and Comparability Metrics
Each tool will be assessed using the following structured data fields:


## Data Structure
| Field Name                  | Data Type  | Example Values |
|-----------------------------|------------|----------------|
| Tool Name                   | String     | "Tor Browser" |
| Category                    | id     | "Secure Communication" |
| Status                      | Boolean (Y/N)   | Y |
| OS Compatibility            | List       | [Windows, macOS, Linux, Android, iOS] |
| Installation Manual      | Boolean (Y/N) | Y |
| User Documentation  | Boolean (Y/N) | Y |
| Required Technical Knowledge  | String | No Experience Required / Beginner / Advanced |
| Security Features | List | E2E, etc. |
| Data Collection Practices   | List     | "AES-256, RSA-4096" |
| Active Development     |  Boolean (Y/N) | Y |
| Community Support     | String | Strong |
| Last Update Date        | String | 11/2/24 |
| License     | id | OSI |
| Subscription needed     | Boolean (Y/N) | Y |
| External Links    | String | URL |



---


### 2. Metrics for Comparability
These five categories contribute to the overall tool assessment score. Each category has sub-metrics with assigned weights, and the category score is calculated as a weighted average of its sub-metrics.

#### **1. Operational Functionality (Weight: 10%)**
| Sub-Metric                       | Data Type | Example Value |
|-----------------------------------------|----------|--------------|
| Offline Functionality     | Integer (1-5) | 3 |
| Localization and Language Support         | Integer (1-5) | 5 |
| Mobile Accessibility      | Integer (1-5) | 2 |

#### **2. Usability for Non-Technical Users (Weight: 25%)**
| Sub-Metric                      |  Data Type | Example Value |
|---------------------------------|----------|--------------|
| Ease of installation/deployment |  Integer (1-5) | 3 |
| User onboarding experience      |  Integer (1-5) | 4 |
| Technical experience required   |  Integer (1-5) | 2 |

#### **3. Security & Privacy Strength (Weight: 30%)**
| Sub-Metric                      |  Data Type | Example Value |
|---------------------------------|----------|--------------|
| Encryption standards            | Integer (1-5) | 5 |
| Resilience against known threats| Integer (1-5) | 4 |
| Compliance with security best practices | Integer (1-5) | 3 |
| Data minimization               |  Integer (1-5) | 4 |
| Privacy policy transparency     |  Integer (1-5) | 5 |

#### **4. Maintenance & Sustainability (Weight: 15%)**
| Sub-Metric                      |  Data Type | Example Value |
|---------------------------------|----------|--------------|
| Active development              |  Integer (1-5) | 5 |
| Community support               |  Integer (1-5) | 3 |
| Funding & sponsorship           |  Integer (1-5) | 2 |

#### **5. Performance Efficiency (Weight: 20%)**
| Sub-Metric                      |  Data Type | Example Value |
|---------------------------------|----------|--------------|
| CSO Function                      | Integer (1-5)   | 4 |
| Relevance          |  Integer (1-5) | 3 |
| Effectiveness |  Integer (1-5) | 2 |

---

### **Final Scoring Calculation**
Each category is scored as a weighted average of its sub-metrics which are just simply added and divided by the number of sub-metrics for that category. The final tool score is then computed as a weighted sum of all five categories:


$$
\text{Final Score} = (0.10 \times \text{Operational Functionality}) + (0.25 \times \text{Usability}) + (0.30 \times \text{Security}) + (0.15 \times \text{Maintenance/Sustainability}) + (0.20 \times \text{Performance})
$$

We are planning to create a system that allows users to adjust weights dynamically on a webpage to find tools that match their specific needs. *Coming Soon!*


## Contributing

We welcome contributions from the community! Please see our [Contributing Guidelines](CONTRIBUTING.md) for:
- Tool submission process
- Documentation requirements
- Testing guidelines
- Review process

## License

This repository and its contents are licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

<div align="center">
Made with ❤️ by WPI students and the OCF community
</div>
