def foo(n):
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

print(foo(int(input())))
