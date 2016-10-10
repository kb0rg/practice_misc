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

arrrrrrgh. gave up, and looked for hint. got the answer in the search result,
not just a hint. sigh. well, still need to implement it.

hint "<-- zip" at opening tag was pointing to the tag (html).
replace "html with "zip" and open 
http://www.pythonchallenge.com/pc/def/channel.zip

unzip, find many numbered txt files and a readme.
readme says:
"welcome to my zipped list.
hint1: start from 90052
hint2: answer is inside the zip"

90052.txt says:
"Next nothing is 94191"
(redux of pc_4 linked list)

"""
import os

def zipper():
    dirpath = '~/Downloads/channel/'
    nums = '90052'

    while nums:
        filename = ''.join([dirpath, nums, '.txt'])
        nextfile = open(os.path.expanduser(filename), 'r')
        msg = nextfile.read()
        clue = nextfile.comment()
        print msg
        print "clue: ", clue
        nums = msg[16:] #strips 'Next nothing is '
        nextfile.close()

if __name__ == '__main__':
    zipper()

"""
After reading and redirecting to several "next" nums, got:
"Next nothing is 46145
Collect the comments."

comments?
"""

with ZipFile('spam.zip') as myzip:
    with myzip.open('eggs.txt') as myfile:
        print(myfile.read())
