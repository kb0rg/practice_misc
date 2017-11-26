def distance(strand_a, strand_b):
    if not len(strand_a) == len(strand_b):
        raise ValueError('Strands must be the same length')
    if strand_a == strand_b:
        return 0

    dist = 0
    for i in range(len(strand_a)):
        if not strand_a[i] == strand_b[i]:
            dist += 1
    return dist