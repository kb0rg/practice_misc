#Try to make your own gcd method without importing stuff

def mygcd(x,y):

	"""
	Find the greatest common divisor of two positive integers. The integers can 
	be large, so you need to find a clever solution.

	The inputs x and y are always greater or equal to 1, so the the greatest 
	common divisor will always be an integer that is also greater or equal to 1.
		
	>>> mygcd(30,12)
	6
	>>> mygcd(8,9)
	1
	>>> mygcd(1,1)
	1
	>>> mygcd(45,15)
	15
	>>> mygcd(6,30)
	6
	>>> mygcd(10927782,6902514)
	846
	>>> mygcd(1590771464,1590771620)
	4
	"""

	#edge cases:
	if x == 1 or y == 1:
		return 1
	if x % y ==0 or y % x == 0:
		return min([x,y])

	for num in range((max([x,y])/2), 0, -1):
		# print num
		# print "x % num: " + str(x % num)
		# print "y % num: " + str(y % num)
		if x % num == 0 and y % num ==0:
			return num
		# print "NEXT!"


if __name__ == "__main__":


    import doctest
    doctest.testmod()
