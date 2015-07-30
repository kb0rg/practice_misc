"""
Write a function which takes a string (day of week) and an integer (number to 
be tested) and tests whether number matches rules below (return a boolean).

Monday --> 12
Tuesday --> numbers greater than 95
Wednesday --> 34
Thursday --> 0
Friday --> numbers divisable by 2
Saturday --> 56
Sunday --> 666 or -666

"""

def am_I_afraid(day,num):


	"""
	>>> am_I_afraid("Monday", 13)
	False
	>>> am_I_afraid("Sunday", -666)
	True
	>>> am_I_afraid("Tuesday", 2)
	False
	>>> am_I_afraid("Tuesday", 965)
	True
	>>> am_I_afraid("Friday", 2)
	True
	"""

	""" first instinct: use dict. 
	but not sure how to handle values that are conditional
	(ie rules for Tues and Fri)
	"""
	# rules_dict = {
	# "Monday": 12,
	# "Tuesday": , #--> numbers greater than 95
	# "Wednesday": 34,
	# "Thursday": 0,
	# "Friday": , #--> numbers divisable by 2
	# "Saturday": 56,
	# "Sunday": [666, -666]
	# }

	"""
	the long way, refactored after seeing solutions
	"""

	if day == "Monday":
		return num == 12
	if day == "Tuesday": 
		return num > 95
	if day == "Wednesday":
		return num == 34
	if day == "Thursday":
		return num == 0			
	if day == "Friday":
		return num % 2 == 0
	if day == "Saturday":
		return num == 56
	if day == "Sunday":
		return abs(num) == 666


if __name__ == "__main__":

	import doctest
	doctest.testmod()