empty = 'empty'


def is_link(link):
    return link == empty or (len(link) == 2 and is_link(link[1]))


def link(first, rest):
    assert(is_link(rest))
    return [first, rest]


def first(link):
    assert is_link(link)
    return link[0]


def rest(link):
    assert is_link(link)
    return link[1]


def len_link(link):
    """Return the length of link
    >>> len_link(link(1))
    1
    >>> len_link(link(1, link(2)))
    2
    """
    assert is_link(link)
    length = 0
    while link != empty:
        link, length = rest(link), length + 1
    return length


def getitem_link(link, i):
    assert is_link(link)
    while i > 0:
        link, i = rest(link), i - 1
    return first(link)


def len_link_recursive(link):
    if link == empty:
        return 0
    else:
        return len_link_recursive(rest(link)) + 1


def getitem_link_recursive(link, i):
    if i == 0:
        return first(link)
    else:
        return getitem_link_recursive(rest(link), i - 1)


def extend_link(s, t):
    if s == empty:
        return t
    return link(first(s), extend_link(rest(s), t))


def apply_to_all_link(f, s):
    if s == empty:
        return s
    return link(f(first(s)), apply_to_all_link(f, rest(s)))


def keep_if_link(f, s):
    if s == empty:
        return s
    exist = f(first(s))
    if exist:
        return link(first(s), keep_if_link(f, rest(s)))
    return keep_if_link(f, rest(s))


def join_link(s, separator):
    if s == empty:
        return ''
    elif rest(s) == empty:
        return str(first(s))
    return str(first(s)) + separator + join_link(rest(s), separator)


def mutable_link():
    contents = empty

    def dispatch(message, value=None):
        nonlocal contents
        if message == 'len':
            return len_link(contents)
        elif message == 'getitem':
            return getitem_link(contents, value)
        elif message == 'push_first':
            contents = link(value, contents)
        elif message == 'pop_first':
            pop_value = first(contents)
            contents = rest(contents)
            return pop_value
        elif message == 'str':
            return join_link(contents, ', ')
    return dispatch


def to_mutable_link(source):
    """Return a functional list with the same contents as source."""
    s = mutable_link()
    for element in reversed(source):
        s('push_first', element)
    return s


def mutable_dict():
    contents = []

    def dispatch(message, key=None, value=None):
        nonlocal contents
        if message == 'get_item':
            pair = [r for r in contents if r[0] == key]
            if len(pair == 1):
                return pair[0][1]
        elif message == 'set_item':
            non_matches = [r for r in contents if r[0] != key]
            contents = non_matches + [[key, value]]
    return dispatch
