# https://szkopul.edu.pl/problemset/problem/GE48t27fgAbn4WNGoGhVChb-/site/?key=statement

from sys import stdin
input = stdin.readline

def main():
    n, q = map(int, input().split())
    t = list(map(int, input().split()))
    w = [0 for _ in range(n + 1)]
    w[n] = n
    w[n - 1] = n
    t.insert(0, 0)
    
    for i in range(n - 2, 0, -1):
        if t[i + 2] - t[i + 1] == t[i + 1] - t[i]:
            w[i] = w[i + 1]
        else:
            w[i] = i + 1
        
    for _ in range(q):
        od, do = map(int, input().split())
        
        if w[od] >= do:
            print("TAK")
        else:
            print("NIE")


main()