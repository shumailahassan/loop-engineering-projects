"""Simple calculator module with intentional bugs for Project 5."""


def add(a, b):
    """Add two numbers and return the result."""
    return a + b


def multiply(a, b):
    """Multiply two numbers and return the result."""
    return a * b


def divide(a, b):
    """Divide a by b and return the result.

    Bug: Returns a * b instead of a / b.
    """
    return a / b


def square(x):
    """Return the square of a number."""
    return x * x
