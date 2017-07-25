"""
test for the math.py module
"""


import fcm
import pytest


def test_add():
    assert fcm.math.add(5,2) == 7 
    assert fcm.math.add(2,5) == 7

testdata = [
    (2, 5, 10),
    (1, 2, 2 ),
    (11, 9, 99)
]
@pytest.mark.parametrize("a,b,expected", testdata)
def test_mult(a, b, expected):
    assert fcm.math.mult(a, b) == expected
