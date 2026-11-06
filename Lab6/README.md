# Lab 6: Code and Branch Coverage Analysis

## Objective

To understand the difference between code coverage and branch coverage, use Python coverage tools to measure test completeness, identify untested code paths, and improve test cases to achieve at least 90% coverage.

## Application Overview

**Assigned Program:** Blood Donation Screening

The application contains two functions:

1. **`process_donor_cohort()`**
   - Validates donor cohort information.
   - Checks donor eligibility based on age, weight and haemoglobin levels.
   - Calculates collected blood volume.
   - Handles high-altitude cohorts and fast-track processing.
   - Determines the final status: `ACCEPTED`, `ZERO_YIELD` or `HIGH_DEFERRAL`.

2. **`verify_storage_centrifuge()`**
   - Checks centrifuge RPM readings.
   - Detects consecutive RPM drops.
   - Returns `ABORT_SPIN`, `STABLE` or `NO_DATA`.

## Tools and Technologies

- Python 3.12
- Pytest
- Coverage.py
- Visual Studio Code
- Git and GitHub

## Test Files

| File | Description |
|---|---|
| `blood_donation_screening.py` | Original application program |
| `test_blood_donation.py` | Original test case |
| `CodeCoverageTest_blood_donation_screening.py` | Test cases for code coverage |
| `BranchCoverageTest_blood_donation_screening.py` | Test cases for branch coverage |

## Implementation and Testing

### 1. Code Coverage Analysis

Created additional test cases to execute all statements in the application, including input validation, donor eligibility, haemoglobin conditions, cohort processing, deferral handling and centrifuge verification.

**Command used:**

```bash
python -m coverage erase
python -m coverage run -m pytest CodeCoverageTest_blood_donation_screening.py
python -m coverage report -m blood_donation_screening.py
```

**Result:**
- Tests passed: 22
- Statements: 45
- Missing statements: 0
- Code coverage: 100%

Screenshot: `screenshots/code_coverage.png`

### 2. Branch Coverage Analysis

Created additional test cases to exercise both outcomes of conditional statements and different execution paths, including donor eligibility decisions, haemoglobin limits, high-altitude processing, fast-track processing, deferral thresholds and centrifuge RPM conditions.

**Command used:**

```bash
python -m coverage erase
python -m coverage run --branch -m pytest BranchCoverageTest_blood_donation_screening.py
python -m coverage report -m blood_donation_screening.py
```

**Result:**
- Tests passed: 22
- Statements: 45
- Missing statements: 0
- Branches: 32
- Partial branches: 0
- Branch coverage: 100%

Screenshot: `screenshots/branch_coverage.png`

## Final Results

| Coverage Metric | Achieved |
|---|---:|
| Code Coverage | 100% |
| Branch Coverage | 100% |
| Code Coverage Tests | 22 passed |
| Branch Coverage Tests | 22 passed |

Both code coverage and branch coverage achieved 100%, exceeding the minimum requirement of 90%.

## Deliverables

- Original application program.
- Original test file.
- Code coverage test file.
- Branch coverage test file.
- Code coverage terminal output screenshot.
- Branch coverage terminal output screenshot.

## Git Commits

The updated code coverage test cases and branch coverage test cases are maintained in separate commits as required by the lab instructions.
