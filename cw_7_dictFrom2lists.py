"""
There are two lists of different length. The first one consists of keys, the 
second one consists of values. Write a function createDict(keys, values) that 
returns a dictionary created from keys and values. 
If there are not enough values, the rest of keys should have a None value. 
If there not enough keys, just ignore the rest of values.

>>> createDict(['a', 'b', 'c', 'd'], [1, 2, 3])
{'a': 1, 'b': 2, 'c': 3, 'd': None})
>>> createDict(['a', 'b', 'c'], [1, 2, 3, 4])
{'a': 1, 'b': 2, 'c': 3})


"""

def createDict(keys, values):

	new_dict = {}

	for i in range(0, len(keys)):
		if i < len(values):
			new_dict[keys[i]] = values[i]
		else:
			new_dict[keys[i]] = None

	return new_dict


"""
passes cw tests.
fails doctest bc testmod looks for literal match,
dictionary is unordered therefore not returned as literal match.

need to learn other methods for local testing.

"""

# if __name__ == "__main__":

# 	import doctest
# 	doctest.testmod()

"""
also, most solutions on cw use "zip()"
have not used zip. investigate and revisit.
"""