#!/bin/python
# -*- coding: utf-8 -*-

"""
hackerrank: algorithms: sorting: insertion sort pt 1

Problem Statement:
One common task for computers is to sort data. For example, people might want to
see all their files on a computer sorted by size. Since sorting is a simple 
problem with many different possible solutions, it is often used to introduce 
the study of algorithms.

Insertion Sort 
These challenges will cover Insertion Sort, a simple and intuitive sorting 
algorithm. We will first start with an already sorted list.

Insert element into sorted list 
Given a sorted list with an unsorted number e in the rightmost cell, can you 
write some simple code to insert e into the array so that it remains sorted?

Print the array every time a value is shifted in the array until the array is 
fully sorted. The goal of this challenge is to follow the correct order of 
insertion sort.

Guideline: You can copy the value of e to a variable and consider its cell 
"empty". Since this leaves an extra cell empty on the right, you can shift 
everything over until V can be inserted. This will create a duplicate of each 
value, but when you reach the right spot, you can replace it with e.

Input Format:
There will be two lines of input:
Size - the size of the array
Arr - the unsorted array of integers

Constraints:
1≤Size≤1000 
−10000≤e≤10000,e∈Arr

Output Format:
On each line, output the entire array every time an item is shifted in it.

Sample Input:
5
2 4 6 8 3

Sample Output:
2 4 6 8 8 
2 4 6 6 8 
2 4 4 6 8 
2 3 4 6 8 

Explanation:
3 is removed from the end of the array.
In the 1st line 8>3, so 8 is shifted one cell to the right. 
In the 2nd line 6>3, so 6 is shifted one cell to the right. 
In the 3rd line 4>3, so 4 is shifted one cell to the right. 
In the 4th line 2<3, so 3 is placed at position 2.

"""

#!/bin/python
def insertionSort(input_array):
    num = input_array[-1]
    for i in range(m-2, -1, -1):
        if input_array[i] > num:
            input_array[i+1] = input_array[i]
            if i == 0:
            	print " ".join(str(x) for x in input_array)
                input_array[i] = num
            print " ".join(str(x) for x in input_array)
        else:
            input_array[i+1] = num
            print " ".join(str(x) for x in input_array)
            break


    #input_array[0] = num
    return ""

m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)

"""
fails test case #2:

input:
10
2 3 4 5 6 7 8 9 10 1

output expected:
2 3 4 5 6 7 8 9 10 10
2 3 4 5 6 7 8 9 9 10
2 3 4 5 6 7 8 8 9 10
2 3 4 5 6 7 7 8 9 10
2 3 4 5 6 6 7 8 9 10
2 3 4 5 5 6 7 8 9 10
2 3 4 4 5 6 7 8 9 10
2 3 3 4 5 6 7 8 9 10
2 2 3 4 5 6 7 8 9 10 # missing this line
1 2 3 4 5 6 7 8 9 10

actual output:
2 3 4 5 6 7 8 9 10 10
2 3 4 5 6 7 8 9 9 10
2 3 4 5 6 7 8 8 9 10
2 3 4 5 6 7 7 8 9 10
2 3 4 5 6 6 7 8 9 10
2 3 4 5 5 6 7 8 9 10
2 3 4 4 5 6 7 8 9 10
2 3 3 4 5 6 7 8 9 10
1 2 3 4 5 6 7 8 9 10

passes 0, 1, 3

test case #0:

input:

5
2 4 6 8 3

output expected:

2 4 6 8 8
2 4 6 6 8
2 4 4 6 8
2 3 4 6 8

actual output:
2 4 6 8 8
2 4 6 6 8
2 4 4 6 8
2 3 4 6 8
3 3 4 6 8
"""
