# Look into Pascal's triangle
# see sol by NewForester: (((nn / 2) * (nn + 1)) ** 2)
def square_of_sum(num):
    return sum(range(1, num+1))**2


def sum_of_squares(num):
    return sum([x**2 for x in range(1, num+1)])


def difference(num):
    return square_of_sum(num)-sum_of_squares(num)
