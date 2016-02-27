def anagrams(word, words):

	"""
	Write a function that will find all the anagrams of a word from a list. 
	You will be given two inputs: a word and an array with words. 
	You should return an array of all the anagrams or an empty array if there are none.
	"""

	anagram_list = []

	for w in words:
		if sorted(w) == sorted(word):
			anagram_list.append(w)
	return anagram_list

"""
For example:

anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) => ['aabb', 'bbaa']

anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) => ['carer', 'racer']

anagrams('laser', ['lazing', 'lazy',  'lacer']) => []
"""

print "test 1: 'abba', ['aabb', 'abcd', 'bbaa', 'dada'] => ['aabb', 'bbaa'] ?"
print anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) == ['aabb', 'bbaa']
print "test 2: 'racer', ['crazer', 'carer', 'racar', 'caers', 'racer'] => ['carer', 'racer']?"
print anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) == ['carer', 'racer']
print "test 3: 'laser', ['lazing', 'lazy',  'lacer'] => []?"
print anagrams('laser', ['lazing', 'lazy',  'lacer']) == []
