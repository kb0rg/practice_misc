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

hint2:
page's title is re. use regex?

note:
in page source is another giant block of char. 
saved as py_3.txt

approach:
we want to find a lowercase char with 3 uppercase char on either side. 
those need to be bounded by lowercase to fullfill the "exactly 3" parameter.

looking for pattern LLLsLLL may eliminate matches at beg or end of text:
look for pattern LLLsLLL
and then make sure there is no L on either side?

also try again with return char stripped, parsing text as one string, no lines

questions:
how to do this more efficiently than looking for pattern at each char?

"""

from pprint import pprint

def candles(text_file):
    text_file = open(text_file)
    text = text_file.read().replace("\n", "")

    part_matches = []

    i = 0
    while i < (len(text) - 6): # check to last poss occur of 1st char in pattern
        if text[i:i+3].isupper():
            if text[i+3].islower():
                if text[i+4: i+7].isupper():
                    if i == 0 or text[i-1].islower():
                        if i + 7 == len(text) or text[i+7].islower():
                            part_matches.append(text[i:i+7])
        i+=1

    url_string = "" 

    for item in part_matches:
        url_string = url_string + item[3]

    return url_string

f = "pc_3.txt"
pprint(candles(f))

"""
the output string is "linkedlist"

http://www.pythonchallenge.com/pc/def/linkedlist.html
returns a page blank except for the text "linkedlist.php"

tried
http://www.pythonchallenge.com/pc/def/l.html
(just the "head" of the linked list) and got:
yes. but there are more.

"""
