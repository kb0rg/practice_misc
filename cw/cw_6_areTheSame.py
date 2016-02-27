"""

Given two arrays a and b write a function comp(a, b) that checks whether the 
two arrays have the "same" elements, with the same multiplicities. 
"Same" means, here, that the elements in b are the elements in a squared, 
regardless of the order.

If a or b are None return false.
If a or b are empty return false.

"""

def comp(array1, array2):

	"""
	>>>	a = [121, 144, 19, 161, 19, 144, 19, 11]  
	>>> b = [121, 14641, 20736, 361, 25921, 361, 20736, 361]
	>>> comp(a, b)
	True
	>>>	a = [121, 144, 19, 161, 19, 144, 19, 11]
	>>> b = [132, 14641, 20736, 361, 25921, 361, 20736, 361]
	>>> comp(a, b)
	False
	>>> a = [121, 144, 19, 161, 19, 144, 19, 11]
	>>> b = [121, 14641, 20736, 36100, 25921, 361, 20736, 361]
	>>> comp(a, b)
	False
	"""
	if array1 == None or array2 == None:
		return False

	if len(array1) != len(array2):
		return False

	array1 = sorted(array1)
	array2 = sorted(array2)

	print array1
	print array2

	for i in range(len(array1)):
		if array1[i] **2 != array2[i]:
			return False
	return True





# if __name__ == "__main__":

# 	import doctest
# 	doctest.testmod


# docstring tests not working -- multi-line not ok?
# print tests below:
a = [121, 144, 19, 161, 19, 144, 19, 11]  
b = [121, 14641, 20736, 361, 25921, 361, 20736, 361]
print "a = [121, 144, 19, 161, 19, 144, 19, 11]"
print "b = [121, 14641, 20736, 361, 25921, 361, 20736, 361]"
print "should return True"
print comp(a, b)
print "*" * 30
a = [121, 144, 19, 161, 19, 144, 19, 11]
b = [132, 14641, 20736, 361, 25921, 361, 20736, 361]
print "a = [121, 144, 19, 161, 19, 144, 19, 11]"
print "b = [132, 14641, 20736, 361, 25921, 361, 20736, 361]"
print "should return False"
print comp(a, b)
print "*" * 30
a = [121, 144, 19, 161, 19, 144, 19, 11]
b = [121, 14641, 20736, 36100, 25921, 361, 20736, 361]
print "a = [121, 144, 19, 161, 19, 144, 19, 11]"
print "b = [121, 14641, 20736, 36100, 25921, 361, 20736, 361]"
print "should return False"
print comp(a, b)
print "*" * 30
a = [121, 144, 19, 161, 19, 144, 19]
b = [121, 14641, 20736, 36100, 25921, 361, 20736, 361]
print "a = [121, 144, 19, 161, 19, 144, 19]"
print "b = [121, 14641, 20736, 36100, 25921, 361, 20736, 361]"
print "should return False"
print comp(a, b)
print "*" * 30
a = []
b = [121, 14641, 20736, 36100, 25921, 361, 20736, 361]
print "a = []"
print "b = [121, 14641, 20736, 36100, 25921, 361, 20736, 361]"
print "should return False"
print comp(a, b)
print "*" * 30
a = None
b = [121, 14641, 20736, 36100, 25921, 361, 20736, 361]
print "a = None"
print "b = [121, 14641, 20736, 36100, 25921, 361, 20736, 361]"
print "should return False"
print comp(a, b)
print "*" * 30 + "\n" + "*" * 30 + "\n" + "*" * 30 + "\n"



