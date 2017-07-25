"""
test for the math.py module
"""


import fcm
import pytest


def test_add():
    assert fcm.math.add(5,2) == 7 
    assert fcm.math.add(2,5) == 7
def test_mult():
    assert fcm.math.mult(5,2) == 10
    assert fcm.math.mult(2,5) == 10
