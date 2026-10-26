
# Faultline Roadmap

Faultline aims to make security remediation more actionable, verifiable, and
traceable — connecting vulnerability findings to developer-reviewed fixes
and evidence of remediation.

This roadmap describes planned milestones, not a guarantee that every feature
will ship. Priorities may change based on implementation progress and
feedback from developers and security teams.

## 1. Foundation — Build a Reliable Core

- [ ] Establish a working API with automated tests.
- [ ] Define the core data model for findings, remediation proposals, jobs,
      and verification results.
- [ ] Build the initial frontend for reviewing findings and workflow status.
- [ ] Add continuous integration for tests, linting, and basic security checks.
- [ ] Document the threat model, trust boundaries, and security assumptions.
- [ ] Establish clear error handling and job lifecycle states.

**Milestone:** A developer can run the application and exercise a documented,
testable core workflow.

## 2. Security Findings — Turn Scan Output into Actionable Data

- [ ] Define a stable scanner adapter interface.
- [ ] Normalize findings into a consistent schema.
- [ ] Preserve source, severity, affected component, and available references.
- [ ] Implement finding deduplication and explainable prioritization.
- [ ] Integrate an initial dependency vulnerability scanner.
- [ ] Evaluate secret-scanning integration with safe handling of sensitive data.

**Milestone:** Findings from a supported scanner can be ingested, reviewed,
and traced back to their source.

## 3. Remediation — Make Fixes Reviewable

- [ ] Associate remediation proposals with their originating findings.
- [ ] Present proposed changes in a reviewable format.
- [ ] Support developer approval, rejection, and revision of proposals.
- [ ] Preserve the relationship between findings and proposed fixes.
- [ ] Define safe execution boundaries for remediation-related jobs.
- [ ] Prevent a proposed change from being labelled verified without
      corresponding verification evidence.

**Milestone:** A developer can inspect and review a proposed fix before
accepting it.

## 4. Verification — Produce Evidence, Not Just Claims

- [ ] Define verification checks for supported finding types.
- [ ] Run relevant checks against proposed remediations.
- [ ] Distinguish passed, failed, inconclusive, and errored checks.
- [ ] Record execution metadata and verification outcomes.
- [ ] Generate reports linking findings, changes, and verification evidence.
- [ ] Test failure scenarios and document verification limitations.

**Milestone:** A developer can determine what was checked, what passed,
and what remains unresolved.

## 5. Developer Workflows — Fit Existing Engineering Practices

- [ ] Support repository import through a documented workflow.
- [ ] Add job history and finding status tracking.
- [ ] Enable report export with appropriate sensitive-data controls.
- [ ] Evaluate pull request and CI integration.
- [ ] Add further scanner integrations based on user demand.
- [ ] Document deployment, configuration, and troubleshooting.

**Milestone:** Developers can incorporate supported Faultline workflows into
their existing repository and review process.

## 6. Validation — Prove the Product Solves a Real Problem

- [ ] Recruit developers or security engineers to test the core workflow.
- [ ] Measure time from finding ingestion to reviewed remediation.
- [ ] Track verification success, false positives, and unresolved findings.
- [ ] Evaluate usability against existing developer workflows.
- [ ] Document limitations and publish reproducible evaluation results.
- [ ] Prioritize improvements using user feedback and observed failures.

**Milestone:** Demonstrate measurable value on real, authorized test
repositories before making broader effectiveness claims.

## Guiding Principles

- **Developer control:** Proposed fixes remain reviewable.
- **Verifiable outcomes:** A generated fix is not automatically a successful fix.
- **Traceability:** Findings, changes, and verification results remain connected.
- **Secure by design:** Untrusted inputs and execution jobs require explicit
  security boundaries.
- **Evidence over claims:** Publish only metrics supported by reproducible tests.
- **Open development:** Use issues and discussions to explain priorities and
  invite focused contributions.

## Contributing to the Roadmap

This roadmap is subject to change as the project develops. Contributions,
bug reports, integration proposals, and feedback are welcome through the
repository's GitHub issues and pull requests, where enabled.
