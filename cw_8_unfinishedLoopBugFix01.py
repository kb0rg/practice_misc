"""
Unfinished Loop - Bug Fixing #1
find and fix the bug in this unfinished For Loop!

>>> create_array(1)
[1]
>>> create_array(2)
[1,2]
>>> create_array(3)
[1,2,3]
>>> create_array(4)
[1,2,3,4]
>>> create_array(5)
[1,2,3,4,5]
"""

def create_array(n):
    res=[]
    i=1
    while i<=n: 
    	res+=[i]
    	i += 1
    return res

if __name__ == "__main__":

	import doctest
	doctest.testmod()