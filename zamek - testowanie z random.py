def fast(n, q, l, zap):
    ile_do_konca = [0 for _ in range(n + 1)]
    ile_do_konca[n] = l[-1]
    
    for i in range(n - 1, 0, -1):
         ile_do_konca[i] = ile_do_konca[i + 1] + l[i - 1]
         
    for i in range(1, n + 1):
        dla_potwora = ile_do_konca[i] / 20
        dla_bajtka = ile_do_konca[i] / 10
        
        ile_do_konca[i] = (dla_potwora, dla_bajtka)
        
    for i in range(q):
        p, b = zap[i]
        
        if p >= b:
            return "NIE"
        else:
            if ile_do_konca[p][0] < ile_do_konca[b][1]:
                return "NIE"
            else:
                return "TAK"
            
def brut(n, q, l, zap):
    for i in range(q):
        p, b = zap[i]
        do_laki_pot, do_laki_baj = 0, 0
        
        for k in range(p - 1, n):
            do_laki_pot += l[k]
         
        for k in range(b - 1, n):
            do_laki_baj += l[k]
            
        if do_laki_pot < do_laki_baj:
            return "NIE"
        else:
            dla_potwora = do_laki_pot / 20
            dla_bajtka = do_laki_baj / 10
            
            if dla_potwora < dla_bajtka:
                return "NIE"
            else:
                return "TAK"
            
from random import randint
licz = 0

while True:
    licz += 1
    n = randint(4, 10)
    q = randint(1, 5)
    l = [randint(1, 5) for _  in range(n)]
    zap = []

    for i in range(q):
        a = randint(1, n - 2)
        b = randint(a + 1, n)
            
        
        zap.append((a, b))
        
    w1, w2 = fast(n, q, l, zap), brut(n, q, l, zap)

    if w1 == w2:
        print("OK", licz)
    else:
        print("ZLE", licz)
        print("Fast:", w1)
        print("Brut:", w2)
        print("")
        print(n, q)
        
        for i in l:
            print(i, end = " ")
        print("")
        
        for i in zap:
            print(zap[0], zap[1])

            
        