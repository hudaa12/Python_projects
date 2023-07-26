import pytest
from lib.check_task_word import *

def test_check_task_word():
    result = check_task_word("#TODO")
    assert result == True

def test_check_no_task_word():
    result = check_task_word("No todos here")
    assert result == False