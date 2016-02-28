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
unpickle
<peakhell src="banner.p"/>

questions:
what to do with the results of the unpickle?
or is there something else I need to unpickle?

"""
import pickle
from pprint import pprint

def peak_hill():

    fileObject = open('pc_5_banner.p', 'r')
    peakhell = pickle.load(fileObject)
    
    times_count = 0
    tuples_count = 0

    for peak in peakhell:
        times_count += 1
        for duo in peak:
            tuples_count += 1

    print "times_count", times_count
    print "tuples_count", tuples_count

peak_hill()

"""
result:
a long list of lists. of tuples. each tuple has an int in index 1. 
every other tuple containing a hash sign in index 0, and
the alternates have an empty string in index 0.

first and last list are: [(' ', 95)]

the sum of all intergers in each list is 95.
are the hash signs significant?

sum of all ints in tuples with hash signs: 661
http://www.pythonchallenge.com/pc/def/661.html
nope

sum of all ints in tuples with NO hash signs: 1524
http://www.pythonchallenge.com/pc/def/1524.html
nope

1524-661 = 863
http://www.pythonchallenge.com/pc/def/863.html
nope

hmmmm. 
how many tuples are there?
348
http://www.pythonchallenge.com/pc/def/348.html
nope

how many 95's are there?
23
http://www.pythonchallenge.com/pc/def/2395.html
nope


"""

