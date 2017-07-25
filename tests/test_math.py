"""
Testing for the math.py module
"""

import sss_2017_MolSSI as ss 
import pytest

def test_add():
    assert ss.math.add(5, 2) == 7
    assert ss.math.add(2, 5) == 7
