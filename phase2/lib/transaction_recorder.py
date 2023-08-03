# class TransactionsRecorder:
#     # User-facing properties:
#     #   name: transactions

#     def __init__(self):
#         self.transactions = {} 

#     def list_transactions(self):
#         return self.transactions

#     def add_transaction(self, name, amount):
#         self.transactions[name] = amount

#     def get_total_amount(self):
#         # Parameters: none
#         # Side effect: none
#         # Returns the sum of all the transactions amounts
#         return sum(self.transactions.values())

#     def get_top_five_items(self):
#         # Parameters: none
#         # Side effect: none
#         # Returns a dictionary of the item names and their price
#         #   sorted by their 'position' from highest to lowest
#         # example: { 'coat': 12, 'jacket': 24, 'socks': 4 }
#         pass