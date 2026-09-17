"""Tests for candidate 2: divide() bug."""

import pytest
from calculator import add, multiply, divide, square


class TestCandidate2:
    """Test candidate 2 fixes."""

    def test_add(self):
        """Test addition works correctly."""
        assert add(2, 3) == 5

    def test_multiply(self):
        """Test multiplication works correctly."""
        assert multiply(3, 4) == 12

    def test_divide(self):
        """Test division - divide() has a bug."""
        assert divide(10, 2) == 5
