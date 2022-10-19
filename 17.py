def foo(a, b, eps):
    if b == 0:
        return -1
    prev = a / b
    a, b = b, a+b
    current = a/b
    while (abs(prev-current) > eps):
        prev = current
        a, b = b, a+b
        current = a/b

    return current

EPS = 0.000000001
print(foo(int(input()), int(input()), EPS))
