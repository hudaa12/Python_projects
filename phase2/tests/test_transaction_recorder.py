# from lib.transaction_recorder import TransactionsRecorder

# def test_list_transactions_empty():
#     recorder = TransactionsRecorder()
#     assert recorder.list_transactions() == {}



# def test_add_transaction_list_transaction():
#     recorder = TransactionsRecorder()
#     recorder.add_transaction('Red jumper', 9.99)
#     assert recorder.list_transactions() == {'Red jumper': 9.99}
#     recorder.add_transaction("Yellow cap", 9.99)
#     assert recorder.list_transactions() == {'Red jumper: 9.99', 'Yellow cap: 6.99'}