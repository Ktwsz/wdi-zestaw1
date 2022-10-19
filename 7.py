def foo(n):
    a, b = 0, 1
    while a <= n:
        if a*b == n:
            return True
        a, b = b, a+b
    return False

print(foo(int(input())))
