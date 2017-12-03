import re

def word_count(phrase):
    counts = {}
    for word in re.split('[\W_]+', phrase.lower()):
        if word:
            counts[word] = counts.get(word, 0) + 1
    return counts
