import pytest
from src.grade_calculator import calculate_grade

def test_A_plus():
    grade = calculate_grade([95, 90, 92, 94, 93])
    assert grade == "A+"

