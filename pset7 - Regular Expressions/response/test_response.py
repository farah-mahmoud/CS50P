from response import validate

def test_right_validate():
    assert validate("farah.farooh2003@gmail.com") == "valid"
    assert validate("farahmahmoud031@gmail.com") == "valid"
    assert validate(" farahmahmoud031@gmail.com") == "valid"
    assert validate("farah.fouad03@eng-st.cu.edu.eg") == "valid"
    assert validate("DavidjMalan@harvard.edu") == "valid"
    assert validate("farah@outlook.com") == "valid"
    assert validate("_@gmail.com") == "valid"

def test_wrong_validate():
    assert validate("FARAH.FAROOH2003@GMAIL.COM") == "Invalid"
    assert validate("farah@@@@gmail.com") == "Invalid"
    assert validate("farah@gmail..com") == "Invalid"
    assert validate("farah @ gmail. com") == "Invalid"
    assert validate("farah@") == "Invalid"
    assert validate("") == "Invalid"
    assert validate("farah") == "Invalid"
    assert validate("@gmail.com") == "Invalid"
    assert validate("@") == "Invalid"
    assert validate(".net") == "Invalid"
    assert validate("_@_._") == "Invalid"

