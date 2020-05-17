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
            return ""
        if len(strs) == 1:
            return strs[0]

        latest_match_index = -1

        smallest_word_length = min([len(x) for x in strs])
        i = 0

        while i < smallest_word_length:
            current_char = strs[0][i]
            for word in strs[1:]:
                if word[i] != current_char:
                    return strs[0][:latest_match_index + 1]
            latest_match_index += 1
            i += 1

        if latest_match_index >= 0:
            return strs[0][:latest_match_index + 1]
        return ""

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

    def test_no_match(self):
        input = ['aca','cba']
        self.assertEqual(self.sol.longestCommonPrefix(input), '')

if __name__ == '__main__':
    unittest.main()
