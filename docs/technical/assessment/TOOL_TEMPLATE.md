# Testing Template
Does the tool "prove" to be high-impact?

## Testing & Evaluation Sheet

### Tool Overview
- **Name**: [Tool Name]
- **Category**: [Category, e.g., Secure Communication, Anonymity, Encryption]
- **Purpose**: [What the tool is designed to do]
- **Date Tested**: [Date tested]
- **Status**: 
  - [ ] Deployed / Not Deployed (Launched or not)
  - [ ] Operational - Actively running/maintained
  - [ ] In Testing - Currently being evaluated or piloted
  - [ ] Inactive/Deprecated - No longer maintained or functional
- **Deployment Architecture**:
  - [ ] A standalone software - Runs entirely locally (e.g., runs on computer and doesn't depend on external server)
  - [ ] A locally hosted service with separate server and client component - Run both backend/frontend yourself (e.g., backend could be on a local network, or self-hosted on cloud)
  - [ ] A service with a local client that's hosted by a third party - You install a client on your device, but it connects to and depends on a remote server (e.g., Signal: install app (client), but Signal's servers handle message relaying, etc.)
  - [ ] A service that is hosted by a third party but can also be self-hosted
- **Version**: [Version Tested]

### Installation & Setup
- **OS Compatibility**: What is the OS compatibility of the tool?
- **Installation Manual**: Yes/No
- **Installation Steps**: What is the installation process?
- **Common Installation Issues & Fixes**: List common errors users might face and how to troubleshoot them
- **User Documentation**: Yes/No
- **Required Technical Knowledge**: None, beginner, intermediate, professional
- **Special Configurations**: Mention if command-line setup or special configurations are needed

### Testing & Evaluation

#### Operational Functionality
- **Functionality**
  - Test Steps: Verify the tool's core features by using all major functions, tracking any failures or bugs.
  - [ ] The tool is mostly non-functional with many broken features and bugs
  - [ ] Several broken features or bugs
  - [ ] Minor bugs or issues
  - [ ] Mostly functional with few bugs or no bugs
  - [ ] Fully functional with no bugs

- **Internet Dependence**:
  - Simulate no internet connection (e.g., disable Wifi)
  - Test the tool on 2G/3G networks

- **Localization & Language Support**
  - How many languages are available?
  - Which East Asian languages are available?
  - Do they have an active community contributing to localization?

- **Mobile Accessibility**
  - Verify if a mobile app exists and is functional
  - Test key functions (e.g., navigating, uploading data) on mobile browsers

#### Usability for Non-Technical Users
- **Ease of Installation & Deployment**
  - How many steps are required to install the tool?
  - Are there one-click installations, or does it require command-line knowledge?
  - Are setup guides, manuals and FAQ's regularly updated?
  - Approximately how much times does a typical installation take (e.g., under 10 minutes, 30+ minutes)

- **User Onboarding Experience**
  - Are there any tool-tips or in-app guidance when first using the software?

- **Technical Experience Level Required**
  - Can users with no programming background install and start using the tool?
  - Is the interface visual and menu-driven or does it rely heavily on terminal commands?

#### Security & Privacy Strength
- **Encryption Standards**
  - Verify encryption strength through external tools or expert review
  - Does the tool use E2E encryption? What algorithm is used? (E.g., "AES-256 encryption used; E2E verified in test")

- **Known Strength resilience**
  - Is the tool usable in regions with heavy censorship or surveillance?
  - Does it include built-in circumvention tools?
  - Any known weaknesses or risks?

- **Comparison with Known Standards**
  - How does the tool measure up against established security/privacy standards?

- **Data Minimization**
  - What user data is collected?

- **Privacy Policy Transparency**
  - What does the privacy policy state about data handling?

#### Maintenance/Sustainability
- **Community support**
  - Is it easy to get help, ask questions, or find solutions from other users or developers?

- **Development active status**
  - How frequently is it updated?
  - How responsive is the development team?

- **Funding and Sponsorship**
  - Who are the main funders? (e.g., NGOs, governments, private donors)
  - Who are the main sponsors?
  - Does the software seem financially sustainable?

#### Performance / Effectiveness & Reliability
- **Testing Environment Setup**:
  - Device: [Device model and specs (CPU, RAM, etc.)]
  - OS: [Operating System version]
  - Network: [Network type and speed (e.g., broadband, 3G/4G, etc.)]

- **User Experience Observations**
  - How smooth does the tool feel?
  - What is the tool's responsiveness during normal use?

- **Speed & Responsiveness**:
  - Does it load & work efficiently?
  - Conduct speed tests to measure loading times and responsiveness (e.g., using ping, traceroute, lighthouse)
  - Are there any noticeable delays or lag during use?

- **Resource Usage**:
  - How much CPU & memory does it consume?
  - Measure CPU and memory usage using specific tools like Task Manager (Windows), htop (Linux), or Activity Monitor (macOS)?

- **Network Performance**:
  - How much Latency & Bandwidth Usage?
  - Test network efficiency by monitoring bandwidth consumption with tools like Wireshark.

- **Reliability**
  - Are there independent peer reviews or third-party audits available?
  - Detail if low error rates and specify uptime percentage
  - Run core tests multiple times and log how many attempts fail

### Deployment Considerations
- **Open Source & Transparency**:
  - Is the code open for independent verification?

- **Cloud vs. Local Deployment**:
  - Does the tool require cloud infrastructure like AWS or Azure, or can it be locally run on a private server?

- **Dependencies**:
  - Does it require Docker, Python, databases, etc.?
  - Are dependencies clearly documented?

- **Post-Deployment Maintenance**
  - After deployment, is the tool easy to maintain?
  - If a deployer decides to fork the project, is the code easy to modify?
- **Merge/Sustainability**: 
  - How open is the original project to contributions?
  - Is there a streamlined process for submitting changes back to the main repository?

### Testing Scenarios
#### Scenario 1
- Notes & Documentation

#### Scenario 2
- Notes & Documentation

### Insights & Recommendations
- **Key Findings**
  - What are the key findings?

- **Strengths**:
  - What are the benefits of the tool?

- **Weaknesses**:
  - What are the major drawbacks of the tool?

- **Suggested Improvements**
  - What are some suggestions for improving the tool?

- **Alternative Tools**:
  - Are there better tools available? If so, which tools are they?

- **License**:
  - Which License?

- **Cost/Resource Implications**:
  - **Total Cost of Ownership**:
    - Is the tool free to use?
      - Are there premium tiers or paid features?
    - Are there hidden costs for maintenance, third-party integrations, or updates?
    - [License cost, time, resources to install, maintain and troubleshoot]

### Why is this useful to civil societies in authoritarian environments?
Explain why this tool would be useful to civil society organizations. Include if it is unavailable in certain regions due to firewalls or other blocking systems.