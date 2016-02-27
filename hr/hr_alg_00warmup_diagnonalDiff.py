"""
hackerrank: algorithms: warmup: diagonal difference

Problem Statement:
You are given a square matrix of size N×N. Calculate the absolute difference of 
the sums across the two main diagonals.

Input Format

The first line contains a single integer N. The next N lines contain N integers 
(each) describing the matrix.

Constraints:
1≤N≤100 
−100≤A[i]≤100

Output Format:
Output a single integer equal to the absolute difference in the sums across the 
diagonals.

Sample Input:
3
11 2 4
4 5 6
10 8 -12

Sample Output:
15

Explanation:
The first diagonal of the matrix is:
11
    5
        -12
Sum across the first diagonal = 11+5-12= 4

The second diagonal of the matrix is:

        4
    5
10
Sum across the second diagonal = 4+5+10 = 19 
Difference: |4-19| =15
"""

def diag_difference(size_of_matrix):

	"""
	hint gotten in HR discussion forum:
	process STDIN row as part of loop instead of storing entire matrix
	"""

	sum_diag1 = 0
	sum_diag2 = 0

	for i in range(size_of_matrix):
		row = [int(x) for x in raw_input().split()]
		sum_diag1 += row[i]
		sum_diag2 += row[-(i+1)]

	return abs(sum_diag2-sum_diag1)

n = int(raw_input())
print diag_difference(n)



