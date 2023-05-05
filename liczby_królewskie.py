# https://szkopul.edu.pl/c/olimpiada-poziom-ii-202223/p/krolewskie/

from sys import stdin
input = stdin.readline

def czy_kro(n):
    w = 0
    while n >= 1:
        w += n % 2
        n //= 2
        
    return w % 2 == 0

def main():
    q = int(input())
    
    for _ in range(q):
        k = int(input())
        l1 = 2 * k - 1
        l2 = 2 * k - 2
        
        if czy_kro(l1):
            print(l1)
        else:
            print(l2)
    
main()