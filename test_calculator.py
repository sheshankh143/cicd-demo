from calculator import add 
import pytest
from calculator import substraction
from calculator import multiplication
def test_add():
    assert add(5, 3) == 8
def test_substraction():
    assert substraction(6,2)==4
def test_mul():
    assert multiplication(2,3)==6
