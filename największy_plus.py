# https://szkopul.edu.pl/problemset/problem/DJN8oaDlV5EfddZP8aBWyA_t/site/?key=statement

import math
from sys import stdin
input = stdin.readline

def min_w_prze(L, R, table):
    j = int(math.log2(R - L + 1))
    if table[L][j] <= table[R - (1 << j) + 1][j]:
        return table[L][j]
 
    else:
        return table[R - (1 << j) + 1][j]

def zbuduj_table(li, n):
    logn = math.ceil(math.log2(n)) + 1
    table = [[0] * logn for _ in range(n)]
    
    for i in range(0, n):
        table[i][0] = li[i]
     
    j = 1
    
    while (1 << j) <= n:
        i = 0
        while (i + (1 << j) - 1) < n:
            if (table[i][j - 1] <
                table[i + (1 << (j - 1))][j - 1]):
                table[i][j] = table[i][j - 1]
            else:
                table[i][j] = table[i + (1 << (j - 1))][j - 1]
             
            i += 1
        j += 1
    
    return table

def czy_da_sie(ra, li, table):
    for i in range(ra, len(li) - ra):
        if li[i] >= (ra + ra + 1):
            if min_w_prze(i - ra, i + ra, table) >= ra + 1:
                return True
        
    return False


def binary(maxi, li, table):
    pocz = 0
    kon = maxi
    
    while pocz < kon:
        srodek = (pocz + 1 + kon) // 2
        if czy_da_sie(srodek, li, table):
            pocz = srodek
        else:
            kon = srodek - 1
        
    return pocz

def main():
    n = int(input())
    wierz = list(map(int, input().split()))
    maxi = max(wierz)
    table = zbuduj_table(wierz, n)
    
    print(binary(maxi, wierz, table))
    
main()