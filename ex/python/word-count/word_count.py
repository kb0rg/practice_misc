import re

def word_count(phrase):
    words = re.split("[\W_]+(?<!')", phrase.lower())
    return {w: words.count(w) for w in words if w}
