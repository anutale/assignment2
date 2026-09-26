
from app.operations import addition, division, multiplication, subtraction


def test_addition():
    assert addition(1,1) == 2

def test_subtraction():
    assert subtraction(5,3) == 2

def test_multiplication():
    assert multiplication(3,4) == 12

def test_division():
    assert division(10,2) == 5

def test_division_by_zero():
    try:
        division(10, 0)
    except ValueError as e:
        assert str(e) == "Denominator cannot be zero."
    else:
        assert False, "Expected ValueError for division by zero"