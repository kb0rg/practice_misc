"""
write a function that takes a String and returns an Array/list with the length 
of each word added to each element, separated by a space.

Note: Input string will have at least one element; 
words will always be separated by a space.

>>> add_length('apple ban')
['apple 5', 'ban 3']
>>> add_length('you will win')
['you 3', 'will 4', 'win 3']

"""

def add_length(orig_str):

	words_len_list = []

	for word in orig_str.split():
		word = word + " " + str(len(word))
		words_len_list.append(word)

	return words_len_list


if __name__ == "__main__":

	import doctest
	doctest.testmod()