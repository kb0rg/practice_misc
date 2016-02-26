#!/bin/python
# -*- coding: utf-8 -*-
"""
Python Challenge 4
http://www.pythonchallenge.com/pc/def/linkedlist.php

image:
two wooden dolls on either side of a log, with two-handle saw

hint:
image hover text:
linkedlist.php?nothing=12345

hint2:
title = follow the chain

hint3:
comment in source:
urllib may help. DON'T TRY ALL NOTHINGS, since it will never 
end. 400 times is more than enough.

note:
and the next nothing is 44827...
and the next nothing is 45439...

approach:

loop through a range (up to 400)
use urllib to open page, read html text.
grab numbers out of html body
rebind nothing to numbers
return last url

questions:

are numbers always same number of digits? 
no
is body text before numbers always the same?
no
then need to find a way to grab numbers out of text w/o string slicing

"""
from pprint import pprint
import urllib2

def chainsaw():

    base_url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
    num = "12345"
    num_dict={}

    for x in range(401):
        new_url = base_url + num
        response = urllib2.urlopen(new_url)
        html = response.read()
        # grab numbers out of html body
        num = ''.join([str(i) for i in html.split() if i.isdigit()])
        if num in num_dict:
            break
        else:
            num_dict[num] = num_dict.get(num, 1)

    
    return new_url

pprint(chainsaw())


"""
following the nothings 400 times returns:
http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=85501
which gives:
and the next nothing is 43650

creating a dict to see what is going on. is the list circular?

there are several numbers that appear only once, and some twice.
there are also a couple of empty results.

running until a duplicated num occurs returns (the empty num/ break!):
http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=
which gives:
and the next nothing is 6711

...
try the num before the break?
http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=66831
give:
peak.html

yes!!
http://www.pythonchallenge.com/pc/def/peak.html
"""

