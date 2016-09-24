#!/bin/python
# -*- coding: utf-8 -*-
"""
Python Challenge 6
http://www.pythonchallenge.com/pc/def/channel.html

image:
shiny black pants with zipper open.
colorful shiny underthing with super 70s pattern.
an arrow pointing toward belt loop.

page title:
"now there are pairs"

hint:
comment "<-- zip" at opening html tag

note:
paypal button: html comment says not relevant to riddle.  
pants button says "sprint" twice

approach:
looking into zipfile

questions:
what to zip? the jpg? then what?
"""
import pickle
import urllib2

def zipper():
    img_url = 'http://www.pythonchallenge.com/pc/def/channel.jpg'
    txt_url = 'http://www.pythonchallenge.com/pc/def/channel.html'

    img_data = urllib2.urlopen(img_url).read()
    txt_data = urllib2.urlopen(txt_url).read()

    import pdb; pdb.set_trace()
    zz = zip(img_data, txt_data)


if __name__ == '__main__':
    zipper()

"""
reading the image as data, can then zip(), which returns a list of tuples.
passing only one iternable returns single-item tuples. 
hint about pairs...? pass in same image twice? pass in html and img?


"""
