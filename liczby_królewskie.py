# https://szkopul.edu.pl/c/testowy_dd/p/krolewskie/

from sys import stdin
input = stdin.readline

def czy_krol(x):
    jed = 0
    
    while x != 0:
        if x % 2 == 1:
            jed += 1
        x //= 2
        
    if jed % 2 == 0:
        return True
    return False

def fast():
    q = int(input())
    
    for _ in range(q):
        n = int(input())
        
        l1 = 2 * n - 1
        l2 = 2 * n - 2
        
        if czy_krol(l1):
            print(l1)
        else:
            print(l2)
    
fast()