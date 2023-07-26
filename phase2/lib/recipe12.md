1. Describe the Problem
Put or write the user story here. Add any clarifying notes you might have.

As a user
So that I can keep track of my tasks
I want to check if a text includes the string #TODO.


2. Design the Function Signature
Include the name of the function, its parameters, return value, and side effects.

def check_task_word()

parameter - text, string of readable text

return value - True if valid, False if invalid

no side effects

3. Create Examples as Tests
Make a list of examples of what the function will take and return.

Given a text with the word #TODO, return True

Given a text with a word that does not include #TODO, return False

4. Implement the Behaviour
After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour.

