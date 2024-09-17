# https://szkopul.edu.pl/c/marcelina-domin/p/stosy/

from itertools import accumulate as ac
from sys import stdin
input = stdin.readline

def main():
    n = int(input())
    l = list(map(int, input().split()))
    max_w = 0
    lewo = [0 for _ in range(n)]
    prawo = [0 for _ in range(n)]
    
    lewo[0] = l[0]
    for i in range(1, n):
        lewo[i] = l[i] + lewo[i - 1] // 2
        
    prawo[n - 1] = l[n - 1]
    for i in range(n - 2, -1, -1):
        prawo[i] = l[i] + prawo[i + 1] // 2
    
    for i in range(n):
        wyn = l[i]
        
        if i > 0:
            wyn += lewo[i - 1] // 2
        
        if i < n - 1:
            wyn += prawo[i + 1] // 2
        
        max_w = max(wyn, max_w)
        
    print(max_w)
    
main()