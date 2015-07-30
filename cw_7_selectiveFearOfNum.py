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
	going to solve it the long way then revisit.
	"""

	if day == "Monday":
		if num == 12:
			return True
		else: 
			return False
	elif day == "Tuesday":
		if num > 95:
			return True
		else: 
			return False
	elif day == "Wednesday":
		if num == 34:
			return True
		else: 
			return False
	elif day == "Thursday":
		if num == 0:
			return True
		else: 
			return False			
	elif day == "Friday":
		if num % 2 == 0:
			return True
		else: 
			return False			
	elif day == "Saturday":
		if num == 56:
			return True
		else: 
			return False			
	elif day == "Sunday":
		if abs(num) == 666:
			return True
		else: 
			return False			
	else: 
		return False



if __name__ == "__main__":

	import doctest
	doctest.testmod()