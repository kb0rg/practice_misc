"""
136. Single Number
https://leetcode.com/problems/single-number/

Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it
without using extra memory?

"""
from typing import List
import unittest

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen = set()
        for num in nums:
            if num not in seen:
                seen.add(num)
            else:
                seen.remove(num)

        return seen.pop()



class Tests(unittest.TestCase):

    sol = Solution()

    def test_example_1(self):
        self.assertEqual(self.sol.singleNumber([2,2,1]), 1)

    def test_example_2(self):
        self.assertEqual(self.sol.singleNumber([4,1,2,1,2]), 4)


if __name__ == '__main__':
    unittest.main()