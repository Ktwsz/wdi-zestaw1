from math import sqrt
def foo(n, eps):
    a, b = n-1, 1
    while abs(b-a) > eps:
        a = (a+2*b)/3
        b = sqrt(n/a)
    return a

a = int(input())
EPS = 0.000001
print(foo(a,EPS))
