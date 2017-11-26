import re
def is_isogram(string):
    chars = sorted(list(''.join(re.split('[- ,]', string.lower()))))
    iso = sorted(list(set(chars)))
    if chars == iso:
    	return True
    return False
