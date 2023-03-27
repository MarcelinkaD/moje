# https://szkopul.edu.pl/problemset/problem/QgFenN44XX_a8nX7RPmBNph4/site/?key=statement

import bisect as bi
from sys import stdin
input = stdin.readline    
    
def main():
    n = int(input())
    duze = list(map(int, input().split()))
    male = []
    duze.sort(reverse = True)
    baj = 2
    w = 0
    
    while baj < duze[0]:
        while duze[-1] < baj:
            male.append(duze[-1])
            duze.pop()
            
        if len(male) == 0:
            print("NIE")
            return 0
                
        baj += male[-1]
        male.pop()
        w += 1

    print(w)
    
main()