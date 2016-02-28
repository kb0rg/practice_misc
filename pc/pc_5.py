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

"""
import pickle
import urllib2

def peak_hill():

    url = 'http://www.pythonchallenge.com/pc/def/banner.p'
    data = pickle.loads(urllib2.urlopen(url).read())
    for line in data:
        print ''.join(elmt[0] * elmt[1] for elmt in line)

peak_hill()

"""
result:

got stuck. was trying to visually plot the data, looked into matplotlib
but was getting errors, couldn't figure it out. 

reached my stuckness threshhold. looked up solution. arrrgh.
same idea on a high level (visual representation of data). 
but totally different approach.
prints "channel"
"""

