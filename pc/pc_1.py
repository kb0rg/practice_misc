#!/bin/python
# -*- coding: utf-8 -*-
"""
Python Challenge 1
http://www.pythonchallenge.com/pc/def/map.html

image:
K -> M 
O -> Q 
E -> G 

hint:
everybody thinks twice before solving this.

text:
g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.

note: 
not sure what's up with the hint.
image implies the key to code is each char offset by 2 in alphabet.
"map" in url hints that I should use the map function?
I'm not sure what function I can apply to the iterable (alphabet list), to 
advance the index/ rotate the list?
working around it with list slices
"""

import string

def decode_str(str):

    alphabet = list(string.ascii_lowercase)
    cracked = alphabet[2:] + alphabet[:2]

    cracked_str = ""
    
    for char in str:
        if char in alphabet:
            cracked_str = cracked_str + cracked[alphabet.index(char)]
        else:
            cracked_str = cracked_str + char
    return cracked_str

text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
# print decode_str(text)

"""
output:
i hope you didnt translate it by hand. thats what computers are for. doing it in 
by hand is inefficient and that's why this text is so long. using 
string.maketrans() is recommended. now apply on the url.

note:
I'll have to play with maketrans, have never seen it before.
in the meantime, using the function I already built to get to the next challenge

"""


print decode_str('map')
# output: ocr
# http://www.pythonchallenge.com/pc/def/ocr.html