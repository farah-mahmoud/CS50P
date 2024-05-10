from um import count

def test_um():
    assert count("") == 0
    assert count("um") == 1
    assert count("UM") == 1 #capitalized
    assert count("hi, um, how is it going?") == 1
    assert count("um.") == 1 #dot
    assert count("ummmmmm") == 0
    assert count("yummy humburger") == 0
    assert count("This summer um is hot") == 1
    assert count("Um hi") == 1
    assert count("um UM Um uM") == 4
    assert count("um9 20um um") == 1
    assert count("um?") == 1
    assert count("umumumum") == 0
    assert count("u m") == 0
