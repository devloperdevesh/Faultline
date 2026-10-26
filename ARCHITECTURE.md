
# Faultline Architecture

Faultline is an open-source security remediation platform designed to connect
vulnerability findings with reviewable fixes, verification results, and
auditable evidence.

This document describes the intended architecture and component boundaries.
It does not imply that every component or integration is currently implemented.

## 1. Design Goals

- Connect security findings to actionable remediation workflows.
- Preserve developer control over proposed code changes.
- Verify remediation using relevant checks rather than assuming a fix is correct.
- Maintain traceable records of findings, proposed changes, and verification outcomes.
- Isolate untrusted inputs and security-analysis jobs.
- Keep scanner integrations modular and replaceable.

## 2. High-Level Workflow

The intended workflow is:

1. **Discover** — collect findings from supported security analysis tools.
2. **Normalize** — convert tool-specific output into a consistent finding format.
3. **Prioritize** — organize findings using available severity and contextual information.
4. **Remediate** — generate or present proposed changes for developer review.
5. **Verify** — run relevant checks to evaluate whether the proposed remediation addresses the finding.
6. **Record** — preserve verification outcomes and associated evidence.
7. **Report** — present findings, remediation status, and verification results.

Each stage should have explicit inputs, outputs, and failure states.

## 3. Intended Components

### Frontend

Provides the user interface for reviewing findings, tracking remediation
workflows, inspecting proposed changes, viewing verification outcomes, and
accessing reports.

### API Layer

Handles request validation, authentication and authorization where configured,
workflow orchestration, and communication between application components.

The API should enforce access controls and validate untrusted input at system
boundaries.

### Scanner Adapters

Integrate supported security analysis tools and translate their outputs into
Faultline's normalized finding format.

Adapters should be modular so that scanner-specific behavior does not leak
throughout the application.

### Remediation Engine

Manages proposed fixes and their associated review workflow.

Proposed changes should remain reviewable by developers. A generated patch
must not be treated as a verified fix merely because it was produced.

### Verification Engine

Runs relevant tests or security checks against a proposed remediation and
records the results.

Verification outcomes should distinguish between successful checks, failed
checks, inconclusive results, and execution errors.

### Evidence and Reporting

Associates findings with relevant remediation details, verification outcomes,
timestamps, and available execution metadata.

Reports should distinguish verified results from pending, failed, or
unverified work. Sensitive values must not be included in exported evidence.

### Execution Sandbox

Provides an isolation boundary for untrusted inputs and security-analysis
jobs.

Depending on the execution environment, isolation may require restricted
filesystem access, limited network access, resource limits, and least-privilege
execution. The intended boundary must not be described as secure isolation
until its controls have been implemented and tested.

### Persistence Layer

Stores application records such as jobs, findings, remediation proposals,
verification outcomes, and associated metadata.

The implementation should define data ownership, retention, access controls,
and appropriate handling of sensitive information.

## 4. Data Flow

The intended data flow is:

    Security Tools
         |
         v
    Scanner Adapters
         |
         v
    Normalized Findings
         |
         v
    API / Workflow Orchestration
         |
         v
    Remediation Proposal
         |
         v
    Developer Review
         |
         v
    Verification Jobs
         |
         v
    Results and Evidence
         |
         v
    Reports / Frontend

The persistence layer supports the workflow by storing relevant records.
The sandbox is intended to constrain untrusted job execution.

This diagram represents the target design, not a guarantee that all
connections are implemented in the current repository.

## 5. Security Principles

- Validate and normalize untrusted input before processing it.
- Apply least privilege to application components and execution jobs.
- Keep credentials and secrets out of logs, reports, and source control.
- Require explicit authorization for sensitive operations.
- Avoid executing untrusted code directly within the main application process.
- Treat scanner output and generated remediation as untrusted until validated.
- Record verification results without overstating what the checks prove.
- Document security assumptions and limitations for each execution environment.

## 6. Failure Handling and Observability

Components should expose meaningful failure states and sufficient diagnostic
information to support investigation.

Where implemented, observability should cover job status, execution failures,
verification outcomes, and relevant timing information.

Logs and telemetry must avoid exposing credentials, private customer data,
or sensitive source-code content unnecessarily.

## 7. Implementation Status

The components described above define the intended architecture. Their actual
implementation status depends on the current source code and configured
integrations.

Update this document whenever component boundaries, data flows, security
controls, or supported integrations change.

Do not describe a scanner, sandbox, verification mechanism, or persistence
integration as operational until it has been implemented and validated.
