# Goat Show Manager Testing Strategy 🐐

This document outlines the testing approach for Goat Show Manager.  
It defines tools, practices, and workflows to ensure code quality and reliability.

---

## 🎯 Goals
- Maintain high test coverage across all modules
- Catch bugs early through automated testing
- Ensure reproducibility and consistency in results
- Support CI/CD integration with GitHub Actions

---

## 🧪 Testing Framework
- **Framework:** `pytest`
- **Why:** Simple syntax, powerful fixtures, integrates well with PyCharm and CI/CD
- **Command:** Run all tests with:
  ```bash
  pytest

📂 Test Organization
GoatShowManager/
│── tests/
│    ├── test_models.py      # Tests for Goat, Owner, Show, Judge
│    ├── test_services.py    # Tests for registration, scoring, scheduling
│    ├── test_utils.py       # Tests for validation, formatting, file I/O
│    └── test_cli.py         # Tests for CLI menus and user input

🔑 Testing Principles
Unit Tests: Cover individual functions and classes

Integration Tests: Verify interactions between modules (e.g., services + models)

Edge Cases: Test invalid input, missing data, and boundary conditions

Repeatability: Tests should run consistently across environments

📊 Coverage
Use pytest-cov for coverage reports:
  pytest --cov=src --cov-report=html
Aim for 80%+ coverage across all modules

Review coverage reports regularly

⚙️ Continuous Integration (CI)
Use GitHub Actions to run tests automatically on each push or pull request

Example workflow (.github/workflows/tests.yml):
name: Run Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      - run: pip install -r requirements.txt
      - run: pytest --cov=src

🐐 Next Steps
Add pytest-cov to requirements.txt

Write initial tests for models/Goat and services/registration

Set up GitHub Actions workflow for automated testing