# https://szkopul.edu.pl/c/testowy_dd/p/pos/

from sys import stdin
input = stdin.readline

def suma(x):
    k = 0
    for i in x:
        k += int(i)
    return k

def main():
    od, do = map(int, input().split())
    w = 0
    
    for i in range(od, do + 1):
        w = max(w, suma(str(i)))
        
    print(w)
    
main()