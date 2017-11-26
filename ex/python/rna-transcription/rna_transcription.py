
decode = {
    'G': 'C',
    'C': 'G',
    'T': 'A',
    'A': 'U',
}

def to_rna(dna_strand):
    try:
        transcribe = [decode[x] for x in dna_strand]
    except KeyError:
        raise ValueError('Not a valid input')

    return ''.join(transcribe)