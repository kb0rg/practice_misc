"""
fix the sortArray function to sort all numbers in ascending order

>>> sort_array('12345')
'12345'
>>> sort_array('54321')
'12345'
>>> sort_array('34251')
'12345'

"""

def sort_array(value):
    return "".join(sorted(value,key=lambda a: -int(a)))

if __name__ == "__main__":

	import doctest
	doctest.testmod()