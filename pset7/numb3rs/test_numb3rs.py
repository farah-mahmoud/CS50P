from numb3rs import validate

def test_validate():
    assert validate('0.0.0.0') == True
    assert validate('255.255.255.255') == True
    assert validate('0.1.2.3') == True
    assert validate('1.2.3.4') == True
    assert validate('100.200.150.60') == True #random

def test_false_validate():
    assert validate(' . . . ') == False
    assert validate('') == False
    assert validate(' ') == False
    assert validate('...') == False
    assert validate('0') == False
    assert validate('0.0') == False
    assert validate('0.0.0') == False
    assert validate('256.1.2.3') == False
    assert validate('1.256.1.1') == False
    assert validate('1.1.256.1') == False
    assert validate('1.1.1.256') == False
    assert validate('1000.299.3648.482') == False
    assert validate('cat') == False
    assert validate('-1.-2.-3.-4') == False
    assert validate('1.2.3.4.5') == False
    assert validate('a.b.c.d') == False
    assert validate('True.False.True.True') == False
