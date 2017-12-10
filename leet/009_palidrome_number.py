import unittest

"""
Determine whether an integer is a palindrome. Do this without extra space.

"""

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if not x >= 0:
            return False
        for i in range(len(str(x))//2):
            if not str(x)[i] == str(x)[-(i + 1)]:
                return False
        return True

class Tests(unittest.TestCase):

    sol = Solution()

    def test_base_true(self):
        self.assertEqual(self.sol.isPalindrome(4004), True)

    def test_base_false(self):
        self.assertEqual(self.sol.isPalindrome(123), False)

    def test_negative(self):
        self.assertEqual(self.sol.isPalindrome(-2147483648), False)

if __name__ == '__main__':
    unittest.main()