# https://szkopul.edu.pl/problemset/problem/kjKReZKZ62uxjVY3TVkHiz2u/site/?key=statement

import sys
from sys import stdin
input = stdin.readline
sys.setrecursionlimit(10**6)


def f(x, y, n, c):    
    if x == 1:
        return y + c
    elif y == n:
        return ((n + x) - 1) + c
    elif x == n:
        return (((3 * n) - y) - 1) + c
    elif y == 1:
        return (((4 * n) - x) - 2) + c
    else:
        return f(x - 1, y - 1, n - 2, (4 * n - 4) + c)
    
def X1(x, y, n, c):
    return f(y, n - x + 1, n, c)

def X2(x, y, n, c):
    return f(n - x + 1, n - y + 1, n, c)

def X3(x, y, n, c):
    return f(n - y + 1, x, n, c)                                                                                                                                                                                                                    

def main():
    n, kierunek, zwrot = map(str, input().split())
    sx, kx, sy, ky = map(int, input().split())
    n = int(n)
    c = 0
    
    for i in range(ky, sy - 1, -1):
        for j in range(sx, kx + 1):
            if kierunek == "POLNOC":
                if zwrot == "PRAWO":
                    print(f(j, i, n, c), end = " ")
                else:
                    print(X3(i, j, n, c), end = " ")
            elif kierunek == "WSCHOD":
                if zwrot == "PRAWO":
                    print(X3(j, i, n, c), end = " ")
                else:
                    print(f(i, j, n, c), end = " ")
            elif kierunek == "POLUDNIE":
                if zwrot == "PRAWO":
                    print(X2(j, i, n, c), end = " ")
                else:
                    print(X1(i, j, n, c), end = " ")
            else:
                if zwrot == "PRAWO":
                    print(X1(j, i, n, c), end = " ")
                else:
                    print(X2(i, j, n, c), end = " ")
                    
        print("")
    
main()