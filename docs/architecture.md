# CSPM Agent Architecture

Cloud Security Posture Management agent that continuously monitors cloud infrastructure against CIS benchmarks, detects configuration drift, prioritizes findings by risk, and generates remediation scripts.

## Domain Tools

- **analyze**: Primary analysis function for CSPM Agent
- **scan**: Scan target for issues relevant to CSPM Agent
- **report**: Generate report for CSPM Agent
- **remediate**: Execute remediation action
- **monitor**: Monitor for ongoing issues