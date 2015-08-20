"""
transform a string into a number.

all inputs will be strings, and every string is a perfectly valid representation 
of an integral number.

>>> string_to_number("1234")
1234
>>> string_to_number("605" )
605
>>> string_to_number("1405")
1405
>>> string_to_number("-7"  )
-7

"""


def string_to_number(s):

	return int(s)

if __name__ == "__main__":

	import doctest
	doctest.testmod()