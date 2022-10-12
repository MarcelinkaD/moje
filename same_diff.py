from collections import *
from sys import stdin
input = stdin.readline

def main():
	tc = int(input())
	for _ in range(tc):
		input()
		l = [x - i for i, x in enumerate(map(int, input().split()))]
		breakpoint()
		g = Counter(l)
		ans = 0
		for k in g:
			ans += (g[k] * (g[k]-1)) // 2
		print(ans)
main()
