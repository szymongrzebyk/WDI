from test_zadanie_6 import SpecialNumbersTest
from zadanie_6 import isSpecial
import pytest


def test_special():
    assert isSpecial(120) == True
    assert isSpecial(2100) == False


def test_special_test():
    with pytest.raises(AssertionError):
        test_special()
