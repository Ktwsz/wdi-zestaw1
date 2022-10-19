def foo():
    a, b = 53, 4
    print(a)
    print(b)
    while b < 1000000:
        a, b = b, a+b
        print(b)

foo()
