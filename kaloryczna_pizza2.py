# https://szkopul.edu.pl/c/olimpiada-od-podstaw-2023-24/p/kap/

from sys import stdin
input = stdin.readline

def main():
    n, m = map(int, input().split())
    matrix = [[0 for _  in range(m + 1)]]
    pref = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    
    for _ in range(n):
       lit = list(map(int, input().split()))
       lit.insert(0, 0)
       matrix.append(lit)
           
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            pref[i][j] = pref[i][j - 1] + pref[i - 1][j] + matrix[i][j] - pref[i - 1][j - 1]
            
    q = int(input())
    
    for _ in range(q):
        w_1, k_1, w_2, k_2 = map(int, input().split())
        
        print(pref[w_2][k_2] - pref[w_1 - 1][k_2] - pref[w_2][k_1 - 1] + pref[w_1 - 1][k_1 - 1])
    
       
main()
