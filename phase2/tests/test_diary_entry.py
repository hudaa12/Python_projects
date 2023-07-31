import pytest
from lib.diary_entry import *

def test_diary_entry_initial():
    diary_entry = DiaryEntry('my day', 'today was a good day')
    assert diary_entry.title == 'my day'
    assert diary_entry.contents == 'today was a good day'
    result = diary_entry.format()
    assert result == "my day: today was a good day"

def test_diary_entry_count_title_contents():
    diary_entry = DiaryEntry("my day", "today was a good day")
    result = diary_entry.count_words()
    assert result == 7 


def test_reading_time_two_hundred_wpm():
    diary_entry = DiaryEntry("my day", "one two three four")
    text = " ".join(["read" for text in range(0, 200)])
    result = diary_entry.reading_time(text)
    assert result == 1

def test_reading_time_three_hundred_wpm():
    diary_entry = DiaryEntry("my day", "one two three four")
    text = " ".join(["read" for text in range(0, 300)])
    result = diary_entry.reading_time(text)
    assert result == 1.5

def test_reading_time_four_hundred_wpm():
    diary_entry = DiaryEntry("my day", "one two three four")
    text = " ".join(["read" for text in range(0, 400)])
    result = diary_entry.reading_time(text)
    assert result == 2


# def test_reading_chunk_with_two_wpm_and_two_minutes():
#     diary_entry = DiaryEntry("My day", "one two three four five six")
#     result = diary_entry.reading_chunk(2,1)
#     assert result == "one two three four"
"""
given a contents of six words 
and a wpm of 2 and 1 minute
first time, #reading_chunk(2,1) returns "one two"
Next time #reading_chunk(1,1) returns "three four"
Next time #reading_chunk(2,1) returns "five six"
"""
# def test_reading_chunk_with_two_wpm_and_one_minute_called_twice():
#     diary_entry = DiaryEntry("My day", "one two three four five six")
#     assert diary_entry.reading_chunk(2,1) == "one two"
#     assert diary_entry.reading_chunk(1,1) == "three"
#     assert diary_entry.reading_chunk(2,1) == "four five"

