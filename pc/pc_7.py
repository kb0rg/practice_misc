#!/bin/python
# -*- coding: utf-8 -*-
"""
Python Challenge 7
http://www.pythonchallenge.com/pc/def/oxygen.html

image:
very long (pano?) shot of edge of a river,
with a bar of gray squares bisecting it lengthwise
almost completely lf to rt

page title:
"smarty"

hint:

note:

approach:
smarty or smartypants modules?
neither seems relevant
decode image to string?

questions:


"""
import urllib2
import base64

def oxygen():
    url = 'http://www.pythonchallenge.com/pc/def/oxygen.png'
    import pdb; pdb.set_trace()
    # pic = urllib2.urlopen(url)
    # with open(pic, "rb") as imageFile:
    #     str = base64.b64encode(imageFile.read())
    #     print str
    pic = urllib2.urlopen(url).read()
    for line in pic:
        print line
if __name__ == '__main__':
    oxygen()
