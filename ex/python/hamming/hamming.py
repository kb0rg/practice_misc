def distance(strand_a, strand_b):
    if not len(strand_a) == len(strand_b):
        raise ValueError('Strands must be the same length')
    if strand_a == strand_b:
        return 0

    return sum(map(lambda x,y: x!=y, strand_a, strand_b))