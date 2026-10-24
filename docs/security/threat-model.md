# Security Threat Model

Treat uploaded repositories, archives, dependency manifests, and scanner output
as untrusted input.

Security requirements:
- Validate archive paths and prevent path traversal.
- Avoid executing untrusted code on the host.
- Apply time, memory, and process limits to scanner jobs.
- Never log secrets or credentials.
- Require human review before accepting or merging proposed changes.
- Clearly document network access and data retention.
