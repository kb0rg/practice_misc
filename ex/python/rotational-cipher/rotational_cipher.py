def rotate(text, key):
    if key % 26 == 0:
        return text

    coded = []
    for c in text:
        if c.isalpha():
            rot = (ord(c) + key)
            if rot > 122:
                rot -= 26
            c = chr(rot)
        coded.append(c)
    return ''.join(coded)