
# Faultline Threat Model

## 1. Overview

Faultline is an open-source security remediation platform intended to connect
vulnerability findings with developer-reviewed fixes, verification results,
and auditable evidence.

This document identifies the primary assets, trust boundaries, potential
threats, and security controls relevant to the intended architecture.

It is a living document and must evolve alongside the implementation.
Documented controls are requirements unless their implementation and
effectiveness have been verified.

## 2. Scope

This threat model covers the intended handling of:

- Uploaded source archives and repository contents.
- Repository metadata and source files.
- Third-party dependencies and package metadata.
- Scanner output and normalized security findings.
- Remediation proposals and generated patches.
- Verification jobs and their execution environment.
- Logs, reports, and stored evidence.
- Application configuration, credentials, and access controls.

Deployment infrastructure and external integrations must be assessed
separately where their security properties are outside Faultline's control.

## 3. Security Objectives

Faultline should aim to preserve the following security properties:

- **Confidentiality:** Prevent unauthorized access to source code, credentials,
  findings, reports, and customer data.
- **Integrity:** Prevent unauthorized modification of findings, remediation
  proposals, verification outcomes, and evidence.
- **Availability:** Prevent malicious or excessive workloads from exhausting
  application or execution resources.
- **Isolation:** Prevent untrusted repositories and jobs from affecting other
  jobs, tenants, or the host environment.
- **Traceability:** Maintain reliable associations between findings, proposed
  fixes, verification results, and recorded evidence.
- **Human control:** Keep remediation proposals reviewable before acceptance
  or application.

## 4. Assets to Protect

| Asset | Security concern |
| --- | --- |
| Source code and archives | Unauthorized disclosure or modification |
| Credentials and secrets | Theft, leakage, or unauthorized use |
| Findings and scan results | Tampering, misclassification, or disclosure |
| Remediation proposals | Malicious or incorrect code changes |
| Verification results | False claims of successful remediation |
| Execution environment | Host compromise or cross-job access |
| Reports and evidence | Tampering or leakage of sensitive information |
| Application data | Unauthorized access or destructive changes |
| Service availability | Resource exhaustion and denial of service |

## 5. Trust Boundaries

Faultline must treat the following boundaries as security-sensitive:

1. **External user to application:** Requests, uploads, and configuration
   values may be malicious or malformed.
2. **Repository to processing pipeline:** Repository files and build scripts
   must not be trusted merely because a user supplied the repository.
3. **Scanner to application:** Scanner output may be malformed, incomplete,
   unexpectedly large, or influenced by malicious input.
4. **Remediation engine to developer:** Proposed changes may introduce bugs,
   unsafe behavior, or new vulnerabilities.
5. **Job execution to host:** Analysis and verification jobs must not receive
   unnecessary host privileges or unrestricted access to host resources.
6. **Application to external services:** Integrations may expose credentials
   or data if permissions and outbound requests are not controlled.
7. **Application to persistence and reports:** Access controls must prevent
   unauthorized reading or modification of stored records and exported data.

## 6. Threat Scenarios and Required Controls

### T1. Archive Path Traversal

**Threat:** A crafted archive contains paths such as `../../target` or
absolute paths intended to write files outside the extraction directory.

**Potential impact:** File overwrite, disclosure of local files, or compromise
of the processing environment.

**Required controls:**
- Reject absolute paths and traversal components.
- Resolve and validate extraction destinations against the intended root.
- Handle symbolic links and platform-specific path behavior safely.
- Apply archive size, file count, and decompressed-size limits.
- Extract into a restricted, temporary workspace.

**Validation:** Test traversal paths, malicious links, nested archives, and
oversized archive entries.

### T2. Command Injection

**Threat:** Malicious repository content or user-controlled values influence
shell commands or process arguments.

**Potential impact:** Unauthorized command execution, credential theft, or
environment compromise.

**Required controls:**
- Avoid shell execution when direct process invocation is available.
- Pass arguments as structured argument lists rather than concatenated strings.
- Validate arguments against explicit allowlists where appropriate.
- Use fixed executable paths and controlled working directories.
- Run jobs with least privilege and restricted filesystem access.

**Validation:** Test metacharacters, unexpected arguments, and malicious
repository metadata without executing destructive payloads.

### T3. Malicious Repositories and Build Scripts

**Threat:** Repository files, dependency installation hooks, build scripts,
or test commands execute malicious behavior during analysis or verification.

**Potential impact:** Host compromise, secret exfiltration, cross-job access,
or unauthorized network activity.

**Required controls:**
- Do not execute repository-controlled scripts implicitly.
- Require explicit configuration or approval for execution-sensitive steps.
- Run untrusted workloads in an appropriately isolated environment.
- Restrict network access, mounted paths, credentials, and Linux capabilities.
- Apply CPU, memory, process-count, disk, and execution-time limits.
- Destroy temporary workspaces after jobs complete.

**Validation:** Use controlled test repositories to evaluate isolation,
filesystem restrictions, and network policy enforcement.

### T4. Secret Exposure

**Threat:** Credentials appear in source code, scanner output, process
arguments, environment variables, logs, reports, or generated patches.

**Potential impact:** Unauthorized access to repositories, services, or
production infrastructure.

