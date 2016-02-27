#Try to make your own gcd method without importing stuff

def mygcd(x,y):

    """
    Find the greatest common divisor of two positive integers. The integers can 
    be large, so you need to find a clever solution.

    The inputs x and y are always greater or equal to 1, so the the greatest 
    common divisor will always be an integer that is also greater or equal to 1.
    
    >>> mygcd(30,12)
    6
    >>> mygcd(8,9)
    1
    >>> mygcd(1,1)
    1
    >>> mygcd(5000,1)
    1
    >>> mygcd(45,15)
    15
    >>> mygcd(6,30)
    6       
    >>> mygcd(10927782,6902514)
    846
    >>> mygcd(1590771464,1590771620)
    4
    >>> mygcd(33504,32511)
    3

    """

    """
    got stuck, looked up answer. mind blown.
    https://en.wikipedia.org/wiki/Euclidean_algorithm
    """

    """
    but I do not grok the mechanics of the solutions. 
    http://www.codewars.com/kata/greatest-common-divisor/solutions?show-solutions=1

    while y:
        x,y=y,x%y
    return x

    or:

    if x%y == 0:
        return y
    else:
        return mygcd(y,x%y)

    """

    # still blowing my mind. adding lots of print statements to see what's happening.
    while y:
        print "x, y was: " + str(x) +"," + str(y)
        print "then magic shit happens."
        print "like, x%y is: " + str(x%y)
        x,y=y,x%y
        print "x, y is now: " + str(x) +"," + str(y)
        print "keep cycling?"
    print "x is now the answer: " + str(x)
    return x

    # #edge cases:
    # if x == 1 or y == 1:
    #     # print "duh. gcd is: 1"
    #     return 1
    # if max(x,y) % min(x,y) == 0:
    #     # print "ok.  gcd is: " + str(min([x,y]))
    #     return min(x,y)

    # """
    # start testing divisors of the lower number.
    # iterate in reverse from highest possible divisor of lower, 
    # ie lower divided by 2, then 3, then 4...
    # confirm, while iterating, that lower divided by iterator produces a 
    # whole number, otherwise skip to next iterator.
    # """
    # lower = min(x,y)
    # i = 2
    # # eliminate any 
    # if lower % i != 0:
    #     i+=1
    # div = (lower/i)

    # while div > 0:
    #     print "i: " + str(i)
    #     print "div: " + str(div)
    #     print "x % div: " + str(x % div)
    #     print "y % div: " + str(y % div)
    #     if x % div == 0 and y % div ==0:
    #         print "!!!!! gcd is: " + str(div)
    #         return div
    #     else:
    #         print "NEXT!"
    #         i += 1
    #         # repeating code here. need optimization?
    #         while lower % i != 0:
    #             i+=1
    #         div = (lower/i)


if __name__ == "__main__":

    # mygcd(8,9)
    # mygcd(6,30)
    # mygcd(5000,1)
    # mygcd(10927782,6902514)
    # mygcd(10927783,6902513)
    # mygcd(1590771464,1590771620)
    # mygcd(33504,32511)
    mygcd(156, 23644309756)

    # import doctest
    # doctest.testmod()





