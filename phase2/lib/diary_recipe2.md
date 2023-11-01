{{PROBLEM}} Multi-Class Planned Design Recipe
1. Describe the Problem
Put or write the user story here. Add any clarifying notes you might have.

As a user
So that I can record my experiences
I want to keep a regular diary

As a user
So that I can reflect on my experiences
I want to read my past diary entries

As a user
So that I can reflect on my experiences in my busy day
I want to select diary entries to read based on how much time I have and my reading speed

As a user
So that I can keep track of my tasks
I want to keep a todo list along with my diary

As a user
So that I can keep track of my contacts
I want to see a list of all of the mobile phone numbers in all my diary entries


2. Design the Class System
Consider diagramming out the classes and their relationships. Take care to focus on the details you see as important, not everything. The diagram below uses asciiflow.com but you could also use excalidraw.com, draw.io, or miro.com

# verbs 
Record 
Read 
Keep 
reflect 
select 
Keep
See a list
Mark complete
List complete
list incomplete
Add
# nouns
Diary
Dairy entries
Experience
Time
Reading speed
Todo List
Tasks
Phone numbers 
List of phone numbers


┌────────────────────────────┐
│ Diary                      │
│                            │
│ -  │
│ -                          │
│ -        │
│   => [tracks...]           │
└───────────┬────────────────┘
            │
            │ owns a list of
            ▼
┌─────────────────────────┐   
│ DiaryEntry              │
│                         │
│ -                       │
│ -                       │
│ -                       │
│                         │
└─────────────────────────┘
            │
            │ owns a list of
            ▼
┌─────────────────────────┐
│ PhoneNumber             │
│                         │
│ -                       │
│ -                       │
│ -                       │
│                         │
└─────────────────────────┘

┌─────────────────────────┐
│ TaskList       │
│                         │
│ -                       │
│ -                       │
│ -                       │
│                         │
└─────────────────────────┘
            │
            │ owns a list of
            ▼

┌─────────────────────────┐
│ Task             │
│                         │
│ -                       │
│ -                       │
│ -                       │
│                         │
└─────────────────────────┘
Also design the interface of each class in more detail.

class Diary:
    def add(self, diary_entry):
        # diary_entry: instance of DiaryEntry
        # returns nothing
        # side-effects: adds to list of diary entries
        pass

    def all(self):
        # returns all DiaryEntry instances
        pass

class DiaryEntry():
    # public properties
        # title: a string representing an entry title
        # contents: a string representing entry contents
    
    def __init__(self, title, contents)
        # title: a string representing an entry title
        # contents: a string representing entry contents
        # side-effects: sets the above properties
        pass


class TaskList():
    def add(self, task)
        # task: an instance of task 
        # returns nothing
        # side-effect: adds to list of tasks
        pass

    def all _incomplete(self):
        #   returns a list of instances of task
        #   representing the incomplete tasks
        pass 

    def all_complete(Self):
        #   returns a list of instances of task
        #   representing the complete tasks
        pass
    
    
    
class Task():
    # public properties
    # title: a string representing a job to do
    def __init__(self, job):
        # title: astring representing a job to do
        # side-effect: sets title property
    pass

    def mark_complete(self):
        # side-effect: marks the task as complete
        # returns nothing 
    pass

class PhoneNumberExtractor():
def __init__(Self, diary):
    # diary: an instance of Diary
    # side-effect: set diary property
    pass

    def extract(self):
    # diary: an instances of diary 
    # returns a list if strings representing
    # a list of phone numbers
    pass


class ReadableEntryFinder():
def __init__(Self, diary):
    # diary: an instance of Diary
    # side-effect: set diary property
    pass

    def extract(self, wpm, minutes):
    # wpm: integer
    # minutes: integer
    # returns the longest diary entry that can be read
    # in the time given the wpm and minutes 
    pass

    # 
    pass

3. Create Examples as Integration Tests
Create examples of the classes being used together in different situations and combinations that reflect the ways in which the system will be used.

# EXAMPLE

"""
when i add multiple diary entries
all lists them out in order they were added
"""
diary  = Diary()
entry_1 = DiaryEntry("My title , "My contents 1")
entry_2 = DiaryEntry("My title , "My contents 2")
entry_3 = DiaryEntry("My title , "My contents 3")
diary.add(entry1)
diary.add(entry2)
diary.add(entry3)
diary.all() # => [entry_1, entry_2, entry_3]
"""

"""
when i add multiple tasks
and i dont mark any complete  
all_incomplete lists them out in order they were added
"""
task_lsit = TaskList()
task_1 = Task("Walk the horse")
task_2 = Task("Walk the dog")
task_3 = Task("Walk the cat")
task_list.add(task_1)
task_list.add(task_2)
task_list.add(task_3)
task_list.all_incomplete() # => [task_1, task_2, task_3]

"""
when i add multiple tasks
And i mark one is complete 
all_incomplete only lists the incomplete tasks
"""
task_lsit = TaskList()
task_1 = Task("Walk the horse")
task_2 = Task("Walk the dog")
task_3 = Task("Walk the cat")
task_list.add(task_1)
task_list.add(task_2)
task_list.add(task_3)
task_2.mark_complete()
task_list.all_incomplete() # => [task_1, task_3]


"""
when i add multiple tasks
And i mark one is complete 
all_complete only lists the complete tasks
"""
task_lsit = TaskList()
task_1 = Task("Walk the horse")
task_2 = Task("Walk the dog")
task_3 = Task("Walk the cat")
task_list.add(task_1)
task_list.add(task_2)
task_list.add(task_3)
task_2.mark_complete()
task_list.all_complete() # => [task_2]


"""
when i add multiple diary entries
And I call Phone
"""
diary  = Diary()
entry_1 = DiaryEntry("My title , "My contents 1")
entry_2 = DiaryEntry("My title , "My contents 2")
entry_3 = DiaryEntry("My title , "My contents 3")
diary.add(entry1)
diary.add(entry2)
diary.add(entry3)
diary.all() # => [entry_1, entry_2, entry_3]





"""

4. Create Examples as Unit Tests
Create examples, where appropriate, of the behaviour of each relevant class at a more granular level of detail.

# EXAMPLE

"""
Initially, dIARY HAS NO ENTRIES
"""
diary =  Diary()
diray.all() # => []

# DiaryEntry
"""
diaryEntry is constructed with a title and contents
"""

entry = DiaryEntry("My title", "My contents")
entry.title # => "My title"
entry.contents # => "My contents"

# TaskList 
"""
Inititally, TaskList has no incomplete tasks
"""
task_lsit = TaskList()
taski_list.all_incomplete() # => []


# TaskList 
"""
Inititally, TaskList has no complete tasks
"""
task_lsit = TaskList()
taski_list.all_incomplete() # => []







# Task
"""
Task constructs with a title
"""
task = Task("Walk the horse")
task.title # => "Walk the horse"

5. Implement the Behaviour
After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour.


