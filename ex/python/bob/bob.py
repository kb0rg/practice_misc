# TODO: fix for phrase w/ only non-alpha char

"""
fixes:
test_non_letters_with_question
test_question_with_only_numbers

fails:
test_forceful_question
test_only_numbers
"""

def hey(phrase):
    """
    Bob answers 'Sure.' if you ask him a question.
    He answers 'Whoa, chill out!' if you yell at him.
    He says 'Fine. Be that way!' if you address him without actually saying
    anything.
    He answers 'Whatever.' to anything else.
    """
    phr = phrase.strip()
    if not phr:
        return 'Fine. Be that way!'
    if phr.endswith('?'):
        return 'Sure.'
    if phr.upper() == phr:
        return 'Whoa, chill out!'
    return 'Whatever.'