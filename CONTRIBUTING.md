
# Contributing to Faultline

Thank you for your interest in contributing to Faultline.

Faultline is an open-source security remediation project focused on connecting vulnerability findings, reviewable fixes, verification, and auditable evidence.

We welcome contributions that improve code quality, security, reliability, documentation, testing, and developer experience.

## Contribution Principles

| Principle | Expectation |
|---|---|
| Security first | Consider security implications before introducing changes. |
| Reviewability | Keep changes focused, understandable, and easy to review. |
| Testability | Add tests that demonstrate the expected behaviour. |
| Transparency | Document limitations, assumptions, and incomplete functionality. |
| Reproducibility | Include clear steps to reproduce bugs and validate fixes. |
| Collaboration | Communicate respectfully and provide constructive feedback. |

## Before You Start

1. Read the [README](README.md) to understand the project.
2. Review [ARCHITECTURE.md](ARCHITECTURE.md) for the current system design.
3. Check existing [issues](https://github.com/devloperdevesh/Faultline/issues) and pull requests.
4. Open an issue before making significant architectural changes.
5. For small documentation fixes or straightforward bugs, a separate issue may not be necessary.

Please avoid duplicating existing work. If you are unsure about an approach, discuss it with the maintainers before investing significant time.

## Development Workflow

### 1. Fork and Clone

Fork the repository on GitHub, then clone your fork:

```bash
git clone https://github.com/<your-username>/Faultline.git
cd Faultline
```

Add the original repository as an upstream remote:

```bash
git remote add upstream https://github.com/devloperdevesh/Faultline.git
git fetch upstream
```

### 2. Create a Focused Branch

Create a branch from the latest default branch:

```bash
git checkout main
git pull upstream main
git checkout -b fix/short-description
```

Use a descriptive branch name.

| Prefix | Purpose | Example |
|---|---|---|
| `feat/` | New functionality | `feat/finding-normalization` |
| `fix/` | Bug fixes | `fix/finding-validation` |
| `test/` | Test improvements | `test/scanner-adapter` |
| `docs/` | Documentation | `docs/setup-guide` |
| `refactor/` | Code restructuring | `refactor/report-generation` |
| `security/` | Security-related changes | `security/path-validation` |

### 3. Make Your Changes

- Keep changes focused on one problem or feature.
- Follow the existing project structure and coding conventions.
- Avoid unrelated formatting changes.
- Handle invalid input and failure cases explicitly.
- Preserve existing behaviour unless the change intentionally modifies it.
- Update documentation when interfaces, configuration, or workflows change.
- Never claim functionality is implemented unless it can be demonstrated and tested.

### 4. Install Dependencies

Use the dependencies and setup instructions documented in the current repository.

For the Python backend, the following commands may be used when supported by the project:

```bash
python -m venv .venv
python -m pip install -r backend/requirements.txt
```

Activate the virtual environment before running project tools.

If a contribution requires additional dependencies, explain why they are needed and update the appropriate dependency file.

### 5. Test Your Changes

Run the relevant tests and checks before opening a pull request.

For example, if the repository uses pytest and Ruff:

```bash
python -m pytest tests -v
python -m ruff check backend/app tests
```

Adapt these commands to the affected component and the current repository configuration.

For security-sensitive changes, also consider:

- Invalid and malformed input.
- Authentication and authorization boundaries, where applicable.
- Path traversal and unsafe file handling.
- Secret exposure and sensitive-data handling.
- Regression tests for the original vulnerability.
- Failure behaviour when an external scanner or dependency is unavailable.

Report the checks that actually ran and their results. Do not describe unexecuted tests as passing.

### 6. Commit Your Changes

Use clear, descriptive commit messages:

```bash
git add .
git commit -m "fix: validate finding input"
```

Examples:

```text
feat: normalize scanner findings
fix: reject unsafe file paths
test: cover remediation validation
docs: clarify local setup
```

Avoid committing generated files, local environments, credentials, or unrelated changes.

### 7. Open a Pull Request

Push your branch:

```bash
git push -u origin fix/short-description
```

Then open a pull request against the repository's default branch.

Your pull request should explain:

- **Problem:** What issue does this change address?
- **Solution:** What did you change and why?
- **Testing:** Which commands or tests did you run?
- **Security impact:** Does the change affect security boundaries or sensitive data?
- **Limitations:** What remains incomplete or unverified?
- **Related issue:** Link the relevant issue, if applicable.

Keep pull requests small enough to review effectively.

## Pull Request Checklist

Before submitting, confirm the applicable items:

- [ ] The change addresses a clear problem or requirement.
- [ ] The implementation follows existing project conventions.
- [ ] Tests were added or updated where appropriate.
- [ ] Relevant checks were executed and their results reported accurately.
- [ ] Documentation reflects changes to behaviour or setup.
- [ ] Security implications and limitations are documented.
- [ ] No credentials, tokens, customer data, or private source code were committed.
- [ ] No unsupported performance, security, or reliability claims were introduced.

## Security Requirements

Faultline processes security-related information. Contributions must take particular care to avoid introducing vulnerabilities.

- Never commit API keys, passwords, access tokens, private keys, or production credentials.
- Never upload customer data, confidential source code, or sensitive vulnerability reports.
- Do not execute untrusted code without appropriate isolation and safeguards.
- Validate inputs and avoid unsafe file operations.
- Do not automatically apply proposed security fixes without appropriate safeguards and review.
- Use the responsible disclosure process in [SECURITY.md](SECURITY.md) to report vulnerabilities in Faultline itself.

Do not disclose exploitable vulnerabilities through public issues or pull requests before coordinating responsible disclosure.

## Documentation and Product Claims

Documentation is part of the contribution.

- Clearly distinguish implemented functionality from planned work.
- Label conceptual dashboards, sample metrics, and simulated workflows as illustrative.
- Do not present mock scan results as real scanner output.
- Do not claim that a vulnerability is resolved without appropriate verification.
- Document known limitations, configuration requirements, and failure modes.
- Support performance and security claims with reproducible evidence.

## Code of Conduct

All contributors are expected to follow the standards described in [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).

Respectful communication and constructive technical discussion are expected in issues, pull requests, reviews, and other project-related spaces.

## Questions and Discussions

For questions, proposed features, and implementation discussions:

- [Open an issue](https://github.com/devloperdevesh/Faultline/issues)
- Review the repository's existing documentation.
- Include relevant logs, reproduction steps, and environment details when reporting a bug. Remove secrets and sensitive information before sharing logs.

## Thank You

Every thoughtful contribution helps make security remediation more reviewable, verifiable, and evidence-driven.

**Faultline — From vulnerability findings to verified remediation.**
