import re

def word_count(phrase):
    words = [w.strip("'") for w in re.split("[\W_]+(?<!')", phrase.lower())]
    return {w: words.count(w) for w in words if w}
