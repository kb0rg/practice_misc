import unittest

"""
Given an array of integers, return indices of the two numbers such that they
add up to a specific target.

You may assume that each input would have exactly one solution, and you may
not use the same element twice.

Example
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        opts = dict()

        for i, n in enumerate(nums):
            diff = target - n
            if diff not in opts:
                opts[n] = i
            else:
                return [opts[diff], i]

class Tests(unittest.TestCase):

    sol = Solution()

    def test_base(self):
        self.assertEqual(self.sol.twoSum([2, 7, 11, 15], 9), [0,1])


if __name__ == '__main__':
    unittest.main()