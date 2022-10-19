def foo(eps):
    e = 2
    val = 0.5
    i = 2
    while val > eps:
        e += val
        i += 1
        val /= i
    return e 


EPS = 0.0000001
print(foo(EPS))
