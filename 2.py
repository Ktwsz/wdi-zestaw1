YEAR = 2022

def check(a, b):
    while a < YEAR:
        a, b = b, a+b
    
    return a == YEAR


def foo():
    sum = 2
    while True:
        a, b = 0, sum
        while b > 0:
            if check(a, b):
                return a, b
            a, b = a+1, b-1
        sum += 1

print(foo())
