import bisect as bis
from sys import stdin
input = stdin.readline

def binary(li, n):
	g = bis.bisect_left(li, n)
	if g != len(li) and li[g] == n:
		return g
	else:
		return -1


def main():
	n, k = map(int, input().split())
	l = list(map(int, input().split()))
	l.sort()
	
	print(binary(l, k))
	
main()
