"""
hackerrank: algorithms: warmup: staircase


Problem Statement:
Your teacher has given you the task to draw the structure of a staircase. 
Being an expert programmer, you decided to make a program for the same. You are 
given the height of the staircase. You need to print a staircase as shown in the 
example.

Input Format:
You are given an integer N depicting the height of the staircase.

Constraints:
1≤N≤100

Output Format:
Draw a staircase of height N in the format given below.

For example:
     #
    ##
   ###
  ####
 #####
######
Staircase of height 6, note that last line has 0 spaces before it.

Sample Input:
6

Sample Output:
     #
    ##
   ###
  ####
 #####
######

"""

def make_staircase(height):

	for level in range(1, height+1):
		print " " * (height - level) + "#" * level

n = int(raw_input())
make_staircase(n)




