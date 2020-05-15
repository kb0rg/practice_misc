"""
859. Buddy Strings
https://leetcode.com/problems/buddy-strings/

Given two strings A and B of lowercase letters, return true if and only if we
can swap two letters in A so that the result equals B.

Note:

0 <= A.length <= 20000
0 <= B.length <= 20000
A and B consist only of lowercase letters.

"""

import unittest

class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if not len(A) == len(B):
            return False

        differences = []
        for i in range(len(A)):
            if not A[i] == B[i]:
                differences.append((A[i], B[i]))
        print(differences)

        if len(differences) == 0:
            if len(set(A)) != len(A):
                return True
        if len(differences) == 2:
            if list(differences[0]) == list(differences[1])[::-1]:
                return True
        return False


class Tests(unittest.TestCase):

    sol = Solution()

    def test_example_1(self):
        self.assertEqual(self.sol.buddyStrings("ab", "ba"), True)

    def test_example_2(self):
        self.assertEqual(self.sol.buddyStrings("ab", "ab"), False)

    def test_example_3(self):
        self.assertEqual(self.sol.buddyStrings("aa", "aa"), True)

    def test_example_4(self):
        self.assertEqual(self.sol.buddyStrings("aaaaaaabc", "aaaaaaacb"), True)

    def test_example_5(self):
        self.assertEqual(self.sol.buddyStrings("", "aa"), False)

    def test_example_identical_strings_false(self):
        self.assertEqual(self.sol.buddyStrings("abcde", "abcde"), False)

    def test_example_identical_strings_true(self):
        self.assertEqual(self.sol.buddyStrings("abab", "abab"), True)

    def test_example_more_than_one_flopped_pair(self):
        self.assertEqual(self.sol.buddyStrings("abcd", "badc"), False)

    def test_example_another_false(self):
        self.assertEqual(self.sol.buddyStrings("abcaa", "abcbb"), False)


if __name__ == '__main__':
    unittest.main()