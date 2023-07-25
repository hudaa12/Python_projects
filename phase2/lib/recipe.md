{{PROBLEM}} Function Design Recipe
# Extract Uppercase method Design recipe 

1. Describe the Problem
Put or write the user story here. Add any clarifying notes you might have.

> As a user
> So that I can manage my time
> I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute.


2. Design the Function Signature
Include the name of the function, its parameters, return value, and side effects.

```python
def estimate_reading_time(text)
# parameters:
#  text: a string representing human-readable text
# return:
#   a float representing a reading time



## 3. Create Examples as Tests
_Make a list of examples of what the function will take and return._

```python
"""
Given a text of 200 words
It will return a reading time of 1
"""
estimate_reading_time("...200...")
# => 1.0

"""
Given a text of 400 words 
It will return a reading time of 2
"""
estimate_reading_time("..400..")
# => 2.0

"""
Given a text of 300 words
It will return a reading of 1.5
"""
estimate_reading_time("...300...")
# => 1.5

"""
Given an empty text
it will raise and error
"""
estimate_reading_time("")
# raises error: "Can't estimate reading time for an empty text."
```

_Encode each example as a test. You can add to the above list as you go._

4. Implement the Behaviour
After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour.

Here's an example for you to start with:


