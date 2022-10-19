from math import sqrt
def foo(eps):
    a = sqrt(0.5)
    b = sqrt(0.5+0.5*a)
    ans = 2/(a*b)
    while abs(a-b) > eps:
        a, b = b, sqrt(0.5+0.5*b)
        ans /= b
    return ans

EPS = 0.000001
print(foo(EPS))
