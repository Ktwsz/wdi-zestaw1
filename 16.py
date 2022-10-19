def piwo(a):
    step = 0
    while (a != 1):
        step += 1
        a = (a % 2) * (3 * a + 1) + (1 - a % 2) * a / 2
    return step

def foo():
    ans, step = 1, 1
    for i in range(2, 10001):
        t = piwo(i)
        if step < t:
            step = t
            ans = i
    return ans

print(foo())
