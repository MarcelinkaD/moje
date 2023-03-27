# https://szkopul.edu.pl/problemset/problem/QgFenN44XX_a8nX7RPmBNph4/site/?key=statement

from sys import stdin
input = stdin.readline

def main():
    n = int(input())
    l = list(map(int, input().split()))
    l.sort()
    w = 0
    baj = 2
    maxi = max(l)
    
    if l[0] >= 2:
        print("NIE")
        return 
    
    while baj < maxi:
        for i in range(len(l) + 1):
            if l[i] >= baj:
                index = i - 1
                if index == -1:
                    print("NIE")
                    return
                baj += l[i - 1]
                w += 1
                l.remove(l[i - 1])
                break
            
                
                
            
    if baj >= maxi:
        print(w)
    else:
        print("NIE")             
    
main()