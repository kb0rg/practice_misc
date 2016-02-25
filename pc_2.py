#!/bin/python
# -*- coding: utf-8 -*-
"""
Python Challenge 2
http://www.pythonchallenge.com/pc/def/map.html

image:
an open book (text not legible)

hint:
recognize the characters. maybe they are in the book, 
but MAYBE they are in the page source.

note:
in page source is following comment:
find rare characters in the mess below:

followed by a giant block of symbols (1220 lines)
saved as py_2.txt

"""
from pprint import pprint

f = open("pc_2.txt")

char_counts = {}

for line in f:
    for char in line:
        char_counts[char] = char_counts.get(char, 0) + 1

pprint(char_counts)

"""
output: 

{'\n': 1219,
 '!': 6079,
 '#': 6115,
 '$': 6046,
 '%': 6104,
 '&': 6043,
 '(': 6154,
 ')': 6186,
 '*': 6034,
 '+': 6066,
 '@': 6157,
 '[': 6108,
 ']': 6152,
 '^': 6030,
 '_': 6112,
 'a': 1,
 'e': 1,
 'i': 1,
 'l': 1,
 'q': 1,
 't': 1,
 'u': 1,
 'y': 1,
 '{': 6046,
 '}': 6105}

ok. round the rare charaters. but in what order should they be typed?
"aeilqtuy" -- order of output above -- didn't work.
since dictionaries are unordered, output is not sequential. 
another data type?

"""
