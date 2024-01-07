# https://szkopul.edu.pl/problemset/problem/h7P1F1yz9gBplZVMII4a442e/site/?key=statement

from sys import stdin
input = stdin.readline

def main():
    n = int(input())
    trees = str(input().strip())
    t = [1 if tree == 'J' else -1 for tree in trees]
    suma = sum(t)

    def rob(l, p):
        v = (suma - l - p) // 3
        pom = 0
        lewy = prawy = n

        for i in range(n - 4):
            pom += t[i]
            if pom == v and t[i + 1] == l and lewy == n:
                lewy = i + 1

        pom = 0
        for i in range(n - 1, lewy + 2, -1):
            pom += t[i]
            if pom == v and t[i - 1] == p:
                prawy = i - 1

        return (lewy, prawy) if prawy != n else (n, n)

    res = (n, n)
    if (suma + 2) % 3 == 0:
        res = min(res, rob(-1, -1))
    if suma % 3 == 0:
        res = min(res, rob(-1, 1), rob(1, -1))
    if (suma - 2) % 3 == 0:
        res = min(res, rob(1, 1))

    return res if res[0] != n else "BRAK"
    
w = main()
if w != "BRAK":
    print(w[0] + 1, w[1] + 1)
else:
    print(w)