import pytest
from lib.estimate_reading_time import *
"""
Given a text of 200 words
It will return a reading time of 1
"""


def test_two_hundred_words():
    text = " ".join(["word" for i in range(0, 200)])
    result = estimate_reading_time(text)
    assert result == 1.0


"""
Given a text of 400 words 
It will return a reading time of 2
estimate_reading_time("..400..")
# => 2.0
"""


def test_four_hundred_words():
    text = " ".join(["word" for i in range(0,400)])
    result = estimate_reading_time(text)
    assert result == 2.0


"""
Given a text of 300 words
It will return a reading of 1.5
"""

def test_three_hundred_words():
    text = " ".join(["word" for i in range(0,300)])
    result = estimate_reading_time(text)
    assert result == 1.5

"""
Given an empty text
It will raise an error"""

def test_empty_text():
    text = ""
    with pytest.raises(Exception) as e:
        estimate_reading_time("")
    error_message = str(e.value)
    assert error_message == "Empty text"