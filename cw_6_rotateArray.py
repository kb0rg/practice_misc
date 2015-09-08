"""

Description:

Create a function named "rotate" that takes an array and returns a new one with 
the elements inside rotated n spaces.

If n is greater than 0 it should rotate the array to the right. If n is less 
than 0 it should rotate the array to the left. If n is 0, then it should return 
the array unchanged.

Example:

>>> data = [1, 2, 3, 4, 5];
>>> rotate(data, 1)
[5, 1, 2, 3, 4]
>>> rotate(data, 2)
[4, 5, 1, 2, 3]
>>> rotate(data, 3)
[3, 4, 5, 1, 2]
>>> rotate(data, 4)
[2, 3, 4, 5, 1]
>>> rotate(data, 5)
[1, 2, 3, 4, 5]
>>> rotate(data, 0)
[1, 2, 3, 4, 5]

>>> rotate(data, -1)
[2, 3, 4, 5, 1]
>>> rotate(data, -2)
[3, 4, 5, 1, 2]
>>> rotate(data, -3)
[4, 5, 1, 2, 3]
>>> rotate(data, -4)
[5, 1, 2, 3, 4]
>>> rotate(data, -5)
[1, 2, 3, 4, 5]

Furthermore the method should take ANY array of objects and perform this 
operation on them:

>>> rotate(['a', 'b', 'c'], 1)    
['c', 'a', 'b']
>>> rotate([1.0, 2.0, 3.0], 1)    
[3.0, 1.0, 2.0]
>>> rotate([True, True, False], 1)
[False, True, True]

Finally the rotation shouldn't be limited by the indices available in the array. 
Meaning that if we exceed the indices of the array it keeps rotating.

Example:
data = [1, 2, 3, 4, 5]
>>> rotate(data, 7)    
[4, 5, 1, 2, 3]
>>> rotate(data, 11)   
[5, 1, 2, 3, 4]
>>> rotate(data, 12478)
[3, 4, 5, 1, 2]

"""

def rotate(arr, n):

	rot = n % len(arr)

	if rot == 0:
		return arr

	new_arr = []
	# print "rot:", str(rot)

	rot_ind = -rot
	# print "rot_ind:", str(rot_ind)
	# print "arr[rot_ind]:", str(arr[rot_ind])

	for i in range(len(arr)):
		# print "-rot:", str(-rot)
		# print "item at -rot +1", int(-rot+1)
		new_arr.append(arr[rot_ind])
		rot_ind += 1

	return new_arr


if __name__ == "__main__":

	import doctest
	doctest.testmod()