**Required controls:**
- Keep credentials out of source control and client-visible responses.
- Redact detected secrets from logs and exported reports.
- Avoid placing secrets in command-line arguments.
- Use short-lived, narrowly scoped credentials where possible.
- Prevent untrusted jobs from accessing application-level secrets.
- Define retention and deletion rules for sensitive artifacts.

**Validation:** Test known dummy secrets across logs, reports, errors, and
job metadata. Never use real credentials in security tests.

### T5. Malicious or Malformed Scanner Output

**Threat:** Scanner output contains oversized payloads, invalid structures,
misleading fields, or content intended to exploit downstream parsers.

**Potential impact:** Application errors, resource exhaustion, misleading
findings, or injection into reports and user interfaces.

**Required controls:**
- Validate output against a defined schema.
- Bound input size, nesting depth, and collection lengths.
- Normalize tool-specific fields before downstream processing.
- Escape untrusted content when rendering it.
- Record parser failures without exposing sensitive payloads.

**Validation:** Test malformed JSON, unexpected field types, oversized results,
and hostile strings in finding descriptions.

### T6. Incorrect or Malicious Remediation

**Threat:** A proposed fix is incomplete, introduces a new vulnerability,
or does not actually address the original finding.

**Potential impact:** False confidence, insecure code changes, or regressions.

**Required controls:**
- Link each proposal to its originating finding.
- Present changes for developer review.
- Run relevant tests and security checks where supported.
- Distinguish proposed, accepted, applied, and verified states.
- Do not equate a successful test run with proof that all vulnerabilities
  have been eliminated.

**Validation:** Test rejected patches, failing checks, partial fixes, and
changes that do not address the original finding.

### T7. Resource Exhaustion

**Threat:** Oversized archives, pathological files, excessive findings, or
expensive verification jobs consume excessive resources.

**Potential impact:** Increased costs, stalled workers, or denial of service.

**Required controls:**
- Set upload and decompression limits.
- Bound execution time, memory, CPU, process count, and disk usage.
- Limit concurrency and queue growth.
- Apply request rate limits where appropriate.
- Support cancellation and cleanup of failed or timed-out jobs.

**Validation:** Test configured limits and confirm that timed-out jobs release
their resources.

### T8. Unauthorized Access or Cross-Tenant Data Leakage

**Threat:** A user accesses another user's repository, job, finding, or report
through missing authorization checks or predictable identifiers.

**Potential impact:** Source-code disclosure, data tampering, or privacy breaches.

**Required controls:**
- Authenticate users where required by the deployment model.
- Enforce authorization on every protected operation.
- Scope queries and object access to the authorized user or tenant.
- Use least-privilege service credentials.
- Test access-control boundaries independently of frontend restrictions.

**Validation:** Attempt unauthorized read, update, deletion, and report-export
operations across test users or tenants.

### T9. Evidence Tampering or Misleading Reports

**Threat:** Verification results or evidence are modified, misattributed, or
presented without sufficient context.

**Potential impact:** Developers make unsafe decisions based on unreliable
security claims.

**Required controls:**
- Associate evidence with the relevant job, finding, and remediation revision.
- Record timestamps and tool or check identifiers where available.
- Preserve failure and inconclusive states.
- Restrict unauthorized modification of completed job records.
- Clearly disclose missing checks and verification limitations.

**Validation:** Test whether evidence can be incorrectly associated with another
job or represented as successful after a failed check.

### T10. Unsafe External Integrations

**Threat:** An integration follows untrusted URLs, leaks credentials, or
communicates with unauthorized destinations.

**Potential impact:** Server-side request forgery, credential disclosure, or
unauthorized network access.

**Required controls:**
- Validate destination URLs and restrict access to internal or sensitive
  network ranges where applicable.
- Apply outbound network policies to execution jobs.
- Limit token scopes and avoid sharing credentials across jobs.
- Set connection and response-size limits.
- Handle redirects and DNS resolution carefully.

**Validation:** Test blocked internal destinations, unexpected redirects,
and unauthorized integration requests in a controlled environment.

## 7. Security Testing Strategy

Security testing should include:

- Unit tests for input validation and path handling.
- Integration tests for scanner parsing and workflow authorization.
- Adversarial test cases for malformed and oversized inputs.
- Isolation tests for untrusted execution jobs.
- Secret-redaction tests using dummy credentials.
- Verification-state and evidence-integrity tests.
- Dependency and static-analysis checks in CI where configured.

Passing these tests provides evidence for the specific cases tested; it does
not prove the absence of all vulnerabilities.

## 8. Assumptions and Residual Risks

This threat model assumes that users may submit malicious repositories and
that scanner results and generated remediation proposals are not inherently
trustworthy.

Residual risks may include unknown vulnerabilities, weaknesses in third-party
tools, misconfigured deployment environments, incomplete isolation, and
incorrect security-analysis results.

Controls must be evaluated against the actual deployment environment. A
documented requirement must not be represented as an implemented safeguard
without supporting code, configuration, and appropriate tests.

## 9. Review and Maintenance

Review this document whenever:

- A new scanner or external integration is introduced.
- Repository-controlled code can be executed.
- Authentication, authorization, or multi-tenant functionality changes.
- New data types or sensitive artifacts are stored.
- The execution environment or deployment architecture changes.
- A security incident reveals a previously unconsidered threat.

Security issues should be reported according to the process documented in
[SECURITY.md](SECURITY.md).

---

**Status:** Initial threat model. This document is not a security audit,
certification, or guarantee that the listed controls are implemented.
