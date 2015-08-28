"""
hackerrank: python: intro: triangle quest


Problem Statement:
You are given a positive integer N. You have to print a numerical triangle of 
height N−1 as shown below:

1
22
333
4444
55555
......

Can you do it using only arithmetic operations, a single for loop and print 
statement?

You can't take more than two lines; the first line (for - statement) is already 
written for you. You have to complete the print statement.

Note Using anything related to strings will give a score of 0.

Input Format:
Given N in the first line.

Constraints:
1≤N≤9

Output Format: 
Print N−1 lines as explained above.

Sample Input:
5

Sample Output:
1
22
333
4444

"""

#More than 2 lines will result in 0 score. Do not leave a blank line also
for i in range(1,input()): 
    print i*(10**i)/(10-1)
    

"""
solved it using print formatting, output was correct but as noted in 
instructions, this failed the test.

totally stumped, consulted discussion forum and learned about repdigits, 
and the mathematical formula to derive them:
https://en.wikipedia.org/wiki/Repdigit
"""

