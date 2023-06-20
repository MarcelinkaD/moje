# https://szkopul.edu.pl/problemset/problem/Geba-YXAmWHFnOUgimkYmoUT/site/?key=statement

from itertools import accumulate as ac
from sys import stdin
input = stdin.readline

def main():
    n = int(input())
    mias = list(map(int, input().split()))
    drogi = list(map(int, input().split()))
    mini = 1e18
    start = -1
    sumy = list(ac(drogi))
    max_w = -1
    
    for i in range(n):
        if mias[i] < mini:
            mini = mias[i]
            start = i
            
    for i in range(n):
        if i != start:
            w = mias[i]
            if i < start:
                if i != 0:
                    w -= sumy[start - 1] - sumy[i - 1]
                else:
                    w -= sumy[start - 1]
            else:
                if i - start != 1:
                    w -= sumy[i - 1] - sumy[start]
                else:
                    w -= sumy[i - 1]
                
            max_w = max(max_w, w - mini)
    
    if max_w == -1:
        print(0)
    else:
        print(max_w)
    
main()