import pytest
from lib.count_words import *

def test_count_words():
    result = count_words('Hello, how are you doing today?')
    assert result == 6