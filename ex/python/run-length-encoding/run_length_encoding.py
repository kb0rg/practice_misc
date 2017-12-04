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
    if not in_str:
        return in_str

    out_str = [in_str[0]]
    count = 1

    for i in range(1,len(in_str)):
        if in_str[i] == out_str[-1]:
            count += 1
            if i == len(in_str)-1:
                last = out_str.pop()
                out_str.extend([str(count), last])
        else:
            if count > 1:
                last = out_str.pop()
                out_str.extend([str(count), last])
            out_str.append(in_str[i])
            count = 1
    return ''.join(out_str)
