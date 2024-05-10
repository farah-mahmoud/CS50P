from working import convert
import pytest

def test1_convert():
    #normal cases
    assert convert("5:00 AM to 7:00 PM") == "05:00 to 19:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("10:00 PM to 6:00 AM") == "22:00 to 06:00"
    assert convert("9:00 PM to 5:30 AM") == "21:00 to 05:30"


def test2_convert():
    #corner cases
    assert convert("12:00 AM to 12:00 PM") == "00:00 to 12:00"
    assert convert("12:00 PM to 12:00 AM") == "12:00 to 00:00"

def test3_convert():
    #normal cases but with no minutes (None)
    assert convert("5 AM to 7 PM") == "05:00 to 19:00"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("10 PM to 6 AM") == "22:00 to 06:00"
    assert convert("9 PM to 5:30 AM") == "21:00 to 05:30"


def test4_convert():
    #Failures
    with pytest.raises(ValueError):
        convert(" to ")
    with pytest.raises(ValueError):
        convert("12:00 - 3:00 ")
    with pytest.raises(ValueError):
        convert("")
    with pytest.raises(ValueError):
        convert("12:60 AM to 7:00 PM")
    with pytest.raises(ValueError):
        convert("cat AM to dog PM")
    with pytest.raises(ValueError):
        convert("30:00 AM to 7:00 PM")
    with pytest.raises(ValueError):
        convert("10:00 AM to 80:00 PM")
