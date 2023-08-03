import pytest
from lib.track_tasks import *

"""
initially, there are no task 
"""
def test_init_has_no_tasks():
    tracker = TrackTasks()
    assert tracker.list_incomplete() == []

"""
when we add a task
it is reflected in the list of tasks
"""
def test_add_tasks():
    tracker = TrackTasks()
    tracker.add("walk the dog")
    assert tracker.list_incomplete() == ["walk the dog"]

"""
When we add multiple tasks
and mark the one as complete
it disappears from the task list 
"""
def test_add_multiple_tasks():
    tracker = TrackTasks()
    tracker.add("walk the dog")
    tracker.add("walk the cat")
    tracker.add("walk the horse")
    assert tracker.list_incomplete() == ["walk the dog", "walk the cat", "walk the horse"]

def test_mark_tasks_complete():
    tracker = TrackTasks()
    tracker.add("walk the dog")
    tracker.add("walk the cat")
    tracker.add("walk the horse")
    tracker.mark_complete(1) # it raises an error "No such task to mark complete"
    assert tracker.list_incomplete() == ["walk the dog", "walk the horse"]



"""
If we try to mark a track complete that does not exist (too low)
It raises an error
"""
def test_mark_tasks_too_low_complete():
    tracker = TrackTasks()
    tracker.add("walk the dog")
    with pytest.raises(Exception) as err:
        tracker.mark_complete(-1) # it raises an error "No such task to mark complete"
    assert str(err.value) == "No such task to mark complete"
    assert tracker.list_incomplete() == ["walk the dog"]


"""
If we try to mark a track complete that does not exist (too high)
It raises an error
"""
def test_mark_tasks_too_high_complete():
    tracker = TrackTasks()
    tracker.add("walk the dog")
    with pytest.raises(Exception) as err:
        tracker.mark_complete(1) # it raises an error "No such task to mark complete"
    assert str(err.value) == "No such task to mark complete"
    assert tracker.list_incomplete() == ["walk the dog"]