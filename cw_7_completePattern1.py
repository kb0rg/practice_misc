"""
You have to write a function pattern which returns the following Pattern
(See Pattern & Examples) up to n number of rows.

Note:
Returning the pattern is not the same as Printing the pattern.

Rules/Note:
If n < 1 then it should return "" i.e. empty string.
There are no whitespaces in the pattern.

Pattern:
1
22
333
....
.....
nnnnnn

Examples:
>>> pattern(2)
1
22

>>> pattern(5)
1
22
333
4444
55555

>>> pattern(11)
1
22
333
4444
55555
666666
7777777
88888888
999999999
10101010101010101010
1111111111111111111111

* Hint: Use \n in string to jump to next line
"""
def pattern(n):

    if n < 1:
        return ""
    elif n == 1:
        return "1"
    else:
        pattern_str = ""
        for x in range(1,n):
            pattern_str += "{0}".format(x) * x +"\n"
        pattern_str += "{0}".format(n) * n
        return pattern_str

if __name__ == "__main__":

    import doctest
    doctest.testmod()

