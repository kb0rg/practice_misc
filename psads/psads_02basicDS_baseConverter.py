from pythonds.basic.stack import Stack

"""
from Problem Solving with Algorithms and Data Structures, 
Basic Data Structures chapter, Converting Decimal Numbers.. section.

requires installation of pythonds module.
"""

def baseConverter(decNumber,base):

    """
    converts decimal number to specified base, up to hexidecimal
    """

    digits = "0123456789ABCDEF"

    remstack = Stack()

    if base > 16 and decNumber != base:
        return "Sorry! Except in special cases, this function only works up to hexidecimal (base 16)"

    if decNumber == base:
        return 10

    while decNumber > 0:
        rem = decNumber % base
        remstack.push(rem)
        decNumber = decNumber // base

    newString = ""
    while not remstack.isEmpty():
        newString = newString + digits[remstack.pop()]

    return newString

print "25 base 2 is: " + str((baseConverter(25,2)))
print "25 base 8 is: " + str((baseConverter(25,8)))
print "25 base 16 is: " + str((baseConverter(25,16)))
print "256 base 16 is: " + str((baseConverter(256,16)))
print "25 base 26 is: " + str((baseConverter(25, 26)))
print "26 base 26 is: " + str((baseConverter(26, 26)))
