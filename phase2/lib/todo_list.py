# File: lib/todo_list.py
class TodoList:
    def __init__(self):
        self.tasks = []

    def add(self, todo):
        self.tasks.append(todo)

    def incomplete(self):
        return [todo for todo in self.todos if not todo.is_complete]

    
    def complete(self):
    #     # Returns:
    #     #   A list of Todo instances representing the todos that are complete
        return [todo for todo in self.todos if todo.is_complete]


    def give_up(self):
        # Returns:
        #   Nothing
        # Side-effects:
        #   Marks all todos as complete
        for todo in self.tasks:
            return todo.mark_complete()
