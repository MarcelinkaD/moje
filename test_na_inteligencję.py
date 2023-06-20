# https://szkopul.edu.pl/c/olimpiada-od-podstaw-2022-23/p/tes/

from collections import Counter as C
from sys import stdin
input = stdin.readline

def t1(c1, c2):
    for i in c2:
        if i not in c1:
            return "NIE"
        elif c2[i] > c1[i]:
            return "NIE"
    return "TAK"

def t2(l1, l2):
    licz1, licz2 = 0, 0
    while licz2 < len(l2):
        czy_break = False
        for i in range(licz1, len(l1)):
            if l1[i] == l2[licz2]:
                licz2 += 1
                licz1 = i
                czy_break = True
                break
            
        if czy_break == False:
            return "NIE"
        
    return "TAK"

def main():
    n = int(input())
    ciag = list(map(int, input().split()))
    q = int(input())
    c1 = C(ciag)
    
    for _ in range(q):
        k = int(input())
        ciag2 = list(map(int, input().split()))
        c2 = C(ciag2)
        wynik_test1 = t1(c1, c2)
        
        if wynik_test1 != "TAK":
            print("NIE")
            continue
        
        wynik_test2 = t2(ciag, ciag2)
        
        if wynik_test2 != "TAK":
            print("NIE")
            continue         
        
        print("TAK")
    
main()