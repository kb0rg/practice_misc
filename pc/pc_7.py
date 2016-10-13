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
got stuck, looked for hints. apparently pillow is the way to go,
and smarty is not relevant as a hint to the approach.

approach:
examine pixel values using PIL.
turn values into letters.

questions:

"""
from PIL import Image
import urllib2

def oxygen():
    url = 'http://www.pythonchallenge.com/pc/def/oxygen.png'
    import pdb; pdb.set_trace()
    pic = urllib2.urlopen(url)
    import pdb; pdb.set_trace()
if __name__ == '__main__':
    oxygen()
