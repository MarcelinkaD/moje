# https://szkopul.edu.pl/problemset/problem/KiEvCpZBaUNRCp6oTZx2oAQ4/site/?key=statement

from sys import stdin
input = stdin.readline

def main():
    n = int(input())
    bier = []
    
    for _ in range(n):
        i = int(input())
        bier.append(i)
        
    bier.sort()
    p, k, akt_w, max_w = 1, 0, 1, -1
    
    while k < n:
        while p < n and bier[k] + bier[k + 1] > bier[p]:
            p += 1
            akt_w += 1
            max_w = max(akt_w, max_w)
            
        akt_w -= 1
        k += 1
        
            
    
    print(max_w)

    
main()