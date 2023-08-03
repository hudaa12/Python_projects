from lib.todo import *
from lib.todo_list import *

## 1 - Check a new instance doesn't have any TODOS
def test_empty_todo_list():
    todo = TodoList()
    # assert todo.incomplete() == []


def test_add():
    todo_list = TodoList()
    todo1 = Todo("Buy groceries")
    todo2 = Todo("Finish homework")

    todo_list.add(todo1)
    todo_list.add(todo2)

    assert len(todo_list.tasks) == 2
    assert todo1 in todo_list.tasks
    assert todo2 in todo_list.tasks

def test_incomplete():
    todo_list = TodoList()
    todo_list.todos = [
        Todo("Task 1", is_complete=True),
        Todo("Task 2"),
        Todo("Task 3", is_complete=True),
        Todo("Task 4"),
        Todo("Task 5"),
    ]
    incomplete_todos = todo_list.incomplete()
    expected_incomplete = [todo for todo in todo_list.todos if not todo.is_complete]
    assert incomplete_todos == expected_incomplete, "Test failed! Incomplete todos don't match expected."


def test_complete():
    todo_list = TodoList()
    todo_list.todos = [
        Todo("Task 1", is_complete=True),
        Todo("Task 2"),
        Todo("Task 3", is_complete=True),
        Todo("Task 4"),
        Todo("Task 5"),
    ]
    complete_todos = todo_list.complete()
    expected_complete = [todo for todo in todo_list.todos if todo.is_complete]
    assert complete_todos == expected_complete, "Test failed! Complete todos don't match expected."

def test_give_up():
    todo_list = TodoList()
    todo1 = Todo("Buy groceries")
    todo2 = Todo("Finish homework")

    todo_list.add(todo1)
    todo_list.add(todo2)

    todo_list.give_up()

    assert todo1.mark_complete() == True
    assert todo2.mark_complete() == True
