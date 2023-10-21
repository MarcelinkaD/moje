# https://szkopul.edu.pl/problemset/problem/XJGk8X4KSGw8yuy5EYEy4rSK/site/?key=statement

from sys import stdin
input = stdin.readline

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    a.sort()
    b.sort()
    
    w = 0
    
    for i in range(n):
        k = str(a[i]) + str(b[(n - 1) - i])
        w += int(k)
        
    print(w)
    
    
main()