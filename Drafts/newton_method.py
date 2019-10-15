def improve(update, close, guess=1):
    while not close(guess):
        guess = update(guess)
    return guess


def approx_eq(x, y, tolerance=1e-15):
    return abs(x - y) <= tolerance


def find_zero(f, df):
    def newton_update(guess):
        return guess - (f(guess) / df(guess))

    def near_zero(guess):
        return approx_eq(f(guess), 0)

    return improve(newton_update, near_zero)


def nth_root_of_a(n, a):
    def f(x):
        return x ** n - a

    def df(x):
        return n * (x ** (n - 1))

    return find_zero(f, df)
