from sys import stdin
input = stdin.readline

def f(odl, li, k, n):
    nowa_lista = []
    i = 0
    zmieniajace_sie_k = k
    while zmieniajace_sie_k != 0 and i < n:
        if li[i] + odl < li[n - 1]:
            nowa_lista.append(i + odl)
            zmieniajace_sie_k -= 1
        i += 1
    
    w = -1
    najblizej = {}
    for i in range(n):
        for x in range(k):
            if li[i] not in najblizej:
                najblizej[li[i]] = li[i] - nowa_lista[x]
            else:
                if najblizej[li[i]] 
                
            w = max(w, abs(li[i] - nowa_lista[x]))
            
    return w
        

def binary(li, n, k):
    pocz = 1
    kon = li[n - 1]
    naj_w = -10
    
    while pocz < kon:
        srodek = (pocz + kon) // 2
        co_dostalismy = f(srodek, li, k, n)
        if co_dostalismy > naj_w:
            naj_w = co_dostalismy
            pocz = srodek + 1
        else:
            kon = srodek

    return naj_w
    

def main():
    q = int(input())
    
    for _ in range(q):
        k, n = map(int, input().split())
        l = []
        
        for _ in range(n):
            l.append(int(input()))
            
        breakpoint()
        print(binary(l, n, k))
    
main()

