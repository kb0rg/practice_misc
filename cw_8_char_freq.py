def char_freq(message):
    """
    you will get passed a string, you will then return a dictionary 
    with as keys the characters, and as values how many times that 
    character is in the string. You can assume you will be given valid input.
    
    """
    
    msg_dict = {}
    
    for char in message:
        msg_dict[char] = msg_dict.get(char, 0)+1
    
    return msg_dict