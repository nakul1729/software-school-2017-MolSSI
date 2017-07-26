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


def test_subs():
    assert ss.math.subs(10, 2) == 8
    assert ss.math.subs(2, 10) == -8



"""
testdata = [
	(2, 5, 10),
	

]
@pytest.mark.parameterize("a, b, expected",testdata)

Test multiplications or operations here

"""
