"""
fix regex filter

>>> filter_words("You're Bad! timmy!")
"You're awesome! timmy!"
>>> filter_words("You're MEAN! timmy!")
"You're awesome! timmy!"
"""

import re

def filter_words(phrase):
    return re.sub(r"(bad|mean|ugly|horrible|hideous)","awesome",phrase, flags=re.IGNORECASE)

if __name__ == "__main__":

	import doctest
	doctest.testmod()