from watch import parse

def test_short_parse():
    assert parse('<iframe src="http://www.youtube.com/embed/xvFZjo5PgG0"></iframe>') == 'https://youtu.be/xvFZjo5PgG0'
    assert parse('<iframe src="https://www.youtube.com/embed/xvFZjo5PgG0"></iframe>') == 'https://youtu.be/xvFZjo5PgG0'
    assert parse('<iframe src="http://youtube.com/embed/xvFZjo5PgG0"></iframe>') == 'https://youtu.be/xvFZjo5PgG0'
    assert parse('<iframe src="https://youtube.com/embed/xvFZjo5PgG0"></iframe>') == 'https://youtu.be/xvFZjo5PgG0'
def test_long_parse():
    assert parse('<iframe width="560" height="315" src="http://www.youtube.com/embed/xvFZjo5PgG0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>') == 'https://youtu.be/xvFZjo5PgG0'
    assert parse('<iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>') == 'https://youtu.be/xvFZjo5PgG0'
    assert parse('<iframe width="560" height="315" src="http://youtube.com/embed/xvFZjo5PgG0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>') == 'https://youtu.be/xvFZjo5PgG0'
    assert parse('<iframe width="560" height="315" src="https://youtube.com/embed/xvFZjo5PgG0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>') == 'https://youtu.be/xvFZjo5PgG0'

def test_parse():
    assert parse('') == None
    assert parse('hello') == None
    assert parse('<iframe width="560" height="315" src="https://cs50.harvard.edu/python"></iframe>') == None
