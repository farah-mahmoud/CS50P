from bank import value

def test_value():
    assert value("hello") == 0
    assert value("hi") == 20
    assert value("no") == 100
    assert value("HELLO") == 0
    assert value("HI") == 20
    assert value("NO") == 100
    assert value("0123") == 100
    assert value("@") == 100

