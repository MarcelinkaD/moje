# https://szkopul.edu.pl/problemset/problem/Vtr5pP-RRtjqnivWocv8xaad/site/?key=statement

from sys import stdin
input = stdin.readline

def sum_w(n, prze):
    w = [0] * (n + 2)
    suma = 0
    for i in range(n, 0, -1):
        suma += prze[i]
        w[i] = w[i + 1] + suma
    return w

def main():
    n = int(input())
    l = list(map(int, input().split()))
    l.append(0)
    q = int(input())
    prze = [0] * (n + 1)
    akt_dl = 1
    
    for i in range(n):
        if l[i] < l[i + 1]:
            akt_dl += 1
        else:
            prze[akt_dl] += 1
            akt_dl = 1
    
    w = sum_w(n, prze)
    
    for _ in range(q):
        k = int(input())
        print(w[k])
                     
main()