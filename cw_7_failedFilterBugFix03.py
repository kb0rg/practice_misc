"""
fix the FilterNumber function to remove all the numbers from the string.
>>> filter_numbers("test123")
'test'
>>> filter_numbers("a1b2c3")
'abc'
>>> filter_numbers("aa1bb2cc3dd")
'aabbccdd'


"""

def filter_numbers(string):
    return "".join(x for x in string if int(x))


if __name__ == "__main__":
	import doctest
	doctest.testmod()