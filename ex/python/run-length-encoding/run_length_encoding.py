def decode(in_str):
    if not in_str:
        return in_str

    out_str = []
    count = 1

    for char in in_str:
        if not char.isalpha():
            count = int(char)
        else:
            out_str.extend([char] * count)
            count = 1
    return ''.join(out_str)

def encode(in_str):
    pass
