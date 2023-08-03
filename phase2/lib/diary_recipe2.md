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
    pass

class DiaryEntry():
    pass

class TaskList():
    pass

class Task:
    pass

class PhoneNumberExtractor():
    pass


class ReadableEntryFinder():
    pass


3. Create Examples as Integration Tests
Create examples of the classes being used together in different situations and combinations that reflect the ways in which the system will be used.

# EXAMPLE

"""
list past diary entries 
return as a list

"""

"""

"""

"""

"""

4. Create Examples as Unit Tests
Create examples, where appropriate, of the behaviour of each relevant class at a more granular level of detail.

# EXAMPLE

"""

"""


5. Implement the Behaviour
After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour.


