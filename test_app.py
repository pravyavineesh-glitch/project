
from app import add_numbers,subtract_numbers


def test_add_numbers():
    assert add_numbers(10, 20) == 30


def test_add_numbers_with_zero():
    assert add_numbers(10, 0) == 10

def test_subtract_numbers():
    assert subtract_numbers(10, 20) == -10

def test_subtract_numbers_with_zero():
    assert subtract_numbers(10, 0) == 10

def test_subtract_numbers_with_zero():
    assert subtract_numbers(0, 10) == -10

