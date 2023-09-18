from lib.string_builder import *

def test_init():
    buildy = StringBuilder()
    assert buildy.str == ""

def test_add():
    buildy = StringBuilder()
    buildy.add('Lorem')
    assert buildy.str == 'Lorem'
    buildy.add(' ipsum')
    assert buildy.str == 'Lorem ipsum'

def test_size():
    buildy = StringBuilder()
    test_words = [
        'hello',
        'floopty',
        'goodbye',
        '12345678901234567890'
    ]
    for word in test_words:
        buildy.str = word
        assert buildy.size() == len(word)

def test_output():
    buildy = StringBuilder()
    buildy.str = 'floopty'
    assert buildy.output() == 'floopty'

def test_all():
    buildy = StringBuilder()
    buildy.add('floopty')
    buildy.add(' poopty')
    assert buildy.size() == 14
    assert buildy.output() == 'floopty poopty'