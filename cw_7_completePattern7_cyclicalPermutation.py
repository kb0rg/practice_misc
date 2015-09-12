"""

write a function pattern which creates the following pattern(See Examples) 
up to desired number of rows.

If the Argument is 0 or a Negative Integer then it should return "" 
i.e. empty string.

Examples:

>>> pattern(9)
123456789
234567891
345678912
456789123
567891234
678912345
789123456
891234567
912345678

>>> pattern(5)
12345
23451
34512
45123
51234

>>> pattern(-2)
''

>>> pattern(1)
1
>>> pattern(4)
1234\n2341\n3412\n4123
>>> pattern(0)
''


Note: There are no spaces in the pattern

Hint: Use \n in string to jump to next line
"""

def pattern(n):

	if n <1:
		return ""

	if n == 1:
		return '1'

	base = range(1,n+1)
	pattern_string = ""

	for num in base[:n-1]:
		i = num-1
		pattern_string += "".join([str(x) for x in base[i:]+base[:i]]) + "\n"

	pattern_string += "".join([str(x) for x in base[n-1:]+base[:n-1]])
	return pattern_string

if __name__ == "__main__":

	import doctest
	doctest.testmod()
