import unittest

"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true
"""

def isValid(input_string):



class TestParenthesesStrings(unittest.TestCase):

    def test_base_case_valid(self):
        self.assertEqual(isValid("()"), True)

    def test_base_case_invalid(self):
        self.assertEqual(isValid("(]"), False)

if __name__ == '__main__':

    unittest.main()

