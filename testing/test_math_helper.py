import pytest
import math_helper

def test_sum():
    assert math_helper.sum(3,8) == 11

def test_subtraction():
    assert math_helper.subtraction(7,2) == 5