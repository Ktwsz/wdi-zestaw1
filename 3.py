def gen(sum):
    tab = [0, 1, 2] 
    a, b = 1, 1
    while tab[-1] <= sum:
        a, b = b, a+b
        tab.append(tab[-1]+b)
    return tab

def foo(sum):
    for i in range(0, len(tab)):
        for j in range(i+1, len(tab)):
            if tab[j]-tab[i] == sum:
                return True

    return False


a = int(input())
foo(a)
