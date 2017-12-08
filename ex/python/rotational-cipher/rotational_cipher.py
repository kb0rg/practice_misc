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



"""
# elegant solution from yoongkang on exercism

from string import (
    ascii_letters as letters,
    ascii_lowercase as lower,
    ascii_uppercase as upper,
)

def generate_translation_table(key):
    return str.maketrans(letters, lower[key:] + lower[:key] + upper[key:] + upper[:key])

def rotate(text, key):
    return text.translate(generate_translation_table(key))
"""