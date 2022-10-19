def foo():
    a, b = 0, 1
    print(a)
    print(b)
    while b < 1000000:
        a, b = b, a+b
        print(b)

foo()
