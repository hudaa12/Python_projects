from lib.diary_entry import *

def test_diary_entry_initial():
    diary_entry = DiaryEntry('my day', 'today was a good day')
    assert diary_entry.title == 'my day'
    assert diary_entry.contents == 'today was a good day'
