"""
hackerrank: algorithms: warmup: simple array sum

Problem Statement:
You are given an array of integers of size N. You need to print the sum of the 
elements of the array.

Input Format:
The first line of the input consists of an integer N. The next line contains N 
space-separated integers describing the array.

Constraints:
1≤N≤1000 
0≤A[i]≤1000

Output Format:
Output a single value equal to the sum of the elements of the array.

Sample Input:
6
1 2 3 4 10 11

Sample Output:
31

Explanation:
1+2+3+4+10+11=31
"""


# Enter your code here. Read input from STDIN. Print output to STDOUT
def sum_array(input_list):
    return sum(input_list)

t = int(raw_input())
num_list = [int(x) for x in raw_input().split()]
print sum_array(num_list)