def detect_anagrams(word, candidates):
    word = word.lower()
    match = sorted(list(word))
    ln = len(word)
    res = []

    for w in candidates:
        if len(w) == ln:
            if not w.lower() == word:
                if sorted(list(w.lower())) == match:
                    res.append(w)
    return res

