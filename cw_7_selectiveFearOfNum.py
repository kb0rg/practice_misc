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

	""" 
	the dictionary approach, clarified after seeing solutions.
	didn't know I could use dict like this, with rules 
	being tested at return statement. very cool.
	"""
	return {
	"Monday": num == 12,
	"Tuesday": num > 95,
	"Wednesday": num == 34,
	"Thursday": num == 0,
	"Friday": num % 2 == 0,
	"Saturday": num == 56,
	"Sunday": abs(num) == 666
	}[day]


if __name__ == "__main__":

	import doctest
	doctest.testmod()