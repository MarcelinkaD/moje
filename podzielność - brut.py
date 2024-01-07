def gen(lit, k, akt, schowek):
    if not lit:
        if akt == 0:
            return 1
        return 0
    
    klucz = (tuple((lit)), akt)
    
    if klucz in schowek:
        return schowek[klucz]
    
    wyn = 0
    czy = set()
    for i in range(len(lit)):
        litera = lit[i]
        if litera not in czy:
            wyn += gen(lit[:i] + lit[i+1:], k, ((akt * 10) + int(lit[i])) % k, schowek)
            czy.add(litera)
    
    schowek[klucz] = wyn
    
    return wyn

def fast(n, k):
    k = int(k)
    lit = []
    schowek = {}
    
    for i in n:
        lit.append(i)
    
    w = gen(lit, k, 0, schowek)
    
    print(w)
    

n, k = map(str, input().split())
fast(n, k)
