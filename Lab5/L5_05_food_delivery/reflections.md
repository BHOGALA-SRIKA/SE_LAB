# Lab 5 – Static Code Analysis
## Reflection

### 1. What is static code analysis, and why is it important?

Static code analysis is the process of examining source code without executing the program. It helps identify programming errors, security vulnerabilities, code quality issues and formatting violations. It improves code reliability, readability, security and maintainability.

### 2. What did you learn from using Pylint, Bandit and Flake8?

- **Pylint:** Learned to identify code quality issues such as missing docstrings, mutable default arguments, global statements and poor naming conventions.
- **Bandit:** Learned to detect security vulnerabilities, especially unsafe pickle deserialization and improper exception handling.
- **Flake8:** Learned to identify formatting issues such as incorrect blank lines, bare exceptions and lines exceeding the recommended length.

### 3. What were the major issues identified in your program, and how did you fix them?

The major issues identified were:
- Mutable default arguments were replaced with `None`.
- Unsafe pickle serialization was replaced with JSON serialization.
- Bare exception handling was replaced with specific exception handling and input validation.
- File handling was improved using context managers and UTF-8 encoding.
- Invalid delivery statuses and unknown menu items were rejected.
- Missing docstrings, naming convention issues and formatting violations were corrected.

### 4. How did static code analysis improve your program?

Static code analysis significantly improved the quality and security of the Food Delivery Order Queue Manager. Initially, Pylint gave a score of 6.27/10, and Bandit identified three security-related findings. After fixing the issues, Pylint achieved 10.00/10, Bandit reported zero issues, and Flake8 reported zero violations. The program also continued to perform its intended operations, including order creation, status management, revenue calculation and backup restoration.
