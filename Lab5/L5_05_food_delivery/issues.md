
# Lab 5 – Static Code Analysis
## Food Delivery Order Queue Manager

| Issue | Type | Line(s) | Description | Fix Approach |
|---|---|---:|---|---|
| Unsafe pickle deserialization (B301) | Security - Medium | 49 | pickle.load() can execute malicious code while restoring orders. | Replace pickle with JSON serialization and deserialization. |
| Pickle module import (B403) | Security - Low | 2 | Importing pickle introduces potential unsafe deserialization risks. | Remove pickle and use the JSON module. |
| Bare exception (E722, W0702) | Code Quality | 24 | Bare except catches every exception and hides errors. | Catch specific exceptions and handle invalid order IDs and statuses. |
| Try-except-pass (B110) | Security / Reliability - Low | 24-25 | Exceptions are silently ignored. | Validate inputs and return an explicit success or failure result. |
| Mutable default argument (W0102) | Bug | 11 | order_history=[] is shared across function calls. | Use None as the default and initialize a new list inside the function. |
| Missing file encoding (W1514) | Code Quality | 30 | File is opened without specifying an encoding. | Specify encoding="utf-8". |
| Unsafe file handling (R1732) | Code Quality | 30, 43, 49 | Files are opened without context managers. | Use with open() to ensure files close properly. |
| Broad exception handling (W0718) | Reliability | 32 | Catching Exception can hide unrelated errors. | Catch only expected file and JSON errors. |
| Invalid delivery status | Logic Bug | 27-25 | Invalid statuses such as teleported are accepted. | Validate statuses against VALID_STATUSES. |
| Unknown menu item | Logic Bug | 15 | Unknown dishes are silently assigned a price of 99. | Reject items that are not present in the menu. |
| Missing docstrings (C0114, C0116) | Maintainability | Multiple | Module and functions have no documentation. | Add module and function docstrings. |
| Naming convention (C0103) | Style | 7, 51 | next_id and printQueue do not follow appropriate naming conventions. | Use consistent naming and remove unnecessary global state. |
| Formatting violations (E302, E305, E501) | Style | Multiple | Missing blank lines and lines exceeding 79 characters. | Follow PEP 8 formatting guidelines. |
