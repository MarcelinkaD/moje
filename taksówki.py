# https://szkopul.edu.pl/c/olimpiada-od-podstaw-2023-24/p/

from sys import stdin
input = stdin.readline

def wylicz(x, y, baj):
    if y <= baj:
        return x
    else:
        do_baj = y - baj
        x -= do_baj
        return x

def main():
    do, do_stacji, n = map(int, input().split())
    l = list(map(int, input().split()))
    baj = 0
    w = 0
    ostatnia = -1
    l.sort(reverse = True)
    do_ominięcia = -1
    
    for i in range(n - 1, -1, -1):
        if l[i] >= do - do_stacji:
            ostatnia = l[i]
            do_ominięcia = i
            break

    if ostatnia == -1:
        print(0)
        return
    
    for i in range(n):
        if i != do_ominięcia:
            chcemy = (do + do_stacji - ostatnia) // 2
            if baj >= chcemy:
                baj += ostatnia
                w += 1
                ostatnia = 0
                break
            else:
                if l[i] < do_stacji - baj:
                    print(0)
                    return
                
                baj += l[i] - (do_stacji - baj)
                w += 1
                
                if baj >= do:
                    break
                
    if ostatnia != 0 and baj < do:
        w += 1
        baj += wylicz(ostatnia, do_stacji, baj)
        
    if baj >= do:
        print(w)
    else:
        print(0)
    
main()