def chuj(x, eps):
    X = x*x
    i = 2
    val = -X/2
    prev, ans = 1, 1+val
    while abs(ans-prev) > eps:
        prev = ans
        val *= -1*X
        val /= (i+1)*(i+2)
        i += 2
        ans += val
    return ans

EPS = 0.000001
print(chuj(float(input()), EPS))
