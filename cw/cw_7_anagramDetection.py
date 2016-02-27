def is_anagram(test, original):

	"""
	write the function to return true if the word test is an anagram of the 
	word original and false otherwise. 
	"""

	if sorted(test.lower()) == sorted(original.lower()):
		return True
	else:
		return False

print "Testing 'Creative' and 'Reactive' should be True, returns:"
print is_anagram("Creative", "Reactive")
print "Testing 'level' and 'level' should be True, returns:"
print is_anagram("level", "level")
print "Testing 'red' and 'dog' should be False, returns:"
print is_anagram("red", "dog")
print "Testing '' and 'anything' should be False, returns:"
print is_anagram("", "anything")