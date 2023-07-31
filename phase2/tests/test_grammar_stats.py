import pytest
from lib.grammar_stats import *

def test_valid_text():
    grammar_stats = GrammarStats()
    result = grammar_stats.check("Hello, how are you?")
    assert result is True, f"Expected True but got {result}"



# def test_percentage_good():
#     grammar_stats = GrammarStats()

#         # Test percentage for no texts checked (should be 0)
#     result_percentage_empty = grammar_stats.percentage_good()
#     assert result_percentage_empty == 0, f"Expected 0 but got {result_percentage_empty}"

#         # Test percentage for 1 text checked (should be 0% as it failed the check)
#     grammar_stats.check("this is a test.")
#     result_percentage_one_text = grammar_stats.percentage_good()
#     assert result_percentage_one_text == 0, f"Expected 0 but got {result_percentage_one_text}"

#         # Test percentage for 2 texts checked (1 passed, 1 failed)
#     grammar_stats.check("Hello, how are you?")
#     result_percentage_two_texts = grammar_stats.percentage_good()
#     assert round(result_percentage_two_texts, 2) == 50, f"Expected 50 but got {result_percentage_two_texts}"

#         # Test percentage for 3 texts checked (2 passed, 1 failed)
#     grammar_stats.check("This is a test.")
#     result_percentage_three_texts = grammar_stats.percentage_good()
#     assert round(result_percentage_three_texts, 2) == 66.67, f"Expected 66.67 but got {result_percentage_three_texts}"
import unittest

class TestGrammarStats(unittest.TestCase):
    def setUp(self):
        self.grammar_stats = GrammarStats()

    def test_percentage_good_empty_text(self):
        # Test when the text is empty, the percentage should be 0
        assert self.grammar_stats.percentage_good() == 0

    def test_percentage_good_single_pass(self):
        # Test when a single text passes the check
        self.grammar_stats.check("This is a valid sentence.")
        # The percentage should be 100% as the only text passed the check
        assert self.grammar_stats.percentage_good() == 100

    def test_percentage_good_single_fail(self):
        # Test when a single text fails the check
        self.grammar_stats.check("invalid text")
        # The percentage should be 0% as no text passed the check
        assert self.grammar_stats.percentage_good() == 0
