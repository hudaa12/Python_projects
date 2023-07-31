1. Describe the Problem
Put or write the user story here. Add any clarifying notes you might have.

As a user
So that I can keep track of my tasks
I want a program that I can add todo tasks to and see a list of them.

As a user
So that I can focus on tasks to complete
I want to mark tasks as complete and have them disappear from the list.

2. Design the Class Interface
Include the initializer, public properties, and public methods with all parameters, return values, and side-effects.
class track_tasks():
    def add(self, task):
        # Parameters:
        #   task: string, representing a task
        pass # No code here yet

def list_incomplete(self):
        # Returns: a list of incomplete tasks
        # Side-effects: none
        pass # No code here yet

def mark_complete(self):
        # parameters: 
        #   index: an integer representing the task to complete
        # Side-effects:
        #   removes the task at index from the list of tasks 
        pass # No code here yet


3. Create Examples as Tests
Make a list of examples of how the class will behave in different situations.
Encode each example as a test. You can add to the above list as you go.

# EXAMPLE

"""
initially, there are no taks 
"""
tracker = TrackTasks()
tracker.list_incomplete() # => []

"""
when we add a task
it is reflected in the list of tasks
"""
tracker = TrackTasks()
tracker.add("walk the dog")
tracker.list_incomplete() # => ["walk the dog"]

"""
When we add multiple tasks
and mark the one as complete
it disappears from the task list 
"""
tracker = trackTasks()
tracker.add("walk the dog")
tracker.add("walk the cat")
tracker.add("walk the horse")
tracker.mark_complete(1)
tracker.list_incomplete() 
    # => ["walk the dog, walk the horse"]

"""
If we try to mark a track complete that does not exist (too low)
It raises an error
"""
tracker = trackTasks()
tracker.add("walk the dog")
tracker.mark_complete(-1) # it raises an error "No such task to mark complete"
tracker.list_incomplete() # => ["walk the dog"]


"""
If we try to mark a track complete that does not exist (too high)
It raises an error
"""
tracker = trackTasks()
tracker.add("walk the dog")
tracker.mark_complete(2) # it raises an error "No such task to mark complete"
tracker.list_incomplete() # => ["walk the dog"]



4. Implement the Behaviour
After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour.