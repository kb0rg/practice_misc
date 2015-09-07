"""
Find the mean (average) of a list of numbers in an array.

To find the mean (average) of a set of numbers add all of the numbers together 
and divide by the number of values in the list.

For an example list of 1, 3, 5, 7

Add all of the numbers
1+3+5+7 = 16
Divide by the number of values in the list. In this example there are 4 numbers 
in the list.
16/4 = 4
The mean (or average) of this list is 4


>>> find_average([1])
1
>>> find_average([1, 3, 5, 7])
4
>>> find_average([-1, 3, 5, -7])
0
>>> find_average([5, 7, 3, 7])
5.5
>>> find_average([])
0

"""

def find_average(nums):
	
	if len(nums) < 1:
		return 0
	else:
		if sum(nums) % len(nums) != 0:
			return float(sum(nums)) / len(nums)
		else:
			return sum(nums) / len(nums)

if __name__ == "__main__":
	import doctest
	doctest.testmod()