"""
728. Self Dividing Numbers


A self-dividing number is a number that is divisible by every digit it contains.

For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0,
and 128 % 8 == 0.

Also, a self-dividing number is not allowed to contain the digit zero.

Given a lower and upper number bound, output a list of every possible self
dividing number, including the bounds if possible.

Example 1:
Input:
left = 1, right = 22
Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]

"""
from typing import List
import unittest

class Solution:

    def isSelfDividing(self, num:int) -> bool:
        digits = list(str(num))
        for digit in digits:
            if int(digit) == 0:
                return False
            if num % int(digit) != 0:
                return False
        return True

    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        """
        Takes the range from left to right inclusive and returns a list of
        all self dividing numbers
        """
        answer = []

        for num in range(left, right + 1):
            if self.isSelfDividing(num):
                answer.append(num)
        return answer


class TestSelfDividingNumber(unittest.TestCase):

    sol = Solution()

    def test_self_dividing_zero_fails(self):
        self.assertEqual(self.sol.isSelfDividing(0), False)
        self.assertFalse(self.sol.isSelfDividing(0))

    def test_self_dividing_11(self):
        self.assertEqual(self.sol.isSelfDividing(11), True)

    def test_self_dividing_13(self):
        self.assertEqual(self.sol.isSelfDividing(13), False)

    def test_self_dividing_list_base_case(self):
        self.assertEqual(self.sol.selfDividingNumbers(1, 22), [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22])

    def test_self_dividing_list_simple(self):
        self.assertEqual(self.sol.selfDividingNumbers(4, 5), [4, 5])


if __name__ == '__main__':

    unittest.main()
