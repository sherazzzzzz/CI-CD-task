from calculator import Calculator
import pytest

calc = Calculator()
def test_add():
    assert calc.add(5,3) == 8 
def test_add_negative():
    assert calc.add(-5,3) == -2
def test_add_zero():
    assert calc.add(-5,0) == -5
def test_subtract():
    assert calc.subtract(5,3) == 2
def test_subtract_negative():
    assert calc.subtract(-5,-3) == -2
def test_multiply():
    assert calc.multiply(5,3) == 15
def test_multiply_zero():
    assert calc.multiply(5,0) == 0
def test_multiply_negative():
    assert calc.multiply(-5,-5) == 25
def test_divide_decimal():
    assert calc.divide(5,2) == 2.5
def test_divide():
    assert calc.divide(5,5) == 1
def test_divide_zero():
    assert calc.divide(0,5) == 0
def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        calc.divide(5,0)
