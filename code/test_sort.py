import pytest
from lib.utils import *


# Pytest unit tests
@pytest.mark.parametrize("width, height, length, mass, expected", [
    (100, 100, 100, 10, "SPECIAL"),
    (200, 200, 200, 10, "SPECIAL"),
    (150, 100, 100, 10, "SPECIAL"),
    (100, 100, 100, 25, "REJECTED"),
    (200, 200, 200, 25, "REJECTED"),
    (149, 149, 149, 19.9, "SPECIAL"),
    (150, 150, 150, 20, "REJECTED"),
])
def test_sort(width, height, length, mass, expected):
    assert sort(width, height, length, mass) == expected
