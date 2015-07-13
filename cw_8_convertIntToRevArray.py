def digitize(n):
    """
    Given a non-negative integer, return an array containing a list of 
    independent digits in reverse order.
    """
    
    digit_list = []
    
    # convert int to string and reverse
    reverse_stringify_n = str(n)[::-1]
    
    # append to array
    for char in reverse_stringify_n:
        digit_list.append(int(char))
    
    return digit_list