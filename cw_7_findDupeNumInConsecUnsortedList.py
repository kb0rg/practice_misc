"""
You are given an array of n+1 integers 1 through n. 
In addition there is a single duplicate integer. The array is unsorted.

An example valid array would be [3,2,5,1,3,4]. 
It has the integers 1 through 5 and 3 is duplicated.
[1,2,4,5,5] would not be valid as it is missing 3.

You should return the duplicate value as a single integer.

>>> find_dup([5,4,3,2,1,1])
1
>>> find_dup([1,3,2,5,4,5,7,6])
5

"""


def find_dup(arr):

	for i in range(len(sorted(arr))):
		if sorted(arr)[i] == sorted(arr)[i+1]:
			return sorted(arr)[i]	


if __name__ == "__main__":

	import doctest
	doctest.testmod()


"""
passes. but. a couple other solutions intrigue/ confuse me:

# return sum(arr) - len(arr)*(len(arr)-1)/2
or
# return (i for i in arr if arr.count(i) > 1).next()

revisit.
"""