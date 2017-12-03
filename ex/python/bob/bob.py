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
    if phr.upper() == phr:
        return 'Whoa, chill out!'
    if phr.endswith('?'):
        return 'Sure.'
    return 'Whatever.'
