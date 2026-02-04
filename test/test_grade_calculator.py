import pytest
from src.grade_calculator import calculate_grade

def test_A_plus():
    _, grade = calculate_grade([95, 90, 92, 94, 93])
    assert grade == "A+"

def test_A():
    _, grade = calculate_grade([75, 78, 80, 76, 77])
    assert grade == "A"

def test_B():
    _, grade = calculate_grade([60, 62, 65, 63, 64])
    assert grade == "B"

def test_C():
    _, grade = calculate_grade([50, 52, 55, 53, 54])
    assert grade == "C"

def test_fail():
    _, grade = calculate_grade([40, 45, 42, 43, 44])
    assert grade == "Fail"
