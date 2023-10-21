from sys import stdin
input = stdin.readline

def main():
    MAXN = 1000000 + 3
    gdzie_bony = [0] * MAXN
    m = int(input())
    num_klienta = 1
    ost = [0] * MAXN
    l = []
    
    for _ in range(m):
        p = int(input())
        gdzie_bony[p] = 1
    
    ile_bonow = 0
    q = int(input())
-
    for _ in range(q):
        akt_kupione_pacz = 0
        a = int(input())
        for i in range(ost[a] + a, 1000001, a):
            if akt_kupione_pacz == a:
                break
            
            if gdzie_bony[i] == -1:
                continue
            
            if gdzie_bony[i] == 1:
                ile_bonow += 1
                l.append(num_klienta)
                
            num_klienta += 1
            ost[a] = i
            gdzie_bony[i] = -1
            akt_kupione_pacz += 1
            
            
        
    
    print(ile_bonow)
    
    for i in l:
        print(i)
    
    
main()

