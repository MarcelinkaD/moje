# https://szkopul.edu.pl/c/olimpiada-od-podstaw-2023-24/p/naw/

from sys import stdin
input = stdin.readline

def main():
    q = int(input())
    otw = ["(", "{", "[", "<"]
    zam = [")", "}", "]", ">"]
    
    for _ in range(q):
        czy_break = False
        s = str(input().strip())
        stos = []
        
        for i in s:
            if i in otw:
                stos.append(i)
            else:
                if len(stos) != 0:
                    if otw.index(stos[-1]) == zam.index(i):
                        stos.pop(-1)
                else:
                    czy_break = True
                    break
                
            if czy_break:
                break
            
        if czy_break:
            print("NIE")
            czy_break = False
        else:    
            if len(stos) == 0:
                print("TAK")
            else:
                print("NIE")
        
        
main()