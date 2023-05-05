# https://szkopul.edu.pl/c/programowanie-od-podstaw-2022-23/p/ukr/18452/

from sys import stdin
input = stdin.readline

def main():
    n = int(input())
    s = str(input().strip())
    w = 0
    akt_licz = ""
    
    for i in range(n):
        if s[i].isdigit():
            if s[i] == "0" and akt_licz == "":
                continue
            else:
                akt_licz += s[i]
        else:
            if len(akt_licz) != 0:
                w += int(akt_licz)
                akt_licz = ""
                
    if len(akt_licz) != 0:
        w += int(akt_licz)
        akt_licz = ""
                
    print(w)

main()