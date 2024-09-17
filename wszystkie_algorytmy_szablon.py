import math
import queue

def sumy_prefiksowe(x):
    n = len(x)
    sumy = [0 for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        sumy[i] = sumy[i - 1] + x[i - 1]
        
    return sumy

def gasienica(x, k):
    n = len(x)
    pocz = -1
    kon = 0
    wynik = 0
    akt_suma = 0
    
    while kon < n - 1:
        while pocz < n - 1 and akt_suma <= k:
            pocz += 1
            akt_suma += x[pocz]
            
            if akt_suma == k:
                wynik += 1
                
        akt_suma -= x[kon]
        kon += 1
        
        if akt_suma == k:
            wynik += 1
            
    return wynik

def binary(x, co):
    n = len(x)
    pocz = 0
    kon = n
    
    while pocz < kon:
        srodek = (pocz + kon) // 2
        
        if x[srodek] == co:
            return srodek
        elif x[srodek] < co:
            pocz = srodek
        else:
            kon = srodek - 1
            
    return pocz

def NWW(a, b):
    return (a * b) // math.gcd(a, b)
        
def NWD(a, b):
    return math.gcd(a, b)

def sito(MAXN):
    sito = [True for _ in range(MAXN + 1)]
    sito[0] = False
    sito[1] = False
    
    for i in range(2, MAXN + 1):
        if sito[i]:
            for k in range(i + i, MAXN + 1, i):
                sito[k] = False
                
    return sito

def BFS(graf, n, od):
    odw = [False for _ in range(n + 1)]
    odw[od] = True
    kol = queue.Queue()
    kol.put(od)
    
    while not kol.empty():
        u = kol.get()
        for sasiad in graf[u]:
            if not odw[sasiad]:
                odw[sasiad] = True
                kol.put(sasiad)
                
def BFS_z_liczeniem_odl(graf, n, od):
    odl = [-1 for _ in range(n + 1)]
    odl[od] = 0
    kol = queue.Queue()
    kol.put(od)
    
    while not kol.empty():
        u = kol.get()
        for sasiad in graf[u]:
            if odl[sasiad] == -1:
                odl[sasiad] = odl[u] + 1
                kol.put(sasiad)
                
    return odl
                
                
def DFS(graf, v, odw):
    if not odw[v]:
        odw[v] = True
        for sasiad in graf[v]:
            DFS(graf, sasiad, odw)
    
def wszystkie_podzbiory(l, n):
    do = (2 ** n)
    
    for opcja in range(do):
        for i in range(n):
            if (opcja >> i) & 1:
                print(l[i], end = " ")
        print("")
    

print(BFS_z_liczeniem_odl([[], [2, 3], [1, 4], [1], [2]], 4, 1))
wszystkie_podzbiory([1, 2, 3], 3)
    
    
    