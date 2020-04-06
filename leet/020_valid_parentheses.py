import unittest

"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.
"""

def is_valid(input_string):

    paren_stack = []
    paren_dict = { "(": ")", "{": "}", "[": "]" }

    for char in input_string:
        if char in ["(", "[", "{"]:
            paren_stack.append(char)
        elif len(paren_stack) and char == paren_dict[paren_stack[-1]]:
            paren_stack.pop()
        else:
            return False
    if len(paren_stack) != 0:
        return False

    return True


class TestParenthesesStrings(unittest.TestCase):

    def test_base_case_valid(self):
        self.assertEqual(is_valid("()"), True)

    def test_base_case_invalid(self):
        self.assertEqual(is_valid("(]"), False)

    def test_one_of_each_pair(self):
        self.assertEqual(is_valid("()[]{}"), True)

    def test_interwoven_pairs(self):
        self.assertFalse(is_valid("([)]"))

    def test_nested_pairs(self):
        self.assertTrue(is_valid("{[]}"))

    def test_single_right_side_input(self):
        self.assertFalse(is_valid("]"))

if __name__ == '__main__':

    unittest.main()

