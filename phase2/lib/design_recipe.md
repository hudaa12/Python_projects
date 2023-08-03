# Transactions Recorder Class Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As a user
So I can track my transactions from selling second hand things
I want a program that I can add transactions to and see a list of them
(With their name and amount)

As a user
So I can track how much I made
I want to see the total amount of all transactions

As a user
So I can know the more expensive things I've sold
I want to see the top 5 items that I've sold (the ones with the highest price)

Nouns: transactions, "things" / items, list, name, amount
Verbs / Actions: track, add, see / get

## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python
# EXAMPLE

class TransactionsRecorder:
    # User-facing properties:
    #   name: transactions

    def __init__(self):
        # Parameters: none
        # Side effects:
        #   Sets the transactions to an empty dictionary
        pass # No code here yet

    def list_transactions(self):
        # Parameters: none
        # Returns the transactions

    def add_transaction(self, item_name, amount):
        # Parameters: item_name (string), amount (float)
        # Side effect: add the transaction to transactions
        # Returns nothing

    def get_total_amount(self)
        # Parameters: none
        # Side effect: none
        # Returns the sum of all the transactions amounts

    def get_top_five_items(self):
        # Parameters: none
        # Side effect: none
        # Returns a dictionary of the item names and their price
        #   sorted by their 'position' from highest to lowest
        # example: { 'coat': 12, 'jacket': 24, 'socks': 4 }
```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
# EXAMPLE


"""
If list transactions method is called and
it returns an error message 
cannot show an empty list
"""
def test_list_transactions_empty():
    recorder = TransactionRecorder()
    assert recorder.list_transaction() == {}


"""
If list transaction is called it 
returns a list with items added : # example: { 'coat': 12, 'jacket': 24, 'socks': 4 } 
with name and amount 
"""
def test_add_transaction_list_transaction():
    recorder = TransactionRecoder()
    recoder.add_trnsaction("Red jumper", 9.99)
    assert recorder.list_transactions() == {'Red jumper': 9.99}

    recoder.add_trnsaction("Yellow cap", 9.99)
    assert recorder.list_transactions() == {'Red jumper': 9.99, 'Yellow cap: 6.99} 

"""
gets the total amount from recorded transactions
"""
def test_gets_total_amount():
    recoder.add_trnsaction("Red jumper", 9.99)
    recoder.add_trnsaction("Yellow cap", 9.99)
    assert recorder.list_transactions() == (6.99 + 9.99)


"""
If user tries to add a transaction with amount = 0 
it returns an error 
"""

""" 
If get_tota_amount is called when there is a list 
should return as total amount 
"""

"""
when user tries to get total amount from an amount dict 
returns and error 
"""



```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

