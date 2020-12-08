import pytest
from calc_lean import add

def test_method1():
    assert add(3,5) == 8

def test_method2():
    assert add(15,5) == 21 