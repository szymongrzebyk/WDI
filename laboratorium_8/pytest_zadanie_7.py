from zadanie_7 import dividesOnce, jednokrotna
import pytest


def test_divisibility():
    assert dividesOnce(18, 2) == True
    assert dividesOnce(4500, 6) == False


def test_jeednokrotnosc():
    assert jednokrotna(210) == True
    assert jednokrotna(4) == False
