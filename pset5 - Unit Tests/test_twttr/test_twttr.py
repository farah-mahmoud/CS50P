from twttr import shorten

def test_shorten():
    assert shorten("hello") == "hll"
    assert shorten("hi!@") == "h!@"
    assert shorten("30hi4") == "30h4"
    assert shorten("HELLO") == "HLL"
