class Link:
    """
    >>> s = Link(3, Link(4, Link(5)))
    >>> len(s)
    3
    >>> s[1]
    4
    >>> s
    Link(3, Link(4, Link(5)))
    >>> s_first = Link(s, Link(6))
    >>> s_first
    Link(Link(3, Link(4, Link(5))), Link(6))
    >>> len(s_first)
    2
    >>> len(s_first[0])
    3
    >>> s_first[0][2]
    5
    >>> s + s
    Link(3, Link(4, Link(5, Link(3, Link(4, Link(5))))))
    """
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __getitem__(self, i):
        if i == 0:
            return self.first
        return self.rest[i - 1]

    def __len__(self):
        return 1 + len(self.rest)

    def __repr__(self):
        if self.rest is Link.empty:
            rest = ''
        else:
            rest = ', ' + Link.__repr__(self.rest)
        return 'Link({0}{1})'.format(self.first, rest)

    def __add__(self, link):
        if self is Link.empty:
            return link
        return Link(self.first, Link.__add__(self.rest, link))


def map_link(fn, link):
    """
    >>> s = Link(3, Link(4, Link(5)))
    >>> map_link(lambda s: s * s, s)
    Link(9, Link(16, Link(25)))
    >>> a = Link(1, Link(1, Link(())))
    >>> map_link(lambda s: s, a)
    Link(1, Link(1, Link(())))
    """
    if link is Link.empty:
        return Link.empty
    return Link(fn(link.first), map_link(fn, link.rest))


def filter_link(fn, link):
    """
    >>> s = Link(3, Link(4, Link(5)))
    >>> filter_link(lambda s: s > 4, s)
    Link(5)
    """
    if link is Link.empty:
        return Link.empty
    if fn(link.first) is True:
        return Link(link.first, filter_link(fn, link.rest))
    else:
        return filter_link(fn, link.rest)


def join_link(link, link_operator):
    """
    >>> s = Link(3, Link(4, Link(5)))
    >>> join_link(s, ', ')
    '3, 4, 5'
    >>> a = Link(1, Link(1))
    >>> join_link(a, ', ')
    '1, 1'
    """
    if link is Link.empty:
        return ""
    if link.rest is Link.empty:
        return str(link.first)
    return str(link.first) + link_operator + join_link(link.rest, link_operator)


def partitions(n, m):
    """Return a linked list of partitions of n using parts of up to m.
    Each partition is represented as a linked list.
    >>> partitions(2, 2)
    Link(Link(2), Link(1, Link(1)))
    >>> partitions(6, 4)
    Link(Link(4, Link(2)), Link(Link(4, Link(1, Link(1))), Link(Link(3, Link(3)), Link(Link(3, Link(2, Link(1))), Link(Link(3, Link(1, Link(1, Link(1)))), Link(Link(2, Link(2, Link(2))), Link(Link(2, Link(2, Link(1, Link(1)))), Link(Link(2, Link(1, Link(1, Link(1, Link(1))))), Link(Link(1, Link(1, Link(1, Link(1, Link(1, Link(1)))))))))))))))
    """
    if n == 0:
        return Link(Link.empty)  # A list containing the empty partition
    elif n < 0 or m == 0:
        return Link.empty
    else:
        using_m = partitions(n-m, m)
        with_m = map_link(lambda s: Link(m, s), using_m)
        without_m = partitions(n, m-1)
        return Link.__add__(with_m, without_m)


def print_partitions(n, m):
    """
    >>> print_partitions(6, 4)
    4 + 2
    4 + 1 + 1
    3 + 3
    3 + 2 + 1
    3 + 1 + 1 + 1
    2 + 2 + 2
    2 + 2 + 1 + 1
    2 + 1 + 1 + 1 + 1
    1 + 1 + 1 + 1 + 1 + 1
    """
    lists = partitions(n, m)
    # print(lists)
    strings = map_link(lambda s: join_link(s, " + "), lists)
    print(join_link(strings, "\n"))
