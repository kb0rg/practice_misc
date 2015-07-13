def shortcut( s ):
    """
    remove all the lowercase vowels in a given string.    
    """

    new_string_list = []
    vowel_string = "aeiou"
    
    for char in s:
        if char not in vowel_string:
            new_string_list.append(char)
    return "".join(new_string_list)