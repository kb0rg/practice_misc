def high_and_low(numbers):

	"""
	given a string of space separated numbers, return highest & lowest numbers.

	All numbers are valid Int32, no need to validate them.
	There will always be at least one number in the input string.
	Output string must be two numbers separated by a single space, 
	highest number is first.

	>>> high_and_low("1 2 3 4 5")
	'5 1'
	>>> high_and_low("1 2 -3 4 5")
	'5 -3'
	>>> high_and_low("1 9 3 4 -5")
	'9 -5'
	"""

	num_list = [int(num) for num in numbers.split()]
	# print num_list 
	high = str(max(num_list))
	low = str(min(num_list))

	return high + " " + low

if __name__ == "__main__":


    import doctest
    doctest.testmod()