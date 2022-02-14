import sys
from sys import stdin
input = stdin.readline

def main():
    slowo = str(input())
    liczba_linijek = int(input())
    listtcik = []
    settcik = set([])
    
    for line in range(liczba_linijek):
        linia = str(input())
        listtcik.extend(linia.split())
          
        for i in linia.split():
              settcik.add(i)
          
    print(listtcik)
    print(settcik)
      
main()