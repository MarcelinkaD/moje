import bisect
from sys import stdin
input = stdin.readline

def binary(li, n):
	g = bisect.bisect_left(li, n)
	if g != len(li) and li[g] == n:
		return g
	else:
		return -1

def main():
	n, k = map(int, input().split())
	pierwsza = sorted(list(map(int, input().split())))
	druga = list(map(int, input().split()))
	
	for i in druga:
		if binary(pierwsza, i) != -1:
			print("YES")
		else:
			print("NO")
		
main()
