import pytest
from lib.improve_grammar import *
"""Given a text of "Hello, there!"
Returns = True"""

def test_improve_grammar():
    text = "Hello, there!"
    result = improve_grammar(text)
    assert result == True

"""Given a text of "Hello world,"
Return = False"""

def test_with_capital_letter_no_mark():
    text = 'Hello world'
    result = improve_grammar(text)
    assert result == False

"""Given a text of "hi, what is your name"
Return = False"""

def test_no_capital_letter_no_mark():
    text = "hi, what's your name"
    result = improve_grammar(text)
    assert result == False

"""Given a text of "hello world!"
Return = False"""

def test_no_capital_with_mark():
    text = 'hello world!'
    result = improve_grammar(text)
    assert result == False