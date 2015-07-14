# -*- coding: utf-8 -*-
from math import sqrt

def vector_length(vector):

    """
    For a given 2D vector described by cartesian coordinates of its initial point 
    and terminal point in the following format: [[x1, y1], [x2, y2]], 
    your function must return this vector's length presented as a float.

    Error must be less than 0.0000001 * result.

    Coordinates can be integers or floats.
    """

    # vector = [[xA, yA],[xB, yB]]
    xA = vector[0][0]
    xB = vector[1][0]
    yA = vector[0][1]
    yB = vector[1][1]

    # can't figure out how to unpack the coords?
    # xA, yA, xB, yB = vector

    return sqrt(((xA - xB)**2 + (yA - yB)**2))


"""
math refresher:
distance (c) between two points (A and B)
using Pythagorean Theorem: c**2 = a**2 + b**2
where a = distance between two x coord (xA - xB)
and b = distance between two x coord (yA - yB)
so:
c**2 = (xA − xB)**2 + (yA − yB)**2
c = sqrt((xA − xB)**2 + (yA − yB))**2
"""

## is there a way to locally run tests included in the kata?
# Test.assert_equals(vector_length([[0, 1],[0, 0]]), 1)
# Test.assert_equals(vector_length([[0, 3],[4, 0]]), 5)
# Test.assert_equals(vector_length([[1, -1],[1, -1]]), 0)

print "input [[0, 1],[0, 0]] should return 1, returns:"
print vector_length([[0, 1],[0, 0]])
print 
print "input [[0, 3],[4, 0]] should return 5, returns:"
print vector_length([[0, 3],[4, 0]])
print 
print "input [[1, -1],[1, -1]] should return 0, returns:"
print vector_length([[1, -1],[1, -1]])

