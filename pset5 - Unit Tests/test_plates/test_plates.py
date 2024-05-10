from plates import is_valid

def test_rule1():
    assert is_valid("hello") == True
    assert is_valid("HEllp") == True
    assert is_valid("1ello") == False
    assert is_valid("%ello") == False

def test_rule2():
    assert is_valid("h") == False
    assert is_valid("platessss") == False

def test_rule3():
    assert is_valid("AAA222") == True
    assert is_valid("AB22A") == False
    assert is_valid("Ab02") == False

def test_rule4():
    assert is_valid("hell.o") == False
    assert is_valid("hell o") == False
    assert is_valid("hell/o") == False
