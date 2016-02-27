#!/bin/python
# -*- coding: utf-8 -*-
"""
Python Challenge 5
http://www.pythonchallenge.com/pc/def/peak.html

image:
a hill

hint:
page title: peak hell

hint2:
peak hell sounds familiar ?

note:
sounds like... pickle

approach:
look into pickle module.
look for something to unpickle
try:
<peakhell src="banner.p"/>

questions:
what to do with the results of the unpickle?
or is there something else I need to unpickle?

"""
import pickle
from pprint import pprint

def peak_hill():

    fileObject = open('pc_5_banner.p', 'r')
    # fileObject = open('pc_5_peakhell.jpg', 'r')
    peakhell = pickle.load(fileObject)

    # pprint(peakhell)
    
    # peakhell is a list of lists of tuples. 
    # looks like most sum 95. see if there are any that don't?
    count = 0
    sub_count_str = ''
    for peak in peakhell:
        sub_count = 0
        for duo in peak:
            sub_count += duo[1]
        count += sub_count
        sub_count_str = sub_count_str + str(sub_count)
        
    print sub_count_str
    print count

peak_hill()

"""
result:
a long list of lists. of tuples. each tuple has an int in index 1. 
every other tuple containing a hash sign in index 0, and
the alternates have an empty string in index 0.

first and last list are: [(' ', 95)]

the sum of all intergers in each list is 95.
are the hash signs significant?

should I add all the 95s?
http://www.pythonchallenge.com/pc/def/2185.html 
nope.

should I cat all the 95s?
http://www.pythonchallenge.com/pc/def/9595959595959595959595959595959595959595959595.html
nope.
"""
