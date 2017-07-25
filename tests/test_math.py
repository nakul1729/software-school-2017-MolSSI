"""
Testing for the math.py module
"""

import sss_2017_MolSSI as ss 
import pytest

def test_add():
    assert ss.math.add(5, 2) == 7
    assert ss.math.add(2, 5) == 7


def test_mult():
    assert ss.math.mult(5, 2) == 10
    assert ss.math.mult(2, 5) == 10


def test_div():
    assert ss.math.div(10, 2) == 5
    assert ss.math.div(2, 10) == 0.2

