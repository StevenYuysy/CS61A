"""Lab 1: Expressions and Control Structures"""


def both_positive(x, y):
    """Returns True if both x and y are positive.

    >>> both_positive(-1, 1)
    False
    >>> both_positive(1, 1)
    True
    """
    return x > 0 and y > 0  # You can replace this line!


def sum_digits(n):
    """Sum all the digits of n.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> x = sum_digits(123) # make sure that you are using return rather than print
    >>> x
    6
    """
    "*** YOUR CODE HERE ***"
    if n < 10:
        return n
    last_digit = n % 10
    return last_digit + sum_digits(n // 10)

    # sum = 0
    # last_n = n
    # while last_n >= 10:
    #     sum += last_n % 10
    #     last_n = last_n // 10
    # sum += last_n
    # return sum
