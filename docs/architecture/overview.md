
# Faultline Overview

## From Vulnerability Findings to Verified Remediation

Faultline is an open-source security remediation platform designed to help
developers move from discovering vulnerabilities to reviewing proposed fixes,
checking remediation outcomes, and preserving supporting evidence.

Security findings are only the starting point. Developers also need a
reliable way to understand issues, evaluate proposed changes, determine
whether relevant checks pass, and track what remains unresolved.

Faultline aims to connect these steps in a single, traceable workflow.

## The Problem

Security tools can identify vulnerabilities, but identifying a problem does
not automatically resolve it.

Development teams still need to:
- Understand and prioritize findings.
- Determine which code or dependency is affected.
- Review proposed remediation changes.
- Run relevant tests and security checks.
- Track unresolved findings and document verification results.

When these activities are disconnected, remediation can become difficult to
review, track, and verify.

## The Approach

Faultline is designed around a finding-to-evidence workflow:

1. **Discover** — ingest findings from supported security analysis tools.
2. **Normalize** — convert tool-specific results into a consistent format.
3. **Prioritize** — organize findings using severity and available context.
4. **Remediate** — present proposed fixes for developer review.
5. **Verify** — run relevant checks and record their outcomes.
6. **Document** — preserve findings, remediation details, and verification
   evidence for review and reporting.

The intended result is a traceable connection between an original finding,
the proposed remediation, and the checks performed afterward.

## Design Principles

- **Developer control:** Proposed changes should remain reviewable.
- **Verification over assumptions:** Generating a fix does not prove that
  the vulnerability has been resolved.
- **Traceability:** Findings, remediation proposals, and verification results
  should remain connected.
- **Security by design:** Untrusted repositories and analysis jobs require
  appropriate validation and isolation.
- **Honest reporting:** Reports should distinguish verified, failed,
  inconclusive, and unverified outcomes.
- **Open development:** Architecture, limitations, and project progress
  should be documented transparently.

## Intended Workflow

    Source Code / Dependencies
              |
              v
       Security Findings
              |
              v
     Normalization and Review
              |
              v
     Proposed Remediation
              |
              v
       Developer Approval
              |
              v
      Verification Checks
              |
              v
      Results and Evidence
              |
              v
       Reviewable Reports

This diagram represents the intended workflow, not a claim that every stage
is currently connected or operational.

## Project Status

Faultline is under active development. The workflow and components described
in this document represent the project's intended direction.

Available functionality depends on the current implementation and configured
integrations. Planned scanners, remediation capabilities, verification
mechanisms, and reporting features must not be assumed to be operational
until implemented and tested.

## Contributing

Contributions are welcome in areas such as scanner integrations, finding
normalization, remediation workflows, verification, testing, documentation,
and security hardening.

Please review [CONTRIBUTING.md](CONTRIBUTING.md) before submitting changes.
For security-sensitive issues, follow the process in [SECURITY.md](SECURITY.md).

## Links

- [Architecture](ARCHITECTURE.md)
- [Roadmap](ROADMAP.md)
- [Threat Model](THREAT_MODEL.md)
- [Security Policy](SECURITY.md)
- [Contributing Guide](CONTRIBUTING.md)
