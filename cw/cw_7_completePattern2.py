def pattern(n):
    """
    write a function pattern which creates the following pattern up to n number 
    of rows. If the Argument is 0 or a Negative Integer then it should return 
    empty string.

    for pattern(3) return
    321
    32
    3

    """
    
    if n < 1:
        return ""
    elif n ==1:
        return "1"
    else:
        pattern_string = ""
        this_line_string = ""
        for num in range(1, n):
            # print range(n, num-1, -1)
            this_line_string = "".join(str(x) for x in range(n, num-1, -1))
            # print this_line_string
            pattern_string = pattern_string + this_line_string + "\n"
        return pattern_string + str(n)