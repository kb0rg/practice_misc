import re
import string

def is_pangram(sentence):
    source = sorted(set([x for x in sentence.lower() if x.isalpha()]))
    target = list(string.ascii_lowercase)
    if not target == source:
        return False
    return True
