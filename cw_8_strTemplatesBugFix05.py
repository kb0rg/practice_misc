"""
fix string template

>>> build_string('Cheese','Milk','Chocolate')
'I like Cheese, Milk, Chocolate!'
>>> build_string('Cheese','Milk'), 
'I like Cheese, Milk!'
>>> build_string('Chocolate'), 
'I like Chocolate!'
"""

def build_string(*args):
    return "I like {}!".format(",".join(args))

if __name__ == "__main__":

	import doctest
	doctest.testmod()