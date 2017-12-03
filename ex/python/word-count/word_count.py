def word_count(phrase):
    counts = {}
    for word in phrase.split():
        w = word.lower()
        counts[w] = counts.get(w, 0) + 1
    return counts
