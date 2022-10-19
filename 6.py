def foo(val, eps):
    a, b = 3, 5
    while (abs(a-b) > eps):
        x = (a+b)/2
        x_pot = x**x
        if x_pot-val == 0:
            return x
        if a**a - val < 0 and x_pot - val > 0:
            b = x
        else:
            a = x

    return a


VAL, EPS = 2022, 0.000000001

print(foo(VAL, EPS))
