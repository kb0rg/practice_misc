"""
hackerrank: python: data types: tuples 


Problem Statement:
Tuples are a data structure just like list; the prime difference is that tuples 
are immutable, which means that once created, you can not modify them.

This surely restricts us in using them as we cannot add, remove, or assign 
values. But it gives us advantage in space and time complexities.

A cool use of tuple we do without realizing is swapping two numbers

a,b = b,a 
Here a,b is a tuple and assigns itself values of b,a.

Another awesome use of tuples is that they can be used as keys in a dictionary; 
in other words, tuples are hashable.

Task:
You are given an integer N in one line. The next line contains N space-separated 
integers. Create a tuple of those N integers. Lets call it T.
Compute hash(T) and print it.

Note: hash() is one of the function in __builtins__ module.

Input Format:
The first line contains N. The next line contains N space-separated integer 
values.

Output Format: 
Print the computed value.

Sample Input:
2
1 2

Sample Output:
3713081631934410656

"""

N = int(raw_input())

T = tuple(int(x) for x in raw_input().strip().split(" "))
print hash(T)