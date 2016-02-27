"""
Create a function called repeatIt that takes in a string and a number (n).
The function should return a string that repeats the initial passed in string 
(n) number of times.

If anything other than a string is passed in you should return "Not a string"

>>> repeatIt("Hi",2)
'HiHi'
>>> repeatIt("", 2)
''
>>> repeatIt(20, 2)
'Not a string'

"""
def repeat_it(input_str, num):

	if type(input_str) != str:
		return "Not a string"
	else:
		return input_str * num

if __name__ == "__main__":

	import doctest
	doctest.testmod()