# 📘 Assignment: Automated Testing and Debugging in Python

## 🎯 Objective

Practice writing automated tests and using debugging techniques to verify and improve Python code.

## 📝 Tasks

### 🛠️ Implement Testable Functions

#### Description
Write functions that perform simple operations and make them easy to test.

#### Requirements
Completed program should:

- Define functions `add_numbers(a, b)`, `is_even(number)`, `find_max(values)`, and `divide_numbers(a, b)`.
- Use clear names and docstrings for each function.
- Handle invalid input or edge cases with appropriate errors.

### 🛠️ Create Automated Tests

#### Description
Build a test suite that checks your functions automatically and ensures they behave correctly.

#### Requirements
Completed program should:

- Include a `test_suite.py` file using Python's built-in `unittest` module.
- Test each function with at least two different cases.
- Include tests for edge cases such as an empty list and division by zero.
- Run automatically with `python -m unittest test_suite.py`.

### 🛠️ Debug and Fix a Broken Function

#### Description
Use debugging tools to inspect a faulty function, find the bug, and correct it.

#### Requirements
Completed program should:

- Identify the bug in the provided `divide_numbers` implementation.
- Use `print()` statements or the Python debugger to trace values.
- Fix the code so that the test suite passes.
