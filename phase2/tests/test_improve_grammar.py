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
