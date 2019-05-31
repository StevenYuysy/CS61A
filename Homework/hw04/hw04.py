from operator import sub, mul
from math import sqrt
HW_SOURCE_FILE = 'hw04.py'

###############
#  Questions  #
###############


def intersection(st, ave):
    """Represent an intersection using the Cantor pairing function."""
    return (st+ave)*(st+ave+1)//2 + ave


def street(inter):
    return w(inter) - avenue(inter)


def avenue(inter):
    return inter - (w(inter) ** 2 + w(inter)) // 2


def w(z): return int(((8*z+1)**0.5-1)/2)


def taxicab(a, b):
    """Return the taxicab distance between two intersections.

    >>> times_square = intersection(46, 7)
    >>> ess_a_bagel = intersection(51, 3)
    >>> taxicab(times_square, ess_a_bagel)
    9
    >>> taxicab(ess_a_bagel, times_square)
    9
    """
    "*** YOUR CODE HERE ***"
    street_a, avenue_a = street(a), avenue(a)
    street_b, avenue_b = street(b), avenue(b)
    return abs(street_a - street_b) + abs(avenue_a - avenue_b)


def squares(s):
    """Returns a new list containing square roots of the elements of the
    original list that are perfect squares.

    >>> seq = [8, 49, 8, 9, 2, 1, 100, 102]
    >>> squares(seq)
    [7, 3, 1, 10]
    >>> seq = [500, 30]
    >>> squares(seq)
    []
    """
    "*** YOUR CODE HERE ***"
    match_list = []
    for num in s:
        sqrt_num = sqrt(num)
        if sqrt_num == round(sqrt_num):
            match_list.append(int(sqrt_num))
    return match_list


def g(n):
    """Return the value of G(n), computed recursively.

    >>> g(1)
    1
    >>> g(2)
    2
    >>> g(3)
    3
    >>> g(4)
    10
    >>> g(5)
    22
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'g', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
    if n <= 3:
        return n
    else:
        return g(n - 1) + 2 * g(n - 2) + 3 * g(n - 3)


def g_iter(n):
    """Return the value of G(n), computed iteratively.

    >>> g_iter(1)
    1
    >>> g_iter(2)
    2
    >>> g_iter(3)
    3
    >>> g_iter(4)
    10
    >>> g_iter(5)
    22
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'g_iter', ['Recursion'])
    True
    """
    "*** YOUR CODE HERE ***"
    total, k = 0, 1
    prev_k_1, prev_k_2, prev_k_3 = 3, 2, 1
    while k <= n:
        if k <= 3:
            total = k
        else:
            total = prev_k_1 + 2 * prev_k_2 + 3 * prev_k_3
            prev_k_1, prev_k_2, prev_k_3 = total, prev_k_1, prev_k_2
        k += 1
    return total


def count_change(amount):
    """Return the number of ways to make change for amount.

    >>> count_change(7)
    6
    >>> count_change(10)
    14
    >>> count_change(20)
    60
    >>> count_change(100)
    9828
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'count_change', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
    def max_power_2(n):
        """Return max power 2 value of n
          >>> max_power_2(1)
          1
          >>> max_power_2(4)
          4
          >>> max_power_2(5)
          4
          >>> max_power_2(10)
          8
        """
        # total = 1
        # while total * 2 <= n:
        #     total *= 2
        # return total
        if n == 1:
            return 1
        if n / 2 == n // 2:
            return 2 * max_power_2(n / 2)
        else:
            return 2 * max_power_2((n - 1) / 2)

    def recursive_change(n, k):
        if n < 0:
            return 0
        elif n <= 1:
            return 1
        if k == 1:
            return 1
        return recursive_change(n, max_power_2(k // 2)) + recursive_change(n - k, k)

    return recursive_change(amount, max_power_2(amount))


def print_move(origin, destination):
    """Print instructions to move a disk."""
    print("Move the top disk from rod", origin, "to rod", destination)


def move_stack(n, start, end):
    """Print the moves required to move n disks on the start pole to the end
    pole without violating the rules of Towers of Hanoi.

    n -- number of disks
    start -- a pole position, either 1, 2, or 3
    end -- a pole position, either 1, 2, or 3

    There are exactly three poles, and start and end must be different. Assume
    that the start pole has at least n disks of increasing size, and the end
    pole is either empty or has a top disk larger than the top n start disks.

    >>> move_stack(1, 1, 3)
    Move the top disk from rod 1 to rod 3
    >>> move_stack(2, 1, 3)
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 3
    >>> move_stack(3, 1, 3)
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 3 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 1
    Move the top disk from rod 2 to rod 3
    Move the top disk from rod 1 to rod 3
    """
    assert 1 <= start <= 3 and 1 <= end <= 3 and start != end, "Bad start/end"
    "*** YOUR CODE HERE ***"

###################
# Extra Questions #
###################


def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'make_anonymous_factorial', ['Assign', 'AugAssign', 'FunctionDef', 'Recursion'])
    True
    """
    return 'YOUR_EXPRESSION_HERE'
