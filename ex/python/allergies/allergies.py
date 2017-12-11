# Incomplete.


"""
each allergen score is a power of 2, so we can use a list where the index of
each allergen corresponds to the exponent

but ...
the stub provided for is_allergic_to() makes dict lookup seems a better bet?
"""
ALLERGENS = [
    'eggs',
    'peanuts',
    'shellfish',
    'strawberries',
    'tomatoes',
    'chocolate',
    'pollen',
    'cats',
]


"""
Also
I don't understand why test_ignore_non_allergen_score_parts_only_eggs()
doesn't return ALL the allergens for 257, instead of just 'eggs'

"""

class Allergies(object):

    def __init__(self, score):
        self.score = score
        self.allergies = []
        self.temp_score = score

    def is_allergic_to(self, item):
        pass

    @property
    def lst(self):
        if self.score % 2!= 0:
            self.allergies.append('eggs')
            self.temp_score -= 1
        # check remaining allergens' values (2**i) against score, subtract
        return self.allergies

"""
Example of code that works (from user NewForester)

I don't understand how the bitwise operators work in is_allergic_to()
why doesn't the score need to be decremented?
"""
ALLERGIES = (
    'eggs',             # (1)
    'peanuts',          # (2)
    'shellfish',        # (4)
    'strawberries',     # (8)
    'tomatoes',         # (16)
    'chocolate',        # (32)
    'pollen',           # (64)
    'cats',             # (128)
)

class Allergies(object):
    """
    allergy test results
    """
    def __init__(self, score):
        self._score = score

    def is_allergic_to(self, item):
        """
        return true if the named allergy is among this object's allergies
        """
        return 1 << ALLERGIES.index(item) & self._score != 0

    @property
    def lst(self):
        """
        return this object's allergies as a list of names
        """
        return [item for item in ALLERGIES if self.is_allergic_to(item)]
