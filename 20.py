from math import sqrt
def foo(a, b, eps):
    while (abs(a-b) > eps):
        a_next = sqrt(a*b)
        b_next = (a+b)/2
        a, b = a_next, b_next
    return a

EPS = 0.00000001
print(foo(int(input()), int(input()), EPS))


