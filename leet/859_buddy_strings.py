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

        if A == B:
            return False

        differences = 0
        for i in range(len(A)-1):
            if A[i] != B[i]:
                if A[i] == B[i + 1] and B[i] == A[i+1]:
                    differences += 1
        if differences > 1:
            return False
        return True



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

    def test_example_identical_strings(self):
        self.assertEqual(self.sol.buddyStrings("abcde", "abcde"), False)


if __name__ == '__main__':
    unittest.main()