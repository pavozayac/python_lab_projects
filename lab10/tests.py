from ulamek import Fraction
import pytest
from unittest.mock import mock_open, MagicMock

def test_nonzero_denominator():
    with pytest.raises(AssertionError):
        f = Fraction(821, 0)

@pytest.mark.parametrize('a, b, expected', [
    [Fraction(2, 9), Fraction(1, 8), Fraction(25, 72)],
    [Fraction(2, -9), Fraction(1, 8), Fraction(-7, 72)],
    [Fraction(1, 6), Fraction(1, 6), Fraction(2, 6)],
    [Fraction(-1, 9), Fraction(-2, 8), Fraction(-13, 36)],
])
def test_add(a, b, expected):
    assert a + b == expected

@pytest.mark.parametrize('a, b, expected', [
    [Fraction(2, 9), Fraction(1, 8), Fraction(7, 72)],
    [Fraction(2, -9), Fraction(1, 8), Fraction(-25, 72)],
    [Fraction(1, 6), Fraction(1, 6), Fraction(0, 6)],
    [Fraction(-1, 9), Fraction(-2, 8), Fraction(5, 36)],
])
def test_sub(a, b, expected):
    assert a - b == expected

@pytest.mark.parametrize('a, b, expected', [
    [Fraction(2, 9), Fraction(1, 8), Fraction(1, 36)],
    [Fraction(2, -9), Fraction(1, 8), Fraction(-3, 108)],
    [Fraction(1, 6), Fraction(1, 6), Fraction(1, 36)],
    [Fraction(-1, 9), Fraction(-2, 8), Fraction(2, 72)],
])
def test_mul(a, b, expected):
    assert a * b == expected

@pytest.mark.parametrize('a, b, expected', [
    [Fraction(2, 9), Fraction(1, 8), Fraction(32, 18)],
    [Fraction(2, -9), Fraction(1, 8), Fraction(-16, 9)],
    [Fraction(1, 6), Fraction(1, 6), Fraction(333, 333)],
    [Fraction(-1, 9), Fraction(-2, 8), Fraction(8, 18)],
])
def test_div(a, b, expected):
    assert a / b == expected

@pytest.mark.parametrize('a, b', [
    [Fraction(1, 9), Fraction(6, 54)], 
    [Fraction(-1, 2), Fraction(4, -8)],
    [Fraction(33, 33), Fraction(55, 55)], 
])
def test_eq(a, b):
    assert a == b

@pytest.mark.parametrize('a, b', [
    [Fraction(1, 9), Fraction(6, 53)], 
    [Fraction(1, 2), Fraction(4, -8)],
    [Fraction(33, 33), Fraction(56, 55)], 
])
def test_neq(a, b):
    assert a != b

@pytest.mark.parametrize('a, b', [
    [Fraction(1, 9), Fraction(1, 8)], 
    [Fraction(3, 9), Fraction(4, 9)],
    [Fraction(-4, 3), Fraction(-5, 4)], 
    [Fraction(-1, 9), Fraction(0, 8)],
])
def test_lt(a, b):
    assert a < b

@pytest.mark.parametrize('a, b', [
    [Fraction(1, 8), Fraction(1, 9)], 
    [Fraction(4, 9), Fraction(3, 9)],
    [Fraction(-5, 4), Fraction(-4, 3)], 
    [Fraction(0, 8), Fraction(-1, 9)],
])
def test_gt(a, b):
    assert a > b

@pytest.mark.parametrize('a, b', [
    [Fraction(1, 9), Fraction(1, 9)], 
    [Fraction(3, 9), Fraction(4, 9)],
    [Fraction(-3, 1), Fraction(-6, 2)], 
    [Fraction(-1, 9), Fraction(0, 8)],
])
def test_lte(a, b):
    assert a <= b

@pytest.mark.parametrize('a, b', [
    [Fraction(1, 8), Fraction(1, 8)], 
    [Fraction(4, 9), Fraction(3, 9)],
    [Fraction(-5, 4), Fraction(-4, 3)], 
    [Fraction(0, 8), Fraction(0, 9)],
])
def test_gte(a, b):
    assert a >= b

@pytest.mark.parametrize('a, expected', [
    [Fraction(2, 16), '1 / 8'], 
    [Fraction(12, 27), '4 / 9'],
    [Fraction(-5, 4), '-5 / 4'], 
    [Fraction(0, 8), '0'],
    [Fraction(388, 388), '1 / 1'],
])
def test_str(a, expected):
    assert str(a) == expected

@pytest.mark.parametrize('a, expected', [
    ['1 / 8 ', Fraction(1, 8)], 
    ['-2   /  7', Fraction(-2, 7)], 
    ['0 / 5', Fraction(0, 5)], 
])
def test_from_str(a, expected):
    assert Fraction.from_str(a) == expected

def test_from_str_missing_field():
    with pytest.raises(ValueError):
        Fraction.from_str('0 / ')
        
def test_from_str_non_integer():
    with pytest.raises(ValueError):
        Fraction.from_str('0 / hello')

def test_from_str_zero_denominator():
    with pytest.raises(AssertionError):
        Fraction.from_str('1 / 0')

def test_read_file():
    mock_data = ' 1   / 2'

    m = mock_open(read_data=mock_data)

    with pytest.raises(FileNotFoundError):
        Fraction.from_file('abcdeffubar.txt')

    with pytest.MonkeyPatch.context() as context:
        context.setattr('builtins.open', m)

        fraction = Fraction.from_file('anyfile.json')
    
    m.assert_called_once_with('anyfile.json', 'r')

    assert fraction == Fraction(1, 2)

def test_write_file():
    f = Fraction(1, 2)

    m = mock_open()

    with pytest.MonkeyPatch.context() as context:
        context.setattr('builtins.open', m)

        f.save_to_file('anyfile.json')

    
    m.assert_called_once_with('anyfile.json', 'w')
    m().write.assert_called_once_with('1 / 2')
