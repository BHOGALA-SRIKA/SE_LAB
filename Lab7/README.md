# Lab 7 – Fuzz Testing and Input Validation

Github Repo: https://github.com/BHOGALA-SRIKA/L6_L7_05_blood_donation_screening/tree/main/Lab%207


## Objective
To identify input validation bugs using fuzz testing and improve the robustness of Python functions by handling invalid, unexpected, and malformed inputs safely.

## Project Overview
This lab focuses on testing and improving three functions in `processor.py` using property-based testing with the Hypothesis library.

The functions tested are:
1. `validate_blood_type()` – Validates blood group input.
2. `calculate_pulse_pressure()` – Processes blood pressure values and calculates pulse pressure metrics.
3. `parse_donor_registry()` – Parses donor information and determines donor eligibility.

## Tools and Technologies
- Python
- Pytest
- Hypothesis
- Visual Studio Code
- Git and GitHub

## Files in This Folder

| File/Folder | Description |
|---|---|
| `processor.py` | Contains the corrected functions with input validation and error handling. |
| `test_processor.py` | Contains Hypothesis-based fuzz tests and property-based tests. |
| `Lab7_Screenshots.pdf` | PDF containing screenshots of the original application, fuzz testing failures, corrected application, and passing tests. |
| `screenshots/` | Individual execution and testing screenshots. |

## Implementation
The lab was completed in the following stages:

1. Executed the original application with sample inputs.
2. Applied fuzz testing to identify input validation issues.
3. Observed failures caused by invalid inputs such as `None`, empty strings, and malformed values.
4. Modified the functions in `processor.py` to handle invalid inputs safely.
5. Added property-based tests using Hypothesis.
6. Executed the application again and verified the corrected behaviour.

## How to Run

Install the required packages:

```bash
pip install pytest hypothesis
```

Run the application:

```bash
python processor.py
```

Run the test cases:

```bash
python -m pytest test_processor.py -v
```

## Test Results
All six test cases passed after implementing the input validation fixes.

**Final Result:** `6 passed`

## Conclusion
Fuzz testing helped identify input validation bugs in the original implementation. The functions were updated to handle invalid and unexpected inputs safely. The final Hypothesis-based tests passed successfully, demonstrating improved input handling and robustness.
