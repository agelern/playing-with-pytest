from lib.counter import *

def test_adds_numbers():
    county = Counter()
    county.add(2)
    assert county.count == 2
    county.count = 0
    county.add(0)
    assert county.count == 0

def test_returns_single_entries():
    county = Counter()
    county.add(5)
    assert county.report() == "Counted to 5 so far."

def test_adds_correctly():
    county = Counter()
    county.add(2)
    county.add(6)
    county.add(200)
    assert county.report() == "Counted to 208 so far."