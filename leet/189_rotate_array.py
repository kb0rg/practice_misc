"""
189. Rotate Array
https://leetcode.com/problems/rotate-array/

Given an array, rotate the array to the right by k steps, where k is
non-negative.

Follow up:

Try to come up as many solutions as you can, there are at least 3 different
ways to solve this problem.

Could you do it in-place with O(1) extra space?

Constraints:

1 <= nums.length <= 2 * 10^4
It's guaranteed that nums[i] fits in a 32 bit-signed integer.
k >= 0
"""
from typing import List
import unittest

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        temp_nums = nums[len(nums)-k:] + nums[:len(nums)-k]
        nums.clear()
        nums.extend(temp_nums)

class Tests(unittest.TestCase):
    sol = Solution()

    def test_example_1(self):
        """
        Explanation:
        rotate 1 steps to the right: [7,1,2,3,4,5,6]
        rotate 2 steps to the right: [6,7,1,2,3,4,5]
        rotate 3 steps to the right: [5,6,7,1,2,3,4]
        """
        nums = [1,2,3,4,5,6,7]
        k = 3
        output = [5,6,7,1,2,3,4]
        self.sol.rotate(nums, k)
        self.assertEqual(nums, output)


    def test_example_2(self):
        """
        Explanation:
        rotate 1 steps to the right: [99,-1,-100,3]
        rotate 2 steps to the right: [3,99,-1,-100]
        """
        nums = [-1,-100,3,99]
        k = 2
        output = [3,99,-1,-100]
        self.sol.rotate(nums, k)
        self.assertEqual(nums, output)


if __name__ == "__main__":

    unittest.main()
