from lib.check_codeword import *

def test_check_codeword_horse():
    result = check_codeword('horse')
    assert result == "Correct! Come in."

def test_check_codeword_close():
    close_words = ['hose', 'house', 'homie', 'hope', 'he']
    for word in close_words:
        assert check_codeword(word) == "Close, but nope."

def test_check_codeword_wrong():
    wrong_words = ['haha', 'what', 'even', 'are', 'these', 'words']
    for word in wrong_words:
        assert check_codeword(word) == "WRONG!"