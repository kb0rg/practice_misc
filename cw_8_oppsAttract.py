"""

Timmy & Sarah think they are in love, but around where they live, they will only 
know once they pick a flower each. If one of the flowers has an even number of 
petals and the other has an odd number of petals it means they are in love.

Write a function that will take the number of petals of each flower and return 
true if they are in love and false if they aren't.

>>> lovefunc(1,4)
True
>>> lovefunc(2,2)
False
>>> lovefunc(0,1)
True
>>> lovefunc(0,0)
False

"""

def is_even(num):
	return num % 2 == 0

def lovefunc(flower1, flower2):
	return is_even(flower1) != is_even(flower2)

if __name__ == "__main__":

	import doctest
	doctest.testmod()
