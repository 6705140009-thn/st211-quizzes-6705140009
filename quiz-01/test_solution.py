import pytest
from solution import letter_grade


def test_letter_grade_valid_scores():
    assert letter_grade(85) == "A"
    assert letter_grade(75) == "B"
    assert letter_grade(65) == "C"
    assert letter_grade(50) == "F"


def test_letter_grade_boundaries():
    assert letter_grade(80) == "A"
    assert letter_grade(70) == "B"
    assert letter_grade(60) == "C"


def test_letter_grade_invalid_scores():
    with pytest.raises(ValueError, match="Score must be 0-100"):
        letter_grade(-1)
    with pytest.raises(ValueError, match="Score must be 0-100"):
        letter_grade(101)