# https://szkopul.edu.pl/problemset/problem/eqMHKut-ZAURUhO6-eIEUQS7/site/?key=statement

from sys import stdin
import bisect as bi
input = stdin.readline

def f(x):
    w = 0
    while x > 0:
        w += x % 10
        x //= 10
    return w

def g(x):
    fn = f(x)
    return x + fn * fn

def main():
    q = int(input())
    LIMIT = 5000000000
    M = []
    
    for i in range(q):
        m = int(input())
        M.append((m, i))
    
    M.sort()
    odpowiedz = [False for _ in range(q)]
    n = 1
    wsk_m = 0
    
    while n <= LIMIT:
        while wsk_m < q and M[wsk_m][0] < n:
            wsk_m += 1
            
        while wsk_m < q and M[wsk_m][0] == n:
            odpowiedz[M[wsk_m][1]] = True
            wsk_m += 1
            
        n = g(n)
        
    for i in range(q):
        if odpowiedz[i]:
            print("TAK")
        else:
            print("NIE")
    
main()