import unittest

"""
Given a 32-bit signed integer, reverse digits of an integer.

Note:
Assume we are dealing with an environment which could only hold integers
within the 32-bit signed integer range. For the purpose of this problem,
assume that your function returns 0 when the reversed integer overflows.
"""


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x > 2147483647 or x < -2147483647:
            return 0

        mult = -1 if x < 0 else 1
        y = int(str(x * mult)[::-1])
        if y > 2147483647 or x < -2147483647:
            return 0
        return y * mult


class Tests(unittest.TestCase):

    sol = Solution()

    def test_base(self):
        self.assertEqual(self.sol.reverse(123), 321)

    def test_negative(self):
        self.assertEqual(self.sol.reverse(-123), -321)

    def test_ends_in_zero(self):
        self.assertEqual(self.sol.reverse(120), 21)

    def test_exceeds_max(self):
        self.assertEqual(self.sol.reverse(1534236469), 0)

    def test_exceeds_max_negative(self):
        self.assertEqual(self.sol.reverse(-2147483648), 0)

if __name__ == '__main__':
    unittest.main()