"""Tests for candidate 3: multiply() bug."""

import pytest
from calculator import add, multiply, divide, square


class TestCandidate3:
    """Test candidate 3 fixes."""

    def test_add(self):
        """Test addition works correctly."""
        assert add(2, 3) == 5

    def test_multiply(self):
        """Test multiplication - multiply() has a bug."""
        assert multiply(3, 4) == 12

    def test_square(self):
        """Test squaring a number."""
        assert square(5) == 25
