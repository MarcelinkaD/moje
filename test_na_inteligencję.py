# https://szkopul.edu.pl/c/oki-poziom-2-20232024/p/tes/

from collections import Counter as C
from sys import stdin
input = stdin.readline

def czy_sie_da(lkop, lor, c1):
    if len(lkop) > len(lor):
        return False
    
    c2 = C(lkop)
    
    for i in c2:
        if i not in c1:
            return False
        elif c1[i] < c2[i]:
            return False
        
    return True
    

def main():
    nor = int(input())
    lor = list(map(int, input().split()))
    q = int(input())
    c1 = C(lor)
    
    for _ in range(q):
        nkop = int(input())
        lkop = list(map(int, input().split()))
        
        if czy_sie_da(lkop, lor, c1):
            wsk_lor = 0
            wsk_lkop = 0

            while wsk_lor < nor and wsk_lkop < nkop:
                if lor[wsk_lor] == lkop[wsk_lkop]:
                    wsk_lkop += 1
                wsk_lor += 1
                
            if wsk >= nor and i < nkop:
                print("NIE")
            else:
                print("TAK")
            
        else:
            print("NIE")
    
main()