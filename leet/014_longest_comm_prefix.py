"""
14. Longest Common Prefix
https://leetcode.com/problems/longest-common-prefix/

Write a function to find the longest common prefix string amongst an array of
strings.

If there is no common prefix, return an empty string "".

Note:
All given inputs are in lowercase letters a-z.
"""

from typing import List
import unittest

class Solution(object):
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if not strs:
            return ''

class Tests(unittest.TestCase):

    sol = Solution()

    def test_empty_input(self):
        self.assertEqual(self.sol.longestCommonPrefix([]), '')

    def test_example_2_no_match(self):
        input = ['dog', 'racecar', 'car']
        self.assertEqual(self.sol.longestCommonPrefix(input), '')

    def test_example_1(self):
        input = ['flower', 'flow', 'flight']
        self.assertEqual(self.sol.longestCommonPrefix(input), 'fl')

    def test_match_lee(self):
        input = ['leetcode', 'leets', 'leet', 'leeds']
        self.assertEqual(self.sol.longestCommonPrefix(input), 'lee')

if __name__ == '__main__':
    unittest.main()
