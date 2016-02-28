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
from pprint import pprint
import urllib2
# import matplotlib.pyplot as plt
# import numpy as np

def peak_hill():

    fileObject = open('pc_5_banner.p', 'rb')
    peakhell = pickle.load(fileObject)

    # do I need to re-pickle it for some reason? 
    # re_peakhell = open('temp_pc_5.pkl', 'wb')
    ## maybe as ascii?
    # re_peakhell = open('temp_pc_5.pkl', 'wa')
    # pickle.dump(peakhell, re_peakhell)
    # re_peakhell.close()

    url = 'http://www.pythonchallenge.com/pc/def/banner.p'
    data = pickle.loads(urllib2.urlopen(url).read())
    for line in data:
        print ''.join(elmt[0] * elmt[1] for elmt in line)

peak_hill()

"""
result:
a long list of lists. of tuples. each tuple has an int in index 1. 
every other tuple containing a hash sign in index 0, and
the alternates have an empty string in index 0.


## 

tried to modify a coulple matplotlib examples fr stack overflow
but kept getting errors I couldn't sort out (UserWarning: Dulpicate key in file 
"..../.matplotlib/matplotlibrc", line #2)

need to learn matplotlib.

"""

