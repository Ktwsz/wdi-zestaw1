def foo(a, b, c):
    if a[1] == 0 and b[1] == 0 and c[1] == 0:
        return (a, b, c)
    if a[1] != 0:
        a = (a[1], a[0]%a[1])
    if b[1] != 0:
        b = (b[1], b[0]%b[1])
    if c[1] != 0:
        c = (c[1], c[0]%c[1])
    return foo(a, b, c)


t = [0, 0, 0]
t[0] = int(input())
t[1] = int(input())
t[2] = int(input())
t.sort(reverse=True)

x = (t[0], t[1])
y = (t[0], t[2])
z = (t[1], t[2])

(a, b, c) = foo(x, y, z)

a, b, c = a[0], b[0], c[0]

ans = [a, b, c]
ans.sort(reverse=True)

if ans[0] != 1 and ans[1] != 1 and ans[2] != 1 and ans[0]%ans[1] == 0 and ans[0]%ans[2] == 0 and ans[1]%ans[2] == 0:
    print(ans[2])
else:
    print(1)
