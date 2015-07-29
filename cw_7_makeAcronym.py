"""
Implement a function called makeAcronym that returns the first letters of each 
word in a passed in string. Make sure the letters returned are uppercase.

If the value passed in is not a string return 'Not a string'.

If the value passed in is a string which contains characters other than spaces 
and alphabet letters, return 'Not letters'.

If the string is empty, just return the string itself: "".
"""

import string

def make_acronym(phrase):

    """

    >>> make_acronym('Hello codewarrior')
    'HC'

    >>> make_acronym('a42')
    'Not letters'

    >>> make_acronym(42)
    'Not a string'

    >>> make_acronym([2,12])
    'Not a string'

    >>> make_acronym({'name': 'Abraham'})
    'Not a string'

    >>> make_acronym("")
    ''

    >>> make_acronym('My aunt sally')
    'MAS'

    >>> make_acronym('Please excuse my dear aunt Sally')
    'PEMDAS'

    >>> make_acronym('How much wood would a woodchuck chuck if a woodchuck could chuck wood')
    'HMWWAWCIAWCCW'

    >>> make_acronym('kv r')
    'KR'

    """

    if phrase == "":
        return ""

    if not isinstance(phrase, str):
        return 'Not a string'

    if all(char.isalpha() or char == ' ' for char in phrase):
        acro = ""
        for word in string.split(phrase):
            acro = acro + string.upper(word[0])
        return acro
    else:
        return 'Not letters'



if __name__ == "__main__":

    import doctest
    doctest.testmod()