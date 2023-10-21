# https://szkopul.edu.pl/problemset/problem/ZhrqkG9W7TYF2VPrIuR1Ufry/site/?key=statement

from collections import Counter as C
from sys import stdin
input = stdin.readline

def main():
    n, m = map(int, input().split())
    row = [0] * n
    col = [0] * m

    result = 0
    for i in range(n):
        s = str(input().strip())
        for j in range(m):
            if s[j] == '#':
                row[i] += 1
                col[j] += 1
                result += 2

    result -= max(row)
    result -= max(col)
    print(result)

main()