import string

def drop_cap(orig_str):

	"""
	The first letter of the starting word of the paragraph should be in caps and the 
	remaining lowercase. Capitalize every word that has length greater than 2, leaving smaller words as 
	they are.
	Note: you will be provided at least one word and should take string as input and return string as output.

	>>> drop_cap('apple')
	'Apple'
	>>> drop_cap('apple of banana')
	'Apple of Banana'
	>>> drop_cap('')
	''
	>>> drop_cap('More  Than    one Space between words')
	'More  Than    One Space Between Words'
	"""

	new_str_list = []

	if len(orig_str) < 2:
		return orig_str

	for word in string.split(orig_str, " "):
		if len(word) > 2:
			word = word.capitalize()
		new_str_list.append(word)

	return " ".join(new_str_list)


if __name__ == "__main__":

    import doctest
    doctest.testmod()