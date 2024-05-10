import fuel
import pytest
def test_convert():
    assert fuel.convert("3/4") == 75
    assert fuel.convert("99/100") == 99
    assert fuel.convert("1/100") == 1


def test_guage():
    assert fuel.gauge(75) == "75%"
    assert fuel.gauge(99) == "F"
    assert fuel.gauge(1) == "E"

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        fuel.convert("1/0")

def test_ValueError():
    with pytest.raises(ValueError):
        fuel.convert("cat/dog")
