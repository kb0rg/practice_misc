"""
Take a string and return a hash with all the ascii values of the characters in 
the string. Returns nil if the string is empty. The key is the character, and 
the value is the ascii value of the character. Repeated characters are to be 
ignored and non-alphebetic characters as well.
>>> char_to_ascii("")
None
>>> char_to_ascii("a")
{'a': 97}
>>> char_to_ascii("aaa")
{'a': 97}

"""


def char_to_ascii(string):

	if string == '':
		return None

	ascii_hash = {}
	for char in string:
		if char.isalpha():
			if char not in ascii_hash:
				ascii_hash[char] = ord(char)
	return ascii_hash


if __name__ == "__main__":
	import doctest; doctest.testmod()

	"""
	need to get cw's test module installed.
	doctests are too literal. this passes on cw but fails w doctest
	bc "Expected: None Got nothing"
	"""
	# test.assert_equals(char_to_ascii(""), None,"deals with an empty string")
	# test.assert_equals(char_to_ascii("a"), {"a":97},"deals with one char")
	# test.assert_equals(char_to_ascii("aaa"), {"a":97},"deals with repeated characters")
