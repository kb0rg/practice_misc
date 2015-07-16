def factorial(n):
    """
    function that takes an integer 'n' and returns 'n!'
    """

    if n < 0:
        return None
    elif n == 0:
        return 1
    else:
        i = 1
        f = 1
        while i < n+1:
            f = i * f
            i +=1
            
    return f


"""
(use recursion)

In mathematics, the factorial of integer 'n' is written as 'n!'. It is equal to the product of n and every integer preceding it. For example: 5! = 1 x 2 x 3 x 4 x 5 = 120

Your mission is simple: write a function that takes an integer 'n' and returns 'n!'.

You are guaranteed an integer argument. For any values outside the positive range, return null, nil or None .

Note: 0! is always equal to 1. Negative values should return null;

For more on Factorials : http://en.wikipedia.org/wiki/Factorial

Test.expect(factorial(1) == 1)
Test.expect(factorial(5) == 120)
"""

print "n = 1 should return 1, function returns: " + str(factorial(1))
print "n = 5 should return 120, function returns: " + str(factorial(5))