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
        listify_string = list(A)
        for i in range(len(listify_string)):
            # split the A string into parts:
            # before curr char,
            # current and next char, swapped,
            # after next char
            # then re-assemble, and compare with str B
            #
            # EX: "abcd" "acbd"
            while i < len(listify_string) - 2:
                # this borked - when I walked through it, I realized my mistake
                # in the first position
                if "".join([
                    str(listify_string[0:i]), # "a"
                    listify_string[i+1], # "c"
                    listify_string[i], # "b"
                    str(listify_string[i+2:]) # "d"
                ]) == B:
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


if __name__ == '__main__':
    unittest.main()