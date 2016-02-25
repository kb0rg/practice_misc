#!/bin/python
# -*- coding: utf-8 -*-
"""
Python Challenge 3
http://www.pythonchallenge.com/pc/def/equality.html

image:
7 candles: one small with 3 large on either side

hint:
One small letter, surrounded by EXACTLY three big bodyguards 
on each of its sides.

note:
in page source is another giant block of char. 
saved as py_3.txt

approach:
we want to find a lowercase char with 3 uppercase char on either side. 
those need to be bounded by lowercase to fullfill the "exactly 3" parameter.

look for pattern sLLLsLLLs

questions:
how to do this more efficiently than looking for pattern at each char?
how are returns treated? is each line distinct or does pattern wrap?

"""

def candles(text_file):
    for line in text_file:
        line = line.rstrip("\n")
        i = 0
        while i < (len(line) - 8): # check to last poss occur of 1st char in pattern
            if not line[i].islower():
                i += 1
            else: 
                if line[i:i+4].isupper():
                    if line[i+4].islower() or line[i+4] == "\n":
                        return line[i:i+9]
                i+=1
    return "Nope"

f = open("pc_3.txt")
print candles(f)
