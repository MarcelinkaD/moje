# https://szkopul.edu.pl/problemset/problem/ERz8Uez5UFnNbPH2Jn965eZ3/site/?key=statement

from sys import stdin
input = stdin.readline

def order(x):
    return (len(x), x)

def main():
    n = int(input())
    w = []
    
    for _ in range(n):
        w.append(str(input().strip()))
        
    w = sorted(w, key = lambda j: order(j))
    
    for i in w:
        print(i)
    
main()