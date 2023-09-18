from lib.report_length import *

def test_report_length_various():
    strings = [
        'oh my god stream of consciousness',
        'look at me',
        "I'm Mr. Meseeks",
        'random string'
    ]
    for string in strings:
        assert report_length(string) == f"This string was {len(string)} characters long."