# Day 11: File Management, Exceptions, and Leetcode Setup

### Foundational
1. **File I/O:** Explain the differences between the `r`, `w`, `a`, `r+`, and `a+` file opening modes. Why is the `with open(...) as f:` syntax considered the industry standard?
2. **Exception Hierarchy:** What is the base class for all exceptions in Python? Why is having a bare `except:` block considered bad practice?

### Deep & Tricky
3. **Try-Except-Else-Finally:** Explain the precise execution flow of a complete `try-except-else-finally` block. If the `try` block hits a `return` statement, will the `finally` block still execute?
4. **Custom Exceptions:** How do you create and raise a custom `InsufficientBalanceError` exception class inherited from Python's base `Exception`?

### Placement-Level Problem Solving
5. **Large File Processing:** You need to process a 10GB CSV file on a machine with 2GB of RAM. How do you do this using Python file management or generators to prevent a MemoryError?
6. **Robust Data Ingestion Pipeline:** Write a mock script that attempts to read data from `data.csv`. Implement robust exception handling that specifically catches `FileNotFoundError`, catches `ValueError` for type casting issues within the data, and logs any other unknown errors to a separate `error.log` file, ensuring the script does not crash the server.
