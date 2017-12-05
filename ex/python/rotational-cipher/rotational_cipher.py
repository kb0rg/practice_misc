def rotate(text, key):
    if key % 26 == 0:
        return text

    coded = []
    for c in text:
        if c.isalpha():
            rot = (ord(c) + key)
            if c.isupper():
                if rot > 90: # ord('Z')
                    rot -= 26
            else:
                if rot > 122: # ord('z')
                    rot -= 26
            c = chr(rot)
        coded.append(c)
    return ''.join(coded)
