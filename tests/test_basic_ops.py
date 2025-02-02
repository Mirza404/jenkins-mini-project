# test_main.py

from functions.basic_operations import add, subtract, multiply, divide

def test_add():
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert add(-1, -1) == -2

def test_subtract():
    assert subtract(2, 1) == 1
    assert subtract(-1, 1) == -2
    assert subtract(-1, -1) == 0

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-1, 1) == -1
    assert multiply(-1, -1) == 1

def test_divide():
    assert divide(6, 3) == 2
    assert divide(-1, 1) == -1
    assert divide(-1, -1) == 1
    assert divide(5, 0) == "Error: Division by zero is not allowed."