from zadanie_1 import euklides
import pytest


def test_getNumber():
    assert euklides(15, 3) == 2
    assert euklides(100, 243) == 1


def test_getNumber_test():
    with pytest.raises(AssertionError):
        test_getNumber()
