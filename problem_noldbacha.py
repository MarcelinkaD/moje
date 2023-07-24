# https://codeforces.com/problemset/problem/17/A

import math
from itertools import accumulate as ac
from sys import stdin
input = stdin.readline

def main():
    n, k = map(int, input().split())
    MAXN = 10007
    pierw = []
    w = 0
    sito = [True for _ in range(MAXN)]
    sito[0], sito[1] = False, False

    for i in range(2, int(math.sqrt(MAXN))):
        if sito[i] == True:
            for j in range(i + i, MAXN, i):
                sito[j] = False
    
    for i in range(n):
        if sito[i]:
            pierw.append(i)
                
    for i in range(len(pierw) - 2):
        razem = pierw[i] + pierw[i + 1]
        if sito[razem + 1] and razem + 1 <= n:
            w += 1
#    breakpoint()
    if w >= k:
        print("YES")
    else:
        print("NO")

main()
