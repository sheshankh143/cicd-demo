from calculator import add 
import pytest
from calculator import substraction
def test_add():
    assert add(5, 3) == 8
def test_substraction():
    assert substraction(6,2)==4