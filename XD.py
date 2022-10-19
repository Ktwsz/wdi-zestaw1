from math import log, floor, ceil
def nie_mam_zycia_trzeba_zylowac_optymalizacje(n, i):
    a, b = 0, ceil(log(n,i))+1
    while b - a > 1:
        m = floor((a+b)/2)
        if n % (i**m) == 0:
            a = m
        else:
            b = m
    return a

def gowno(n):
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

def piwo(n):
    i = 2
    tab = []
    while n != 1:
        if n % i == 0:
            exp = nie_mam_zycia_trzeba_zylowac_optymalizacje(n, i)
            n /= i**exp
            tab.append((i, exp))
        i += 1
        while not gowno(i): i += 1
    return tab

def sperm(tab, ix, current_sperm):
    if ix == len(tab):
        val = 1
        for x in current_sperm:
            val *= x[0]**x[1]
        print(val)
        return
    for i in range(0, tab[ix][1]+1):    
        temp_sperm = current_sperm[:]
        temp_sperm.append((tab[ix][0], i))
        sperm(tab, ix+1, temp_sperm)



def foo(n):
    if n == 0:
        print(".|.")
        return
    if n == 1:
        print(1)
        return
    
    tab = piwo(n)
    sperm(tab, 0, [])


foo(int(input()))
