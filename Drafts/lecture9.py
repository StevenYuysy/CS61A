def cascade(n):
    if n < 10:
        print(n)
    else:
        print(n)
        cascade(n//10)
        print(n)


def inverse_cascade_1(n):
    if n > 10:
        inverse_cascade_1(n // 10)
    print(n)


def inverse_cascade_2(n):
    print(n)
    if n > 10:
        inverse_cascade_2(n // 10)


def inverse_cascade_p(n):
    inverse_cascade_1(n // 10)
    print(n)
    inverse_cascade_2(n // 10)


inverse_cascade_p(1234)


def inverse_cascade(n):
    grow(n)
    print(n)
    shrink(n)


def f_then_g(f, g, n):
    if n:
        f(n)
        g(n)


def grow(n): return f_then_g(grow, print, n // 10)


def shrink(n): return f_then_g(print, shrink, n // 10)


inverse_cascade(1234)
