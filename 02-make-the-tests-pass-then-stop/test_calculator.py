"""Minimal failing tests for the calculator exercise."""

import unittest
from calculator import add, subtract, multiply


class TestCalculator(unittest.TestCase):
    """Test basic arithmetic operations."""

    def test_add_two_numbers(self):
        """Adding 2 + 3 should return 5."""
        self.assertEqual(add(2, 3), 5)

    def test_subtract_two_numbers(self):
        """Subtracting 10 - 4 should return 6."""
        self.assertEqual(subtract(10, 4), 6)

    def test_multiply_two_numbers(self):
        """Multiplying 3 * 7 should return 21."""
        self.assertEqual(multiply(3, 7), 21)


if __name__ == "__main__":
    unittest.main()
