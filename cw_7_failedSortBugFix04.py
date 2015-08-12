"""
fix the sortArray function to sort all numbers in ascending order

>>> sort_array('12345')
'12345'
>>> sort_array('54321')
'12345'
>>> sort_array('34251')
'12345'

"""

def sort_array(value):
    return "".join(sorted(value,key=lambda a: int(a)))

if __name__ == "__main__":

	import doctest
	doctest.testmod()


"""
fixed the bug based on code given, but didn't understand the use of lambda 
and value, key.

this helps:
https://wiki.python.org/moin/HowTo/Sorting

Another difference is that the list.sort() method is only defined for lists. 
In contrast, the sorted() function accepts any iterable.
>>> sorted({1: 'D', 2: 'B', 3: 'B', 4: 'E', 5: 'A'})
[1, 2, 3, 4, 5]



Key Functions

Starting with Python 2.4, both list.sort() and sorted() added a key parameter to 
specify a function to be called on each list element prior to making comparisons.

For example, here's a case-insensitive string comparison:


>>> sorted("This is a test string from Andrew".split(), key=str.lower)
['a', 'Andrew', 'from', 'is', 'string', 'test', 'This']
The value of the key parameter should be a function that takes a single argument 
and returns a key to use for sorting purposes. This technique is fast because 
the key function is called exactly once for each input record.

.....

(so in the cw exercise we're turning the string into a dict, where the 
value is orginal number-as-string, and the key is the number-as-int.
the key is what is used to perform the sort, but the value is what is returned
in the output)
"""


