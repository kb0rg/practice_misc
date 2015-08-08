"""
Initiallize input names (See pattern below):

>>> initials('code wars')
'C.Wars'
>>> initials('Barack Hussain obama')
'B.H.Obama'

"""

def initials(name):

	name_list = name.split(" ")
	initials_str = ""

	for i in range(len(name_list)-1):
		initials_str = initials_str + name_list[i][0].upper() + "."

	return initials_str + name_list[-1].title()


if __name__ == "__main__":
	import doctest
	doctest.testmod()