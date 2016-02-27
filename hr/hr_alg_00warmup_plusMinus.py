"""
hackerrank: algorithms: warmup: plus minus

Problem Statement:

You're given an array containing integer values. You need to print the fraction 
of count of positive numbers, negative numbers and zeroes to the total numbers. 
Print the value of the fractions correct to 3 decimal places.

Input Format:
First line contains N, which is the size of the array. 
Next line contains N integers A1,A2,A3,⋯,AN, separated by space.

Constraints:
1≤N≤100 
−100≤Ai≤100

Output Format:
Output three values on different lines equal to the fraction of count of 
positive numbers, negative numbers and zeroes to the total numbers respectively 
correct to 3 decimal places.

Sample Input:
6
-4 3 -9 0 4 1

Sample Output:
0.500
0.333
0.167

Explanation:
There are 3 positive numbers, 2 negative numbers and 1 zero in the array. 
Fraction of the positive numbers, negative numbers and zeroes are 3/6=0.500, 
2/6=0.333 and 1/6=0.167 respectively.

Note This challenge introduces precision problems. You can even print output to 
4 decimal places and above but only the difference at 3rd decimal digit is 
noted. That is the reason you'll notice testcases have much higher precision 
(more decimal places) than required. 
Answers with absolute error upto 10−4 will be accepted.

"""

def find_counts(num_list):

	count_pos = 0
	count_neg = 0
	count_zero = 0

	for num in num_list:
		if num > 0:
			count_pos +=1
		elif num < 0:
			count_neg += 1
		else: 
			count_zero += 1

	return [count_pos, count_neg, count_zero]

t = float(raw_input())
input_list = [int(x) for x in raw_input().split()]
counts = find_counts(input_list)
print "%f\n%f\n%f" % (counts[0]/t, counts[1]/t, counts[2]/t)


