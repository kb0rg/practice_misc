"""
There is a house with 4 levels. In that house there is an elevator. 
You can program this elevator to go up or down, depending on what button the 
user touches inside the elevator.

levels can be only numbers: 0,1,2,3 buttons can be strings: '0','1','2','3' 
possible return values are numbers: -3,-2,-1,0,1,2,3

If the elevator is on the ground floor(0th level) and the user touches button '2' 
the elevator must go 2 levels up, so our function must return 2.

If the elevator is on the 3rd level and the user touches button '0' the elevator 
must go 3 levels down, so our function must return -3.

If the elevator is on the 2nd level, and the user touches button '2' the elevator 
must remain on the same level, so we return 0.

We cannot endanger the lives of our passengers, so if we get erronous inputs, 
our elevator must remain on the same level. So for example:

goto(2,'4') must return 0, 
because there is no button '4' in the elevator.
goto(4,'0') must return 0, because there is no level 4.
goto(3,undefined) must return 0.
goto(undefined,'2') must return 0.
goto([],'2') must return 0, 
because the type of the input level is array instead of a number.
goto(3,{}) must return 0, 
because the type of the input button is object instead of a number.
"""

def goto(level, button):

	"""
	>>> goto(0,'3')
	3
	>>> goto(3, '1')
	-2

	>>> goto(2,'4')
	0
	>>> goto(4,'0')
	0


	>>> goto([],'2')
	0
	>>> goto(3,{})
	0
	>>> goto(3, 'i') #make sure string contains an int?
	0
	"""

	if not isinstance(level, (int)):
		return 0

	if not isinstance(button, (str)):
		return 0

	try:
		int(button)
		button = int(button)

		if level < 0 or level > 3 or button < -3 or button > 3:
			return 0
		if level > button:
			return -(level - button)
		else:
			return button - level	
	except ValueError:
		return 0



if __name__ == "__main__":

	import doctest
	doctest.testmod()
