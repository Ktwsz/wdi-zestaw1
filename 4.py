def foo(n):
    a, i = 1, 1

    while (a <= n):
        i += 1
        a += 2*i-1

    return i-1

a = int(input())
print(foo(a))
