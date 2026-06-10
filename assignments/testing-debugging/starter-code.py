"""Starter Code for Automated Testing and Debugging in Python"""

# Task 1: Implement Testable Functions

def add_numbers(a, b):
    """Return the sum of two numbers."""
    return a + b


def is_even(number):
    """Return True if the number is even, otherwise False."""
    return number % 2 == 0


def find_max(values):
    """Return the maximum value from a list."""
    if not values:
        raise ValueError("The list must contain at least one value")
    return max(values)


def divide_numbers(a, b):
    """Return the quotient of a divided by b."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


# Task 2: Create Automated Tests

# Students should create the test suite in a separate file named test_suite.py.


# Task 3: Debug and Fix a Broken Function

# The function above already includes proper checks for dividing by zero,
# but students should inspect and verify the implementation using debugging.
