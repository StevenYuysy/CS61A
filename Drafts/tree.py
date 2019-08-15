def tree(root_label, branches=[]):
    for branch in branches:
        assert is_tree(branch)
    return [root_label] + list(branches)


def label(tree):
    return tree[0]


def branches(tree):
    return tree[1:]


def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True


def is_leaf(tree):
    return not branches(tree)


def fib_tree(n):
    if n == 0 or n == 1:
        return tree(n)
    left, right = fib_tree(n-2), fib_tree(n-1)
    fib_n = label(left) + label(right)
    return tree(fib_n, [left, right])


def count_leaves(tree):
    if is_leaf(tree):
        return 1
    else:
        branch_counts = [count_leaves(branch)
                         for branch in branches(tree)]  # map function
        return sum(branch_counts)


def partition_tree(n, m):
    if n == 0:
        return tree(True)
    if n <= 0 or m == 0:
        return tree(False)
    left = partition_tree(n-m, m)
    right = partition_tree(n, m - 1)
    return tree(m, [left, right])


def print_parts(tree, partition=[]):
    if is_leaf(tree):
        if label(tree):
            print(' + '.join(partition))
    else:
        left, right = branches(tree)
        m = str(label(tree))
        print_parts(left, [m] + partition)
        print_parts(right, partition)
