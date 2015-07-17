import string

def capitals(word):
	"""
	Write a function that takes a single string (word) as argument. 
	The function must return an ordered list containing the indexes of all 
	capital letters in the string.
	"""

	caps_indices= []

	for i in range(0,len(word)):
		if word[i] in string.ascii_uppercase:
			caps_indices.append(i)

	return caps_indices

print "capitals('CodEWaRs') should return [0,3,4,6], returns:"
print capitals('CodEWaRs')
print "capitals('codewar5') should return [], returns:"
print capitals('codewar5')

"""
first attempt iterating through char failed in cw random tests --
realized if char was duplicated in word, word.index(char) would find *first*
index where that char existed, not necessarily the one at given position.
"""