from operator import add, sub, mul, truediv


def convertor(c, f):
    """Connect c to f with constraints to convert from Celsius to Fahrenheit"""
    u, v, w, x, y = [connector() for _ in range(5)]
    multiplier(c, w, u)
    multiplier(v, x, u)
    adder(v, y, f)
    constant(w, 9)
    constant(x, 5)
    constant(y, 32)


def adder(a, b, c):
    return make_ternary_constraint(a, b, c, add, sub, sub)


def make_ternary_constraint(a, b, c, ab, ca, cb):
    def new_value():
        av, bv, cv = [connector['has_val']() for connector in(a, b, c)]
        if av and bv:
            c['set_val'](constraint, ab(a['val'], b['val']))
        elif av and cv:
            b['set_val'](constraint, ca(c['val'], a['val']))
        elif bv and cv:
            a['set_val'](constraint, cb(c['val'], b['val']))

    def forget_value():
        for connector in (a, b, c):
            connector['forget'](constraint)
    constraint = {'new_val': new_value, 'forget': forget_value}
    for connector in (a, b, c):
        connector['connect'](constraint)
    return constraint


def multiplier(a, b, c):
    return make_ternary_constraint(a, b, c, mul, truediv, truediv)


def constant(connector, value):
    constarint = {}
    connector['set_val'](constarint, value)
    return constarint
