def gcd(a, b):
    if a < b: 
        a, b = b, a
    if b == 0:
        return a
    return gcd(b, a%b)

def lcm(a, b):
    return int(abs(a*b)/gcd(a, b))

a = int(input())
b = int(input())
c = int(input())

print(lcm(lcm(a, b), c))
