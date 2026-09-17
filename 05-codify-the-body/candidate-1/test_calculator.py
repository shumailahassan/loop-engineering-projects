"""Tests for candidate 1: square() bug."""

import pytest
from calculator import add, multiply, divide, square


class TestCandidate1:
    """Test candidate 1 fixes."""

    def test_add(self):
        """Test addition works correctly."""
        assert add(2, 3) == 5

    def test_multiply(self):
        """Test multiplication works correctly."""
        assert multiply(3, 4) == 12

    def test_square(self):
        """Test squaring a number - square() has a bug."""
        assert square(5) == 25
