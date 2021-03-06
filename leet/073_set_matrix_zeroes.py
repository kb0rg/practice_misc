"""
73. Set Matrix Zeroes
https://leetcode.com/problems/set-matrix-zeroes/

Given a m x n matrix, if an element is 0, set its entire row and column to 0.
Do it in-place.

Follow up:

A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
"""

from typing import List
import unittest

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        rows_to_zero = set()
        columns_to_zero = set()

        for i, row in enumerate(matrix):
            for j, value in enumerate(row):
                if value == 0:
                    rows_to_zero.add(i)
                    columns_to_zero.add(j)

        for row_index in rows_to_zero:
            matrix[row_index] = [0] * len(matrix[0])
        for col_index in columns_to_zero:
            for i in range(len(matrix)):
                matrix[i][col_index] = 0




class Test(unittest.TestCase):

    sol = Solution()

    def test_example_1(self):
        input = [
          [1,1,1],
          [1,0,1],
          [1,1,1]
        ]

        output = [
          [1,0,1],
          [0,0,0],
          [1,0,1]
        ]
        self.sol.setZeroes(input)
        self.assertEqual(input, output)

    def test_example_2(self):

        input = [
          [0,1,2,0],
          [3,4,5,2],
          [1,3,1,5]
        ]

        output = [
          [0,0,0,0],
          [0,4,5,0],
          [0,3,1,0]
        ]
        self.sol.setZeroes(input)
        self.assertEqual(input, output)


if __name__ == '__main__':
    unittest.main()