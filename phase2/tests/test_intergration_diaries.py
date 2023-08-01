from lib.diary import Diary
from lib.diary_entry_week4 import DiaryEntry
import pytest
''' 
so we first test that entries are in the diary 
this will show us that diaryentry __init__
works and diary add method works
'''
def test_init_and_add():
    first = DiaryEntry('Go Study!', 'Golden Square')
    second = DiaryEntry('Go Home', 'Junction')
    diary = Diary()
    diary.add(first)
    diary.add(second)
    
    assert diary.all() == [first, second]

def test_count_words_d_entry():
    first = DiaryEntry('Go Study!', 'Golden Square')
    diary = Diary()
    diary.add(first)
    assert first.count_words() == 2
    first = DiaryEntry('Go Study!', 'Golden Square happy days')
    diary = Diary()
    diary.add(first)
    assert first.count_words() == 4


def test_count_words_all():
    diary = Diary()
    first = DiaryEntry('Go Study!', 'Golden Square happy')
    diary.add(first)
    first.count_words() 
    assert diary.count_words() == 3


def test_reading_time():
    diary = Diary()
    first = DiaryEntry('Go Study!', 'Golden Square happy')
    diary.add(first)
    first.count_words()
    assert first.reading_time(3) == 1