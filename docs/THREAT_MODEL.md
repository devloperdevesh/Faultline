# Threat Model

Treat uploaded archives, repositories, dependencies, and scanner output as
untrusted input.

Potential threats include archive path traversal, command injection, secrets
exposure, malicious repositories, and resource exhaustion.

Required controls include input validation, safe process execution, resource
limits, secret redaction, workload isolation, and human review of proposed fixes.

This document is a starting point, not a security certification.
