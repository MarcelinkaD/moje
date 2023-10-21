# https://szkopul.edu.pl/c/oki-poziom-2-20232024/p/sta/18479/

import bisect as bi
from sys import stdin
input = stdin.readline

def main():
    b, k, z = map(int, input().split())
    n1 = int(input())
    l1 = list(map(int, input().split()))
    m1, m2, m3 = 0, 0, 0
    
    for i in range(n1):
        l1[i] *= b
        if l1[i] > m1:
            m1 = l1[i]
        
    n2 = int(input())
    l2 = list(map(int, input().split()))
    
    for i in range(n2):
        l2[i] *= k
        if l2[i] > m2:
            m2 = l2[i]
        
    n3 = int(input())
    l3 = list(map(int, input().split()))
    
    for i in range(n3):
        l3[i] *= z
        if l3[i] > m3:
            m3 = l3[i]
            
    l3.sort()
            
    min_w = (m1 + m2 + m3) / 2
    w = 0
    
    for i in range(n1):
        akt1 = l1[i]
        if akt1 > min_w:
            w += n2 * n3
        else:
            for j in range(n2):
                akt2 = l2[j]
                if akt1 + akt2 > min_w:
                    w += n3
                else:
                    od = bi.bisect_left(l3, min_w - (akt1 + akt2))
                    if od != n3:
                        if l3[od] + akt1 + akt2 > min_w:
                            w += n3 - od
                        else:
                            w += n3 - (od + l3.count(l3[od]))
                        
    print(w)
    
main()