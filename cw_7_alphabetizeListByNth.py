"""
Write a function that accepts two parameters:
i) a string (containing a list of words) and 
ii) an integer (n). 
The function should alphabetize the list based on the nth letter of each word.

The length of all words provided in the list will be >= n. 
The format will be "x, x, x"
"""
import string
def sort_it(list_, n):

	"""
	>>> sort_it('bid, zag', 2)
	'zag, bid'
	>>> sort_it('bill, bell, ball, bull', 2)
	'ball, bell, bill, bull'
	>>> sort_it('bill,bell,ball,bull,comma', 2)
	'ball, bell, bill, comma, bull'
	>>> sort_it('cat, dog, eel, bee', 3)
	'bee, dog, eel, cat'
	"""

	words_list = list_.split(",")
	words_dict = {}
	# print "words_list: ", words_list

	for word in words_list:
		word = string.lstrip(word)
		# print word[(n-1):]
		words_dict[word[(n-1):]] = word

	# print "words_dict: ", words_dict

	sorted_list = [words_dict[x] for x in sorted(words_dict.keys())]

	return ", ".join(sorted_list)

if __name__ == "__main__":

	import doctest
	doctest.testmod()

"""
this worked on the first round of tests. then failed in the second:
some of the input strings were separated by "," only instead of ", "

also, some tests have duplicates, which will break current structure using dict.
re-work how values are stored (use list)
also, keys should poss be the nth char only, not the string slice, to fix issue with
different strings that have the same nth char:
currently returns "ties" sorted alphabetically, but looks like, after initial sort, it should return in order passed

eg:
>>> sort_it('Wolfgang Mittermeyer, Neidhardt Muller, Ernst von Eisenach, Theodor von Lucke, Hildegard von Mariendorf, Adalbert von Fahrenheit, Ernst von Eisenach, Karl Gustav Kempf', 4)
'Hildegard von Mariendorf, Neidhardt Muller, Wolfgang Mittermeyer, Karl Gustav Kempf, Adalbert von Fahrenheit, Theodor von Lucke, Ernst von EisenachErnst von Eisenach' 
should equal 
'Neidhardt Muller, Hildegard von Mariendorf, Wolfgang Mittermeyer, Adalbert von Fahrenheit, Karl Gustav Kempf, Theodor von Lucke, Ernst von Eisenach, Ernst von Eisenach'

>>> sort_it('Adalbert von Fahrenheit, Theodor von Lucke, Ernst von Eisenach, Ernst von Eisenach, August Samuel Wahlen, Paul von Oberstein', 9)
'Adalbert von Fahrenheit, Paul von Oberstein, August Samuel Wahlen, Ernst von Eisenach, Ernst von Eisenach, Theodor von Lucke'

"""


# print sort_it('bid, zag', 2)
# print "*" * 30
# print sort_it('bill, bell, ball, bull', 2)
# print "*" * 30
# print sort_it('cat, dog, eel, bee', 3)
# print "*" * 30
# print sort_it('bill,bell,ball,bull,comma', 2)



