def foo(n):
    sum = 1
    i = 2
    while i*i <= n:
        if n % i == 0:
            sum += i
            if n/i != i: sum += n/i
        i += 1
    return sum == n


for i in range(1000000):
    if foo(i):
        print(i)