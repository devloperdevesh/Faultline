# Faultline Architecture

Intended components:

- Frontend: project workflow, findings, remediation review, and reports.
- API: request validation and workflow orchestration.
- Scanners: adapters for security analysis tools.
- Remediation: proposed changes requiring developer review.
- Verification: relevant checks and recorded outcomes.
- Reports: exportable findings and evidence.
- Sandbox: isolation boundary for untrusted inputs and jobs.
- Database: persistence for jobs, findings, and results.

These are intended boundaries. Update this document as implementation evolves.
