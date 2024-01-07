import math
from sys import stdin
input = stdin.readline

def main():
    n, q = map(int, input().split())
    l = list(map(int, input().split()))
    jakie = [set() for _ in range(n)]
    
    for _ in range(q):
        w = 0
        a, b = map(int, input().split())
        
        for i in range(n):
            kaf = l[i]
            
            if a not in jakie[i]:
                kaf_i_a = (kaf * a) // math.gcd(kaf, a)
                
                if kaf_i_a == a:
                    jakie[i].add(a)
                    
                    if b not in jakie[i]:
                        kaf_i_b = (kaf * b) // math.gcd(kaf, b)
                        if kaf_i_b == b:
                            w += 1
                            jakie[i].add(b)
                    else:
                        w += 1
            else:
                if b not in jakie[i]:
                    kaf_i_b = (kaf * b) // math.gcd(kaf, b)
                    if kaf_i_b == b:
                        w += 1
                        jakie[i].add(b)
                else:
                    w += 1
                    
                    
        print(w)

main()
