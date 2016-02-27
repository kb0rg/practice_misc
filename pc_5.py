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

fileObject = open('pc_5_banner.p', 'r')
# fileObject = open('pc_5_peakhell.jpg', 'r')
peakhell = pickle.load(fileObject)

pprint(peakhell)

"""
result:
a long list of lists. of tuples. each tuple has an int in index 1. 
every other tuple containing a hash sign in index 0, and
the alternates have an empty string in index 0.

first and last list are: [(' ', 95)]

other than that not seeing a clear pattern. the sublists contain varying 
numbers of tuples. I'm sure there's something I'm not seeing yet.

tried unpickling the hill image but got KeyError

"""
