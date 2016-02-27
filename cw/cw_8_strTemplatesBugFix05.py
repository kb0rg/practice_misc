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
    return "I like {}!".format(", ".join(args))

if __name__ == "__main__":

	import doctest
	doctest.testmod()

"""
??? 
passes cw but not doctests.

doctest results showing ", " AFTER last arg.
also returning string inside parens.

some of the other solutions on cw puzzle me.
why would this work?:	
    return "I like {0}!".format(", ".join(args))
(why does it returns more than 1st arg?)

"""