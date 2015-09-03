"""
We have a bunch of kids and in the list/array and there is shown how much candy 
each kid has. Because we don't want kids to argue, we want each kid to have the 
same amount of candies, but we can't take candies from kids.

Your job is to give all the kids the same amount of candies as the kid with the 
most candies and then return the total number candies that have been given out. 
If there are no kids, or 1, return -1. In the first case the most candies are 
given to second kid, 8. Because of that we will give the first kid 3 the third 
kid 2 and the fourth kid 4, so all kids will have 8 candies.

Together we will give out 3 + 2 + 4 = 9 candies, that is why function returns 9. 
In the last case you do the same u see second kid has 6 candies so we need to 
give first one 5 and that is also the answear

>>> candies([5,8,6,4])
9

>>> candies([1,2,4,6])
11

>>> candies([1,6])
5

>>> candies([15])
-1

>>> candies([])
-1
"""


def candies(count_list):

	if len(count_list) <=1:
		return -1
	
	candy_added = 0
	most_given = max(count_list)

	for count in count_list:
		candy_added += (most_given - count)

	return candy_added

if __name__ == "__main__":

	import doctest
	doctest.testmod()
