def hey(phrase):
    """
    Bob answers 'Sure.' if you ask him a question.
    He answers 'Whoa, chill out!' if you yell at him.
    He says 'Fine. Be that way!' if you address him without actually saying
    anything.
    He answers 'Whatever.' to anything else.
    """
    if not phrase:
        return 'Fine. Be that way!'
    if phrase.upper() == phrase:
        return 'Whoa, chill out!'
    if phrase.endswith('?'):
        return 'Sure.'
    return 'Whatever.'
