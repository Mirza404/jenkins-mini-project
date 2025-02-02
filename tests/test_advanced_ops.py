import math
from functions.advanced_operations import power, sqrt, log

def test_power():
    assert power(2, 3) == 8
    assert power(5, 0) == 1
    assert power(2, -2) == 0.25

def test_sqrt():
    assert sqrt(4) == 2
    assert sqrt(9) == 3
    assert sqrt(0) == 0

def test_log():
    assert log(100, 10) == 2
    assert log(math.e, math.e) == 1
    assert log(1, 10) == 0