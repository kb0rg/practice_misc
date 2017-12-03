def decode(in_str):
    if not in_str:
        return in_str

    out_str = []
    count = []

    for char in in_str:
        if char.isnumeric():
            count.append(char)
        else:
            if not count:
                mult = 1
            else:
                mult = int(''.join(count))
            out_str.extend([char] * mult)
            count = []
    return ''.join(out_str)

def encode(in_str):
    pass
