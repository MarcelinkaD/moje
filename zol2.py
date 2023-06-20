from sys import stdin
input = stdin.readline

def f(c, li, bok):
    akt_bok = bok
    i = 0
    k = 0
    while k < c and i < bok:
        if akt_bok - li[k] >= 0:
            akt_bok -= li[k]
            k += 1
        else:
            i += 1
            akt_bok = bok
    
    if k != len(li):
        return "za mały"
    else:
        return "jest ok"
    

def binary(li, x):
    pocz = max(li)
    kon = int(1e9 + 4)
    w = int(1e9 + 4)
    
    while pocz < kon:
        srodek = (pocz + kon) // 2
        if f(x, li, srodek) == "jest ok":
            w = min(w, srodek)
            kon = srodek 
        elif f(x, li, srodek) == "za mały":
            pocz = srodek + 1
    
    return w
    
    
def main():
    n = int(input())
    l = []
    
    for i in range(n):
        l.append(int(input()))
    # ~ breakpoint()
    print(binary(l, n))
    
main()

