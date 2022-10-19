def foo(n):
    if n == 0:
        print(".|.")
        return
    i = 1
    while i*i <= n:
        if n%i == 0:
            print(i)
            print(n/i)
        i += 1


foo(int(input()))
